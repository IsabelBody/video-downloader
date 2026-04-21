"""Command-line interface."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yt_dlp

from video_downloader.client import download_urls
from video_downloader.options import build_ytdlp_opts


def _parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="video-downloader",
        description="Download a YouTube video (requires yt-dlp; audio-as-mp3 needs ffmpeg on PATH).",
    )
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument(
        "-o",
        "--output",
        default="downloads",
        help="Output directory (default: downloads)",
    )
    parser.add_argument(
        "-f",
        "--format",
        default="bv*+ba/b",
        help="yt-dlp format selector (default: best video + best audio, or best single file)",
    )
    parser.add_argument(
        "--audio-only",
        action="store_true",
        help="Download best audio and save as MP3 (needs ffmpeg)",
    )
    parser.add_argument(
        "-q",
        "--quiet",
        action="store_true",
        help="Less console output",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = _parse_args(argv)

    output_dir = Path(args.output).resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    opts = build_ytdlp_opts(
        output_dir,
        format_spec=args.format,
        audio_only=args.audio_only,
        quiet=args.quiet,
    )

    try:
        download_urls([args.url], opts)
    except yt_dlp.utils.DownloadError as e:
        print(f"Download failed: {e}", file=sys.stderr)
        return 1
    return 0
