import os
import sys
import yt_dlp
import logging

# Konfigurasi logging
logging.basicConfig(level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

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
        # Buat direktori download jika belum ada
        os.makedirs(output_path, exist_ok=True)
        
        # Konfigurasi yt-dlp
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'prefer_ffmpeg': True,
            'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
            'default_search': 'ytsearch1:',  # Mencari video pertama
            'nooverwrites': True,
            'no_warnings': False,
            'ignoreerrors': False,
            'no_color': True,
        }
        
        # Gunakan yt-dlp untuk download
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Pencarian dan download dalam satu langkah
            ydl.download([song_name])
        
        logging.info(f"Berhasil download lagu: {song_name}")
        return True
    
    except Exception as e:
        logging.error(f"Kesalahan saat download lagu {song_name}: {e}")
        return False

def download_songs_from_list(file_path):
    """
    Download lagu dari daftar di file txt
    
    Args:
        file_path (str): Path file txt berisi daftar lagu
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            songs = [line.strip() for line in file if line.strip()]
        
        # Simpan log lagu yang gagal
        failed_songs = []
        
        for song in songs:
            logging.info(f"Memproses lagu: {song}")
            success = search_and_download_song(song)
            
            if not success:
                failed_songs.append(song)
        
        # Tampilkan daftar lagu yang gagal di akhir proses
        if failed_songs:
            logging.warning("Lagu-lagu yang gagal didownload:")
            for song in failed_songs:
                logging.warning(song)
    
    except FileNotFoundError:
        logging.error(f"File tidak ditemukan: {file_path}")
    except Exception as e:
        logging.error(f"Kesalahan umum: {e}")

# Program utama dengan penanganan KeyboardInterrupt
if __name__ == "__main__":
    try:
        # Pastikan Anda sudah membuat file list.txt dengan daftar lagu
        download_songs_from_list('list.txt')
    except KeyboardInterrupt:
        logging.warning("\nProses dihentikan oleh pengguna. Keluar dari program.")
