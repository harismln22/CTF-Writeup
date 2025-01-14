# Judul
Irish-Name-Repo 1

# Deskripsi
Author: Chris Hensler
There is a website running at https://jupiter.challenges.picoctf.org/problem/39720/ (link) or http://jupiter.challenges.picoctf.org:39720. Do you think you can log us in? Try to see if you can login!

masalah: tantangan dalam mencoba login sebagai admin

vurnerability: SQL injection

Langkah yang perlu dilakukan:
1. Masuk ke website yang sudah disediakan oleh link
2. Di awal page hanya terdapat list list dari artis. Tidak banyak yang bisa lakukan tetapi terdapat SideBar

![awal page](https://github.com/user-attachments/assets/a7333195-b896-4b55-ba5c-41a88eddc551)


3. Ketika sidebar tersebut di klik, terdapat tab "Close Menu", "Support", "Admin Login".

![side bar](https://github.com/user-attachments/assets/52282f35-f400-4b01-a0c2-b48e19066d62)


4. Kita sudah menemukan tempat loginnya tetapi karena masih tidak ada informasi mengenai nama adminnya apa, kita coba klik tab "Support"
5. Terdapat petunjuk besar disini dari salah satu komen yang bilang "Hi. I tried adding my favorite Irish person, Conan O'Brien. But I keep getting something called a SQL Error" dengan nama admin yaitu "admin"

![clue](https://github.com/user-attachments/assets/57c81e9a-1cb1-4d6e-8aeb-0d3703a61d26)


6. Jika sudah terdapat informasi error mengenai sql, maka sudah pasti kelemahan tersebut di bagian pada saat login.
7. Kembali dan klik "admin login"
8. terdapat login page username dan password, kita sudah mendapatkan informasi nama adminnya adalah "admin" jadi sekarang kita coba gunakan sql inject yang sederhana menggunakan '--'


9. Ketik admin' -- di bagian username dan isi password tersebut dengan apapun

![bypass](https://github.com/user-attachments/assets/eb981266-0ea2-40bf-82ee-dda7450ffdba)


10. Dan berhasil, selamat mendapatkan flagnya

![hasil](https://github.com/user-attachments/assets/3c332a47-a3ee-40ce-8d69-0e0f4c03fade)


