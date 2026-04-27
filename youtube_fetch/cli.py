"""Command-line interface for YouTube media."""

from __future__ import annotations

from pathlib import Path

import click
import yt_dlp

from youtube_fetch.client import fetch_youtube_urls
from youtube_fetch.options import build_ytdlp_opts, parse_cookies_from_browser
from youtube_fetch.urls import is_youtube_url


@click.command(
    name="youtube-fetch",
    context_settings={"help_option_names": ["-h", "--help"]},
)
@click.argument("url")
@click.option(
    "-o",
    "--output",
    default="output",
    show_default=True,
    help="Directory to write files into",
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
    help="Save best audio only as MP3 (needs ffmpeg)",
)
@click.option(
    "-q",
    "--quiet",
    is_flag=True,
    help="Less console output",
)
@click.option(
    "--cookies",
    "cookiefile",
    type=click.Path(path_type=Path, exists=True, dir_okay=False),
    default=None,
    help="Netscape-format cookies file (see yt-dlp wiki: exporting YouTube cookies)",
)
@click.option(
    "--cookies-from-browser",
    "cookies_browser_spec",
    default=None,
    help="Browser for yt-dlp to read cookies from, e.g. edge or chrome:ProfileName. Close the browser first.",
)
def main(
    url: str,
    output: str,
    format_spec: str,
    audio_only: bool,
    quiet: bool,
    cookiefile: Path | None,
    cookies_browser_spec: str | None,
) -> None:
    """Save a single YouTube video or audio track locally (uses yt-dlp; MP3 needs ffmpeg on PATH)."""
    if not is_youtube_url(url):
        raise click.BadParameter("URL must be a YouTube link (e.g. youtube.com or youtu.be).", param_hint="url")

    if cookiefile is not None and cookies_browser_spec is not None:
        raise click.UsageError("Use only one of --cookies and --cookies-from-browser.")

    output_dir = Path(output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    cookiesfrombrowser = None
    if cookies_browser_spec is not None:
        try:
            cookiesfrombrowser = parse_cookies_from_browser(cookies_browser_spec)
        except ValueError as e:
            raise click.BadParameter(str(e), param_hint="--cookies-from-browser") from e

    opts = build_ytdlp_opts(
        output_dir,
        format_spec=format_spec,
        audio_only=audio_only,
        quiet=quiet,
        cookiefile=cookiefile,
        cookiesfrombrowser=cookiesfrombrowser,
    )

    try:
        fetch_youtube_urls([url], opts)
    except yt_dlp.utils.DownloadError as e:
        raise click.ClickException(f"Could not complete: {e}") from e
