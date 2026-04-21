# video-downloader

Small Python helper to download a single YouTube video using [yt-dlp](https://github.com/yt-dlp/yt-dlp). Playlists are ignored (`noplaylist`).

## Requirements

- Python 3
- Dependencies from `requirements.txt` (installs `yt-dlp`)
- **ffmpeg** on your PATH if you use `--audio-only` (MP3 extraction) or when yt-dlp needs to merge separate video and audio streams into MP4

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

On macOS/Linux, activate with `source .venv/bin/activate`.

## Usage

```bash
python download.py "https://www.youtube.com/watch?v=VIDEO_ID"
```

Files are written under `downloads/` by default, named like `Title [video_id].mp4` (or `.mp3` with `--audio-only`).

### Options

| Option | Description |
|--------|-------------|
| `-o`, `--output` | Output directory (default: `downloads`) |
| `-f`, `--format` | yt-dlp format selector (default: `bv*+ba/b` — best video + best audio, or best single file) |
| `--audio-only` | Best audio only, saved as MP3 at 192 kbps (requires ffmpeg) |
| `-q`, `--quiet` | Less console output |

### Examples

```bash
python download.py "https://youtu.be/..." -o "C:\Videos\my-rip"
python download.py "https://www.youtube.com/watch?v=..." --audio-only
python download.py "https://www.youtube.com/watch?v=..." -f "best[height<=720]"
```

## Legal note

Only download content you have the right to access. Respect YouTube’s terms of service and applicable copyright law.
