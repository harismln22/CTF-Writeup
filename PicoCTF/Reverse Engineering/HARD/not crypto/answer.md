Author: asphyxia

Description

there's crypto in here but the challenge is not crypto... 🤔

Skills gained: deeper assembly checking function


# Langkah langkah
1. Install dulu file not-crypto lalu jalankan file tersebut

<img width="576" height="133" alt="(1) input awal panjang string" src="https://github.com/user-attachments/assets/49fcf4fe-7cf3-48d1-b057-937d61a2ea18" />

2. Sepertinya untuk input ini membutuhkan sepanjang sekian.. coba buka dengan ghidra
3. untuk awal fungsi main menggunakan __libc_start_main, coba masuk ke fungsi di dalam tersebut

<img width="1199" height="532" alt="(2) awal main fungsi" src="https://github.com/user-attachments/assets/8b3ba3be-5cb5-4b19-b8b0-27f55bc4753f" />

4. ah ya dari fungsi ini keliatan kalau ini adalah cryptography karena terdapat flag yang dienkripsi.

<img width="1064" height="695" alt="(3)isi dalam fungsi " src="https://github.com/user-attachments/assets/522b8c3a-9de7-49d9-aaf2-57a6c58980cd" />

5. Tapi balik lagi dari clue deskripsinya, katanya challenge ini bukan crypto meskipun menunjukkan adanya algoritma crypto. Jadi kalau kita coba dekrypt ini kemungkinan akan sia sia karena tujuan dari challenge sepertinya bukan ini
6. Jika terus scroll kebawah akan terdapat fungsi menarik. Dimana hasil flag, dan inputan dari user itu dimasukkan ke fungsi MEMCMP untuk hasil perbandingan apakah sesuai atau tidak. Kita bisa menggunakan ini dengan gdb

<img width="315" height="121" alt="(5) memcmp awal" src="https://github.com/user-attachments/assets/f25a5db9-c781-468b-b675-e1c64f800205" />

7. kalian bisa menjalankan gdb dengan start dimulai dari MEMCMP

<img width="1662" height="222" alt="(6) dalam gdb main" src="https://github.com/user-attachments/assets/d4927df6-acbe-4354-ae51-26a3c5fdcf17" />

8. Jika kalian lihat kembali ke ghidra, variabel flag itu adalah parameter pertama dalam memcmp itu. jadi, biasanya register untuk parameter pertama itu bernama $rdi

		note:
		$rdi: Argumen pertama.
		$rsi: Argumen kedua.
		$rdx: Argumen ketiga.
		$rcx: Argumen keempat.
		$r8: Argumen kelima.
		$r9: Argumen keenam.

9. sekarang kenapa bisa tahu kalau parameter pertama itu adalah isi dari string flag? itu karena kita dari pada harus cek memori keseluruhan secara satu satu, sebaiknya kita langsung cek saja hasil cmp antara inputan user yang dimaan kita tau kalau hasilnya iya atau tidak, dan biasanya inputan user ini selalu dibandingkan dengan string flag.
10. Karena memcmp juga cara penggunaanya itu adalah 

		memcmp(local_88 <- (ini biasanya isi variabel string) ,local_198 <- (ini input user), 0x40 <- (cek string yang dibandingkan sama panjangnya));

11. Jika kalian sudah di gdb dan run memcmp@plt, maka kalian bisa cek dengan 'info registers'

<img width="637" height="504" alt="(7) info registers" src="https://github.com/user-attachments/assets/c26d31b7-f7e3-40e2-aed4-e8b58c856434" />

12. Terdapat list banyak register dan cobalah gunakan x/s dari setiap register tapi sesuai dengan note diatas

<img width="1667" height="63" alt="(8) hasil rsi input user" src="https://github.com/user-attachments/assets/89399abf-c368-40cc-98bb-bfb2283b6ee5" />

<img width="842" height="43" alt="(9)hasil flag" src="https://github.com/user-attachments/assets/f44de2c4-babd-4e78-9c1f-1926e6e2f2be" />


# Bonus!

7. Jika gdb kalian sudah gef, maka kalian bisa start saja langsung cek hasil rdi di bagian atas agar langsung melihat flagnya
 
<img width="1096" height="719" alt="(10) hasil flag gef" src="https://github.com/user-attachments/assets/867381eb-cf8c-4909-b3b9-edabcb482088" />
