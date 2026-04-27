# youtube-fetch

Small Python CLI that downloads **one** YouTube video (or audio only) from a watch URL using [yt-dlp](https://github.com/yt-dlp/yt-dlp). The repo folder may be named `video-downloader`; the installable package and module name are **`youtube_fetch`**.

## What this tool does

- Accepts a single URL argument, validates it against known YouTube hosts, then runs yt-dlp once.
- **Playlists are never expanded**: `noplaylist` is set, so a playlist URL still only fetches the single video that URL refers to (not the whole list).
- Writes files under an output directory you choose (default **`output/`** next to your current working directory).
- Default filename pattern: `Title [video_id].ext` (see [Output files](#output-files)).

## Prerequisites

1. **Python 3** (3.10+ recommended; no version pin in repo).
2. **This repo** cloned or copied locally.
3. **ffmpeg** on your `PATH` when you:
   - use `--audio-only` (MP3 extraction), or
   - yt-dlp needs to merge separate best video and best audio into one MP4.

4. **Internet access** to reach YouTube.

## Install and run (first time)

All commands below assume your shell’s **current directory is the repository root** (the folder that contains `requirements.txt` and the `youtube_fetch/` package).

### 1. Create and activate a virtual environment

**Windows (PowerShell or cmd):**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

This installs `yt-dlp` and `click` (see `requirements.txt`).

### 3. Download one video

```bash
python -m youtube_fetch "https://www.youtube.com/watch?v=VIDEO_ID"
```

Replace `VIDEO_ID` with a real id, or use a full `https://youtu.be/...` link.

### 4. Get help

```bash
python -m youtube_fetch -h
```

## Allowed URLs

Only **http** or **https** links whose host (after stripping `www.` and port) is one of:

| Host |
|------|
| `youtube.com` |
| `m.youtube.com` |
| `music.youtube.com` |
| `youtu.be` |

Any other URL is rejected before download starts.

## Output files

- **Directory**: `-o` / `--output` (default: `output`). The directory is created if it does not exist; path is resolved to an absolute path.
- **Template**: `%(title)s [%(id)s].%(ext)s` inside that directory (sanitization follows yt-dlp rules for filenames).
- **Video (default)**: merged container **`mp4`** when separate streams are combined (`merge_output_format`: `mp4`).
- **Audio**: with `--audio-only`, format is best audio, post-processed to **MP3 at 192 kbps**.

## Usage reference

**Invocation pattern:**

```text
python -m youtube_fetch <URL> [options]
```

**`URL`** (positional): one YouTube watch or share link as above.

### Options

| Option | Description |
|--------|-------------|
| `-o`, `--output` | Output directory (default: `output`) |
| `-f`, `--format` | yt-dlp [format selector](https://github.com/yt-dlp/yt-dlp#format-selection) (default: `bv*+ba/b` — best video + best audio, or best single file) |
| `--audio-only` | Best audio only, saved as MP3 (requires ffmpeg) |
| `-q`, `--quiet` | Less console output (`quiet` and `no_warnings` in yt-dlp) |
| `--cookies` | Path to a **Netscape** cookies file (must exist). See yt-dlp wiki for exporting YouTube cookies. |
| `--cookies-from-browser` | Let yt-dlp read cookies from a browser, e.g. `edge` or `chrome:ProfileName`. **Close the browser first.** |

You **cannot** pass both `--cookies` and `--cookies-from-browser`; the CLI exits with a usage error if you do.

### Examples

```bash
python -m youtube_fetch "https://youtu.be/VIDEO_ID"
python -m youtube_fetch "https://www.youtube.com/watch?v=..." -o "C:\Videos\my-clips"
python -m youtube_fetch "https://www.youtube.com/watch?v=..." --audio-only
python -m youtube_fetch "https://www.youtube.com/watch?v=..." -f "best[height<=720]"
```

## Troubleshooting

- **`Could not complete: ...`**: yt-dlp failed (network, geo, age gate, removed video, etc.). Read the message; try `--cookies` or `--cookies-from-browser` if YouTube requires a logged-in session.
- **Merge / MP3 errors**: install ffmpeg and ensure `ffmpeg` is on your `PATH`.
- **`URL must be a YouTube link`**: host not in the allowed list; use a standard YouTube URL.

## Legal note

Only use content you are allowed to access. Follow YouTube’s terms of service and applicable copyright law.
