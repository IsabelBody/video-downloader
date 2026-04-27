# Agent and contributor notes

This file summarizes **how the repository is organized** and **how to run and change the tool**. It is not a product roadmap.

## Purpose

CLI wrapper around **yt-dlp** that downloads **a single YouTube URL** with strict URL validation and `noplaylist: True`. No other sites are supported.

## How users run it

From the **repository root** (directory containing `requirements.txt`):

```bash
pip install -r requirements.txt
python -m youtube_fetch "<youtube-url>" [options]
```

Help: `python -m youtube_fetch -h`.

Entry point: `youtube_fetch/__main__.py` calls `youtube_fetch.cli.main`.

## Layout

| Path | Role |
|------|------|
| `requirements.txt` | Runtime deps: `yt-dlp`, `click`. |
| `youtube_fetch/__main__.py` | Module entry: `main()` from `cli`. |
| `youtube_fetch/cli.py` | Click command: arguments, validation, output dir, builds opts, calls download. |
| `youtube_fetch/options.py` | `build_ytdlp_opts()` — output template, `noplaylist`, format/audio/postprocessors, cookies. `parse_cookies_from_browser()` for `--cookies-from-browser`. |
| `youtube_fetch/urls.py` | `is_youtube_url()` — allowed hosts only. |
| `youtube_fetch/client.py` | `fetch_youtube_urls(urls, opts)` — `yt_dlp.YoutubeDL(opts).download(urls)`. |

There is **no test suite** in this repo yet; changes should be verified manually with `python -m youtube_fetch` and a known-good URL.

## Behavior details (for accurate docs and changes)

- **URL gate**: CLI raises `click.BadParameter` if `is_youtube_url(url)` is false.
- **Cookies**: If both `--cookies` and `--cookies-from-browser` are set, `click.UsageError`.
- **Output**: `Path(output).resolve()`; `mkdir(parents=True, exist_ok=True)`.
- **yt-dlp opts** (from `build_ytdlp_opts`): `outtmpl` under `output_dir`, `noplaylist`, `quiet` / `no_warnings`, optional `cookiefile` / `cookiesfrombrowser`, video branch sets `format` + `merge_output_format: mp4`, audio branch sets `format: bestaudio/best` and FFmpeg MP3 postprocessor at 192 kbps.
- **Errors**: `yt_dlp.utils.DownloadError` is caught in `cli.main` and re-raised as `click.ClickException`.

## Where to extend

- **New hosts**: edit `_YT_HOSTS` and logic in `youtube_fetch/urls.py` (keep scheme/host rules consistent with `is_youtube_url`).
- **New CLI flags**: add Click options in `youtube_fetch/cli.py`, thread into `build_ytdlp_opts` in `youtube_fetch/options.py`.
- **Download behavior**: prefer adjusting opts in `options.py` or the thin wrapper in `client.py` rather than duplicating yt-dlp calls.

## README

User-facing setup, URL rules, options table, and examples live in **`README.md`**. Keep README and this file aligned when behavior changes.
