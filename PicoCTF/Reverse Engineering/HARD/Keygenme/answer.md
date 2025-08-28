Author: LT 'syreal' Jones
Description
Can you get the flag? 
Reverse engineer this binary.

Skills Gained: Deeper assembly, libs_start_main

# Langkah Langkah
1. Install binary tersebut terlebih dahulu lalu jalankan.	


2. seperti password, harus mencari kunci valid. Bagaimana jika dengan strings?


3. terdapat flag tetapi ini kemungkinannya hanya setengahnya saja.
4. Bagaimana dengan ghidra? buka bin tersebut dengan ghidra

5. main program ini dimulai dari fungsi/file __libc_start_main, di dalam fungsi tersebut terdapat fungsi juga

6. ternyata disini yang menjalankan valid lisensi keynya.. tapi untuk dimulai, dia harus membuka file libc_start_main tersebut terlebih dahulu.
7. Dibagian sini terdapat fungsi lagi


8. di fungsi ini terdapat hex flag potongan dari strings sebelumnya..
9. tapi untuk melengkapi bagian flag ini, variabel1 ini harus mempunyai 36 desimal string yang sama agar flag terakhir bisa keluar


10. kita analisis dengan dinamis, pakai gdb lalu jalankan __libc_start_main untuk memulai program ini.


11. Kita mendapat alamat main dari keygenme ini, jalankan dengan breakpoint lalu continue (c). Sesudah itu kita jalankan list intruksi dari main ini


12. sekarang kita masuk ke fungsi yang membuat flagnya dan itu berada di alamat 0x4dd (bisa di cek dalam ghidra yang belakangan 3 nya adalah 4dd). Dan break di isi fungsi call nya 209 lalu c.


13. setelah di dalam fungsi yang membuat flagnya, disini kalian bisa melakukan x/s 22c untuk melihat potongan flag dari hex tersebut.


14. tapi karena disini kita mencari flag terakhirnya, jalankan perintah x/128i $rip terlebih dahulu.



15. break di alamat sebelum if, yaitu alamat 414. Lalu c.
16. disini kita bisa melakukan x/s $rbp-0x30


17. Kenapa ketika membaca register rbp dikurang 0x30 ini bisa memunculkan flag, itu karena rbp itu adalah merujuk ke stack saat ini yang dimana sudah menghasilkan semua hasil flag MD5 disebelumnya (for sebelumnya) lalu setiap iterasi ++ dari local_c0 untuk membandingkan dengan param1 (input user) per karakter. yang berarti disini kalau kita membaca acStack[local_c0] yang berarti kita membaca string (flag) yang sudah dipenuhi dari setiap iterasi untuk dibandingkan (strcmp) dengan input user (param_1)

