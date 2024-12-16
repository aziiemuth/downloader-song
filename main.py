"""
Script Download Lagu dari YouTube

Author: athiief
"""

import os
import sys
import yt_dlp
import logging

# Auto-install pyfiglet jika belum terpasang
try:
    import pyfiglet
except ImportError:
    os.system('pip install pyfiglet')
    import pyfiglet

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.StreamHandler()
        ]
    )

def show_banner():
    # Menampilkan banner Author seperti ASCII art
    author_banner = pyfiglet.figlet_format("A T H I E F")
    print(author_banner)
    print("=" * 50)
    print("     YouTube Song Downloader      ")
    print("=" * 50)
    print()

def search_and_download_song(song_name, output_path='downloads'):
    """
    Mencari dan mendownload lagu dari YouTube

    Args:
        song_name (str): Nama lagu yang dicari
        output_path (str): Direktori untuk menyimpan download

    Returns:
        bool: True jika berhasil download, False jika gagal
    """
    try:
        os.makedirs(output_path, exist_ok=True)

        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'prefer_ffmpeg': True,
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'default_search': 'ytsearch1:',
            'nooverwrites': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_name])

        logging.info(f"Berhasil mendownload: {song_name}")
        return True

    except Exception as e:
        logging.error(f"Gagal mendownload {song_name}: {e}")
        return False

def download_songs_from_list(file_name):
    """
    Download lagu dari daftar di file txt

    Args:
        file_name (str): Nama file (tanpa .txt) berisi daftar lagu
    """
    file_path = file_name + '.txt'

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            songs = [line.strip() for line in file if line.strip()]

        if not songs:
            logging.warning("File daftar lagu kosong. Tidak ada lagu untuk diproses.")
            return False

        logging.info(f"Jumlah lagu yang akan diproses: {len(songs)}")

        failed_songs = []

        for idx, song in enumerate(songs, start=1):
            logging.info(f"[{idx}/{len(songs)}] Sedang memproses: {song}")
            success = search_and_download_song(song)
            if not success:
                failed_songs.append(song)

        if failed_songs:
            logging.warning("\nLagu yang gagal diunduh:")
            for song in failed_songs:
                logging.warning(f" - {song}")
        else:
            logging.info("Semua lagu berhasil diunduh.")
        return True

    except FileNotFoundError:
        logging.error(f"File tidak ditemukan: {file_path}")
        return False
    except Exception as e:
        logging.error(f"Terjadi kesalahan: {e}")
        return False

def main():
    show_banner()

    while True:
        file_name = input("Masukkan nama file daftar lagu : ").strip()

        if not file_name:
            logging.error("Nama file tidak boleh kosong. Coba lagi.")
            continue

        if download_songs_from_list(file_name):
            break
        else:
            logging.warning("Coba lagi dengan file yang valid.")

if __name__ == "__main__":
    try:
        setup_logging()
        main()
    except KeyboardInterrupt:
        logging.warning("\nProses dihentikan oleh pengguna.")
        input("\nTekan Enter untuk keluar...")
