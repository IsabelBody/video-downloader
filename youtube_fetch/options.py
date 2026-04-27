"""yt-dlp option dictionaries for this project."""



from __future__ import annotations



from pathlib import Path





def parse_cookies_from_browser(spec: str) -> tuple[str, ...]:

    """Turn `edge` or `chrome:ProfileName` into a yt-dlp cookiesfrombrowser tuple."""

    parts = [p for p in spec.split(":", 1) if p]

    if not parts:

        raise ValueError("empty --cookies-from-browser value")

    if len(parts) == 1:

        return (parts[0],)

    return (parts[0], parts[1])





def build_ytdlp_opts(

    output_dir: Path,

    *,

    format_spec: str,

    audio_only: bool,

    quiet: bool,

    cookiefile: Path | None = None,

    cookiesfrombrowser: tuple[str, ...] | None = None,

) -> dict:

    outtmpl = str(output_dir / "%(title)s [%(id)s].%(ext)s")

    opts: dict = {

        "outtmpl": outtmpl,

        "noplaylist": True,

        "quiet": quiet,

        "no_warnings": quiet,

    }



    if cookiefile is not None:

        opts["cookiefile"] = str(cookiefile.resolve())

    if cookiesfrombrowser is not None:

        opts["cookiesfrombrowser"] = cookiesfrombrowser



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

