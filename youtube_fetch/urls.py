"""YouTube URL checks."""

from __future__ import annotations

from urllib.parse import urlparse

_YT_HOSTS = frozenset(
    {
        "youtube.com",
        "m.youtube.com",
        "music.youtube.com",
        "youtu.be",
    }
)


def is_youtube_url(url: str) -> bool:
    """Return True if the URL is http(s) and targets a known YouTube host."""
    try:
        parsed = urlparse(url.strip())
    except (TypeError, ValueError):
        return False
    if parsed.scheme not in ("http", "https"):
        return False
    host = (parsed.netloc or "").lower()
    if ":" in host:
        host = host.rsplit(":", 1)[0]
    if host.startswith("www."):
        host = host[4:]
    return host in _YT_HOSTS
