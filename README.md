# Bot Feedback dan Rating

Ini adalah kode bot Feedback dan Rating berbasis Telegram. Bot ini memungkinkan pengguna untuk memberikan rating dan feedback untuk bot tersebut. Bot ini dibuat menggunakan bahasa pemrograman Python dan menggunakan library Telegram Bot API.

## Penggunaan

Untuk menggunakan bot ini, Anda dapat mengunduh kode ini atau melakukan clone dari repository GitHub ini. Setelah itu, lakukan installasi dependencies dengan perintah berikut:

```bash
pip install python-telegram-bot
```

Setelah selesai menginstal dependencies, jalankan bot dengan cara berikut:

```bash
python main.py
```

## Fitur

Bot ini memiliki dua fitur utama, yaitu:

1. Rating
Pengguna dapat memberikan rating dengan mengklik tombol rating yang disediakan.

2. Feedback
Pengguna dapat memberikan feedback dengan mengetikkan pesan feedback yang akan diteruskan ke owner bot.

## Konfigurasi

Sebelum menjalankan bot, pastikan untuk melakukan konfigurasi pada file `app.json` terlebih dahulu dengan mengisi token bot dan id owner bot.

## Deploy

Anda dapat deploy bot ini di beberapa platform seperti Heroku, Replit, dan VPS dengan mengikuti langkah-langkah berikut:

### Heroku

1. Buat akun di [Heroku](https://www.heroku.com/).
2. Buat aplikasi baru dan terhubung ke GitHub Anda.
3. Aktifkan fitur auto deploy untuk melakukan deploy secara otomatis setiap kali ada perubahan pada GitHub.
4. Pastikan untuk mengisi variabel `TOKEN` dan `OWNER_ID` pada fitur Config Variables.

### Replit

1. Buat akun di [Replit](https://replit.com/).
2. Buat repl baru dengan memilih Python sebagai bahasa pemrograman.
3. Upload kode dari bot ini ke dalam repl Anda.
4. Install dependencies dengan perintah `pip install python-telegram-bot`.
5. Jalankan bot dengan perintah `python main.py`.
6. Aktifkan fitur Always On agar bot tetap berjalan.

### VPS

1. Siapkan VPS dengan sistem operasi Ubuntu.
2. Install dependencies dengan perintah berikut:

   ```bash
   sudo apt-get update
   sudo apt-get install python3-pip
   pip3 install python-telegram-bot
   ```

3. Upload kode dari bot ini ke dalam VPS Anda.
4. Jalankan bot dengan perintah `python3 main.py`.
5. Untuk menjalankan bot di background, gunakan perintah berikut:

   ```bash
   nohup python3 main.py > bot.log 2>&1 &
   ``` 

## Kontributor

- Nama: [Miftah GanzZ]
- Email: [miftahazzam09@gmail.com]
