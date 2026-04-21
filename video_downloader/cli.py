"""Command-line interface."""

from __future__ import annotations

from pathlib import Path

import click
import yt_dlp

from video_downloader.client import download_urls
from video_downloader.options import build_ytdlp_opts


@click.command(
    name="video-downloader",
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.argument("url")
@click.option(
    "-o",
    "--output",
    default="downloads",
    show_default=True,
    help="Output directory",
)
@click.option(
    "-f",
    "--format",
    "format_spec",
    default="bv*+ba/b",
    show_default=True,
    help="yt-dlp format selector (best video + best audio, or best single file)",
)
@click.option(
    "--audio-only",
    is_flag=True,
    help="Download best audio and save as MP3 (needs ffmpeg)",
)
@click.option(
    "-q",
    "--quiet",
    is_flag=True,
    help="Less console output",
)
def main(url: str, output: str, format_spec: str, audio_only: bool, quiet: bool) -> None:
    """Download a YouTube video (requires yt-dlp; audio-as-mp3 needs ffmpeg on PATH)."""
    output_dir = Path(output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    opts = build_ytdlp_opts(
        output_dir,
        format_spec=format_spec,
        audio_only=audio_only,
        quiet=quiet,
    )

    try:
        download_urls([url], opts)
    except yt_dlp.utils.DownloadError as e:
        raise click.ClickException(f"Download failed: {e}") from e
