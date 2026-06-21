# 🎵 YouTube Song Downloader

Skrip Python otomatis dan ringan untuk mengunduh audio dari YouTube secara massal (batch) dan mengonversinya menjadi file MP3 berkualitas tinggi menggunakan `yt-dlp` dan `FFmpeg`.

---

## ✨ Fitur

- **Unduh Massal (Batch)**: Membaca judul lagu atau tautan YouTube dari file `.txt` dan mengunduhnya secara berurutan.
- **Konversi MP3 Otomatis**: Secara otomatis mengekstrak dan mengonversi audio ke format MP3 (192 kbps) menggunakan FFmpeg.
- **Pengaturan Ekstraktor Kuat**: Dikonfigurasi dengan client player yang dioptimalkan (`android` dan `web`) serta header khusus untuk menghindari pembatasan (rate limit/blocking) dari YouTube.
- **Tampilan Konsol Bersih**: Dilengkapi dengan logger senyap khusus dan indikator progres yang menampilkan kecepatan unduh, persentase, serta perkiraan waktu selesai (ETA).
- **Pencegahan Duplikat**: Melewati file yang sudah pernah diunduh sebelumnya untuk menghemat kuota internet Anda.

---

## 🛠️ Prasyarat

Untuk menjalankan skrip ini, Anda harus menginstal beberapa dependensi berikut pada sistem Anda:

1. **Python 3.7+**
2. **FFmpeg** (Pastikan sudah terdaftar di PATH sistem Anda)
   - *Windows*: Unduh dari [ffmpeg.org](https://ffmpeg.org/download.html) atau instal melalui `scoop install ffmpeg` / `choco install ffmpeg`.
   - *macOS*: `brew install ffmpeg`
   - *Linux*: `sudo apt install ffmpeg`

---

## 🚀 Instalasi & Persiapan

1. **Klon repositori ini**:
   ```bash
   git clone https://github.com/aziiemuth/downloader-song.git
   cd downloader-song
   ```

2. **Siapkan daftar lagu**:
   Buat sebuah file teks (contoh: `list.txt`) di dalam direktori utama. Tuliskan setiap judul lagu, kata kunci pencarian, atau URL YouTube di baris baru:
   ```text
   Linkin Park - In The End
   Geisha - Jika Cinta Dia
   https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

---

## 💻 Penggunaan

Jalankan skrip menggunakan Python:

```bash
python main.py
```

1. Skrip akan meminta nama file daftar lagu Anda:
   ```text
   Nama file daftar lagu (.txt tidak perlu ditulis): list
   ```
2. Masukkan nama file (tanpa menulis `.txt`) lalu tekan Enter.
3. Skrip akan mulai mencari, mengunduh, dan mengonversi setiap lagu secara otomatis.
4. File MP3 hasil unduhan akan disimpan di dalam folder `downloads/`.

---

## 📝 Lisensi

Proyek ini bersifat open-source dan dirilis di bawah [Lisensi MIT](LICENSE).
