# Judul
Verify

# Challenge Description
Author: Jeffery John

People keep trying to trick my players with imitation flags. I want to make sure they get the real thing! I'm going to provide the SHA-256 hash and a decrypt script to help you know that my flags are legitimate. ssh -p 62901 ctf-player@rhea.picoctf.net Using the password f3b61b38. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!

    Checksum: fba9f49bf22aa7188a155768ab0dfdc1f9b86c47976cd0f7c9003af2e20598f7
    To decrypt the file once you've verified the hash, run ./decrypt.sh files/<file>.


Masalah: sha256 hash

# Langkah
1. copy ssh ke cli yang dihasilkan setelah memulai instances dan masukkan passwordnya
2. setelah mengakses, kita coba dengan ls

![ls](https://github.com/user-attachments/assets/bc20f49e-2fa3-432c-8466-0473c907d2d9)

3. Terdapat 2 file dan satu direktori. Kita bisa melihat isi file tersebut cek dengan **cat**. Coba **cat** pada 

![cat](https://github.com/user-attachments/assets/db3249ac-d1ef-420b-8604-a6241bb7dcec)

4. Isi dari file itu adalah hash sha256. Coba kita lihat isi files dengan ls

![filess](https://github.com/user-attachments/assets/acb4f843-cb60-4ca8-b152-2f4b9220acef)


5. Disini makin jelas kalau kita harus mencari sha256 yang sama seperti di checksum tadi, tapi disini kita tidak mungkin harus mengecek file tersebut satu satu (kalau niat silahkan)

6. cara lebih cepatnya adalah dengan **grep**, **grep** itu seperti baris perintah mencari teks string atau pola. Bisa di gabungkan dengan cat atau ls. Tetapi karena kita sudah mengetahui kalau ini setiap dari file ini adalah sha256, ada terdapat seperti syntax untuk cara yang lebih cepat.

![ketemuu](https://github.com/user-attachments/assets/d4f1f195-a6ec-4269-9b04-30eccde8f1be)


7. kita menemukan kalau file tersebut sama hasilnya checksumnya dengan sha256. Seperti kata yang di deskripsi tadi, kita bisa melakukan ./decrypt.sh <file> untuk melihat teks asli dari hash.

![hasil](https://github.com/user-attachments/assets/7201c44f-f4e0-490d-9e01-98eb2a190962)


