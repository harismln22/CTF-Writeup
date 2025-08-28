Author: LT 'syreal' Jones

Description
Can you get the flag? 

Reverse engineer this binary.

Skills Gained: Deeper assembly, libs_start_main

# Langkah Langkah
1. Install binary tersebut terlebih dahulu lalu jalankan.	

<img width="353" height="84" alt="awal run" src="https://github.com/user-attachments/assets/54ae58ff-afdb-41d9-a8af-ce05a81e6ed7" />

2. seperti password, harus mencari kunci valid. Bagaimana jika dengan strings?

<img width="473" height="452" alt="awal flag" src="https://github.com/user-attachments/assets/1cf4c504-8c51-4d80-8cce-195fc5ad642f" />


3. terdapat flag tetapi ini kemungkinannya hanya setengahnya saja.
4. Bagaimana dengan ghidra? buka bin tersebut dengan ghidra

<img width="1245" height="533" alt="awal main" src="https://github.com/user-attachments/assets/a2e16dbb-fb48-4cfa-976f-7c45941e064e" />

5. main program ini dimulai dari fungsi/file __libc_start_main, di dalam fungsi tersebut terdapat fungsi juga
6. ternyata disini yang menjalankan valid lisensi keynya.. tapi untuk dimulai, dia harus membuka file libc_start_main tersebut terlebih dahulu.

<img width="953" height="552" alt="awal fungsi" src="https://github.com/user-attachments/assets/5dbcd152-20a0-42b3-9cec-08a40fc86acc" />


7. Dibagian sini terdapat fungsi lagi
8. di fungsi ini terdapat hex flag potongan dari strings sebelumnya..

<img width="1017" height="732" alt="fungsi dalam" src="https://github.com/user-attachments/assets/659335d1-e6d5-4a82-a617-148f9afb541d" />


9. tapi untuk melengkapi bagian flag ini, variabel1 ini harus mempunyai 36 desimal string yang sama agar flag terakhir bisa keluar

<img width="506" height="259" alt="desimal 36" src="https://github.com/user-attachments/assets/382c5008-aa29-4335-b35f-ccf72811b048" />


10. kita analisis dengan dinamis, pakai gdb lalu jalankan __libc_start_main untuk memulai program ini.

<img width="1307" height="274" alt="awal gdb" src="https://github.com/user-attachments/assets/d2d9be0b-e416-41c5-8002-031d7815cd2d" />

11. Kita mendapat alamat main dari keygenme ini, jalankan dengan breakpoint lalu continue (c). Sesudah itu kita jalankan list intruksi dari main ini

<img width="527" height="145" alt="awal c" src="https://github.com/user-attachments/assets/bd187938-d967-426a-b43e-62d35ebe498e" />

<img width="812" height="811" alt="awal instruksi" src="https://github.com/user-attachments/assets/49842b3b-02de-455e-b2f6-76a640371e33" />


12. sekarang kita masuk ke fungsi yang membuat flagnya dan itu berada di alamat 0x4dd (bisa di cek dalam ghidra yang belakangan 3 nya adalah 4dd). Dan break di isi fungsi call nya 209 lalu c.

<img width="556" height="145" alt="209" src="https://github.com/user-attachments/assets/58aed030-c949-48e5-ab44-5476dcde97ca" />

13. setelah di dalam fungsi yang membuat flagnya, disini kalian bisa melakukan x/s 22c untuk melihat potongan flag dari hex tersebut.

<img width="1311" height="39" alt="awal flagg" src="https://github.com/user-attachments/assets/fbbe3608-c6ba-478b-9b39-605dab532784" />


14. tapi karena disini kita mencari flag terakhirnya, jalankan perintah x/128i $rip terlebih dahulu.

<img width="578" height="104" alt="414" src="https://github.com/user-attachments/assets/0e481ddb-327d-4b38-86e5-3d32cbcd8353" />

15. break di alamat sebelum if, yaitu alamat 414. Lalu c.

<img width="363" height="99" alt="4144" src="https://github.com/user-attachments/assets/6ab04bf7-d4d7-4091-a6f0-8ce733ac64ee" />

16. disini kita bisa melakukan x/s $rbp-0x30

<img width="655" height="76" alt="hasil flag" src="https://github.com/user-attachments/assets/94d88d15-7bca-439d-b9b2-8b548804fa11" />

17. Kenapa ketika membaca register rbp dikurang 0x30 ini bisa memunculkan flag, itu karena rbp itu adalah merujuk ke stack saat ini yang dimana sudah menghasilkan semua hasil flag MD5 disebelumnya (for sebelumnya), lalu setiap iterasi ++ dari local_c0 untuk membandingkan dengan param1 (input user) per karakter. Yang berarti disini kalau kita break di bagian acStack, kita akan membaca acStack[local_c0] yang sudah ter iterasi penuh (atau string flag penuh), yang berarti kita membaca string (flag) yang sudah dipenuhi dari setiap iterasi untuk dibandingkan (strcmp) dengan input user (param_1)

        disini jika kita coba akses dari -0x10 sampai 0x30. Kita bisa lihat kalau kita mendapatkan string flag karakter per karakter karena loop iterasi 

    <img width="634" height="489" alt="langkah flag" src="https://github.com/user-attachments/assets/114951ff-6aa3-4ee0-b4cd-1d7b7043b99d" />

