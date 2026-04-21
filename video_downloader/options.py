"""yt-dlp option dictionaries for this project."""

from __future__ import annotations

from pathlib import Path


def build_ytdlp_opts(
    output_dir: Path,
    *,
    format_spec: str,
    audio_only: bool,
    quiet: bool,
) -> dict:
    outtmpl = str(output_dir / "%(title)s [%(id)s].%(ext)s")
    opts: dict = {
        "outtmpl": outtmpl,
        "noplaylist": True,
        "quiet": quiet,
        "no_warnings": quiet,
    }

    if audio_only:
        opts["format"] = "bestaudio/best"
        opts["postprocessors"] = [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ]
    else:
        opts["format"] = format_spec
        opts["merge_output_format"] = "mp4"

    return opts
