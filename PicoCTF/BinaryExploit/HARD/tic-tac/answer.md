Author: Junias Bonou

Description

Someone created a program to read text files; we think the program reads files with root privileges but apparently it only accepts to read files that are owned by the user running it.

Skills Gained: TocTou vulnerability


# Langkah Langkah
1. login ke ssh tersebut lalu cek dengan ls

<img width="315" height="46" alt="lss" src="https://github.com/user-attachments/assets/31076c94-59cc-4f3e-9555-a7e01cdb9ffb" />

2. Terdapat binary .txtreader, lalu flag.txt dan src.cpp. Coba cek sourcenya terlebih dahulu (src.cpp)
3. isi dari .cpp ini adalah untuk membaca file sesuai dengan pemiliknya (root atau user biasa. Tapi file flag.txt ini adalah pemilik root).

<img width="763" height="832" alt="SRC cpp" src="https://github.com/user-attachments/assets/d39a08f2-09f8-432f-881e-07fa0eba0ab8" />

4. Isi dari bagian ini yang menarik.

<img width="742" height="365" alt="MENARIK 2" src="https://github.com/user-attachments/assets/8dc96b2b-16cb-4e42-b8e2-5379766aff00" />

5. Karena terdapat kondisi yang dimana jika izin pemilik file tersebut dan user yang sedang di login ssh ini tidak sama (jadi maksudnya bukan sesama root atau bukan sesama user biasa). Maka dia akan menghentikan programnya sebelum menuju ke file.is.open()
6. Yang berarti sudah pasti kalau kita harus menjadi root terlebih dahulu agar bisa membaca flag.txt nya.. tapi, apakah benar?
7. Karena tidak ada penanganan dalam validasi dan penggunaan file dalam secara 'atomik'. Maka vulnerability yang kita dapatkan disini adalah TOCTOU
8. apa itu toctou (Time-of-Check to Time-of-Use)? ketika ada jeda waktu antara saat sebuah sistem memeriksa kondisi suatu sumber daya (seperti keamanan atau keberadaan berkas) dan saat sistem menggunakan hasil pemeriksaan tersebut. Jadi intinya membiarkan si pengguna itu bisa pengecekan dan menggunakan file ketika file tersebut dilakukan pemeriksaan untuk melakukan membaca atau menulis di waktu jeda atau Race Condition.
9. Karena kita menemukan vulnerability nya, yang kita pertama lakukan adalah... melakukan symlink.
10. Gimana caranya? dengan membuat file dahulu
		
		touch test.txt

11. lalu kita bisa membuat symlink bernama tukar

		ln -sf test.txt tukar
		
12. lalu sesudah itu kita buat symlink yang sama, tetapi dari flag.txt
		
		ln -sf flag.txt tukar
		
13. tapi dengan cara ini tidak akan bisa, karena ketika kalian cat tukar, kemungkinannya adalah "you dont own this file" atau membaca dari file test.txt.
14. Cara melakukan ini adalah dengan cara

		while true; do ln -sf test.txt tukar; ln -sf flag.txt tukar; done &
		intinya selama true, maka si file test dan flag akan bertukar-tukar symlink kepada 'tukar' berjalan di background 

15. sesudah itu, jalankan ./txtreader tukar. Tapi karena jalannnya secara pengulangan untuk menukar-nukar dari sebelumnya, jadinya kita akan melakukan pengulangan/loop

		for i in {1..30}; do ./txtreader tukar;done
16. Jalankan. Jika sudah dijalankan tetapi masih belum terlihat flagnya, bisa ubah 30 jadi 50 atau terus jalankan lagi dan lagi.

<img width="678" height="646" alt="flag hasil" src="https://github.com/user-attachments/assets/6746433e-1dcb-4f6b-b149-b60e3fa05eed" />

# Flag
flag: picoCTF{ToctoU_!s_3a5y_2075872e}
