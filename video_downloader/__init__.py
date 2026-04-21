"""YouTube download helper built on yt-dlp."""

from video_downloader.client import download_urls
from video_downloader.options import build_ytdlp_opts

__all__ = ["build_ytdlp_opts", "download_urls"]
