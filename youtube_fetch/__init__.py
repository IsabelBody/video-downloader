"""YouTube media helper built on yt-dlp."""

from youtube_fetch.client import fetch_youtube_urls
from youtube_fetch.options import build_ytdlp_opts
from youtube_fetch.urls import is_youtube_url

__all__ = ["build_ytdlp_opts", "fetch_youtube_urls", "is_youtube_url"]
