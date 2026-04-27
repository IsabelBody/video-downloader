"""Run yt-dlp with a prepared options dict."""

from __future__ import annotations

import yt_dlp


def fetch_youtube_urls(urls: list[str], opts: dict) -> None:
    with yt_dlp.YoutubeDL(opts) as ydl:
        ydl.download(urls)
