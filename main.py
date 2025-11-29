"""
YouTube Song Downloader
Author  : athiief
Features: web_safari client, progress bar, silent warnings
"""

import os
import sys
import logging
import subprocess

try:
    import yt_dlp
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "yt-dlp"])
    import yt_dlp


def setup_log():
    logging.basicConfig(
        level=logging.INFO,
        format="%(message)s",
        handlers=[logging.StreamHandler()]
    )


class QuietLogger:
    def debug(self, msg):
        pass
    def warning(self, msg):
        pass
    def info(self, msg):
        if msg and not str(msg).startswith("WARNING:"):
            print(msg)
    def error(self, msg):
        print(msg)


def progress_hook(data):
    if data.get("status") == "downloading":
        percent = data.get("_percent_str", "").strip()
        speed   = data.get("_speed_str", "").strip()
        eta     = data.get("_eta_str", "").strip()
        print(f"\r{percent} | {speed} | ETA {eta}", end="")
    if data.get("status") == "finished":
        print("\nMengubah audio...")


def get_title(query):
    opts = {
        "default_search": "ytsearch1:",
        "skip_download": True,
        "quiet": True,
        "logger": QuietLogger()
    }
    with yt_dlp.YoutubeDL(opts) as y:
        info = y.extract_info(query, download=False)
        if not info:
            return query
        if "entries" in info:
            return info["entries"][0].get("title", query)
        return info.get("title", query)


def download(query, out="downloads"):
    os.makedirs(out, exist_ok=True)

    title = get_title(query)
    clean  = "".join(c for c in title if c.isalnum() or c in " ._-").strip()
    output_file = os.path.join(out, f"{clean}.mp3")

    if os.path.exists(output_file):
        print(f"Sudah ada: {clean}")
        return True

    opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(out, "%(title)s.%(ext)s"),
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192"
        }],

        "default_search": "ytsearch1:",
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
        "logger": QuietLogger(),

        "extractor_args": {
            "youtube": {"player_client": ["web_safari"]}
        },

        "progress_hooks": [progress_hook],
        "prefer_ffmpeg": True
    }

    try:
        with yt_dlp.YoutubeDL(opts) as y:
            y.download([query])
        print(f"Berhasil: {clean}")
        return True
    except Exception as e:
        print(f"Error saat download: {e}")
        return False


def load_list(file_name):
    path = file_name + ".txt"

    if not os.path.exists(path):
        print("File tidak ditemukan:", path)
        return

    with open(path, "r", encoding="utf-8") as file:
        items = [i.strip() for i in file if i.strip()]

    print("Total lagu:", len(items))

    for i, q in enumerate(items, 1):
        print(f"\n[{i}/{len(items)}] {q}")
        download(q)

    print("\nSelesai semua.")


def main():
    setup_log()
    print("YouTube Downloader by athiief\n")

    file_name = input("Nama file daftar lagu (.txt tidak perlu ditulis): ").strip()
    if not file_name:
        print("Nama file tidak boleh kosong.")
    else:
        load_list(file_name)

    input("\nTekan apa saja untuk keluar...")


if __name__ == "__main__":
    main()
