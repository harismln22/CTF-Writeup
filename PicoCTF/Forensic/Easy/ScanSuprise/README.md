# Judul
Scan Suprise

# Deskripsi
Author: Jeffery John
Description
I've gotten bored of handing out flags as text. Wouldn't it be cool if they were an image instead? You can download the challenge files here:

    challenge.zip

The same files are accessible via SSH here: ssh -p 50437 ctf-player@atlas.picoctf.net Using the password 6abf4a82. Accept the fingerprint with yes, and ls once connected to begin. Remember, in a shell, passwords are hidden!

Masalah: Memakai tools

Vurnerability: Scan QR

# Langkah
1. Ada dua cara, yang pertama bisa dengan download file.zip nya atau dengan launch instance
2. Jika sudah, kalian nanti akan menemukan file.png bernama flag dan itu adalah gambar QR
3. Solusinya sangat simpel, kalian bisa buka hp dan memindai atau scan. Atau bisa dengan zbar-tools.
4. cara dengan zbar-tools adalah kalian install terlebih dahulu, lalu ketik zbarimg file.png

![hasil](https://github.com/user-attachments/assets/9885960b-6778-4e84-a929-f49f4fcde95a)
