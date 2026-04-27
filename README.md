# youtube-fetch

Small Python helper for **YouTube only**: save a single video (or audio only) from a watch URL using [yt-dlp](https://github.com/yt-dlp/yt-dlp). Playlists are ignored (`noplaylist`).

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
python -m youtube_fetch "https://www.youtube.com/watch?v=VIDEO_ID"
```

Only `youtube.com`, `youtu.be`, `m.youtube.com`, and `music.youtube.com` links are accepted.

Files are written under `output/` by default, named like `Title [video_id].mp4` (or `.mp3` with `--audio-only`).

### Options

| Option | Description |
|--------|-------------|
| `-o`, `--output` | Output directory (default: `output`) |
| `-f`, `--format` | yt-dlp format selector (default: `bv*+ba/b` — best video + best audio, or best single file) |
| `--audio-only` | Best audio only, saved as MP3 at 192 kbps (requires ffmpeg) |
| `-q`, `--quiet` | Less console output |
| `--cookies` | Netscape cookies file (see yt-dlp wiki) |
| `--cookies-from-browser` | Browser for yt-dlp cookies, e.g. `edge` or `chrome:ProfileName` |

### Examples

```bash
python -m youtube_fetch "https://youtu.be/..." -o "C:\Videos\my-clips"
python -m youtube_fetch "https://www.youtube.com/watch?v=..." --audio-only
python -m youtube_fetch "https://www.youtube.com/watch?v=..." -f "best[height<=720]"
```

## Legal note

Only use content you are allowed to access. Follow YouTube’s terms of service and applicable copyright law.
