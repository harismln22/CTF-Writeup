Author: asphyxia

Description

there's crypto in here but the challenge is not crypto... 🤔


# Langkah langkah
1. Install dulu file not-crypto lalu jalankan file tersebut


2. Sepertinya untuk input ini membutuhkan sepanjang sekian.. coba buka dengan ghidra
3. untuk awal fungsi main menggunakan __libc_start_main, coba masuk ke fungsi di dalam tersebut


4. ah ya dari fungsi ini keliatan kalau ini adalah cryptography karena terdapat flag yang dienkripsi.
5. Tapi balik lagi dari clue deskripsinya, katanya challenge ini bukan crypto meskipun menunjukkan adanya algoritma crypto. Jadi kalau kita coba dekrypt ini kemungkinan akan sia sia karena tujuan dari challenge sepertinya bukan ini
6. Jika terus scroll kebawah akan terdapat fungsi menarik. Dimana hasil flag, dan inputan dari user itu dimasukkan ke fungsi MEMCMP untuk hasil perbandingan apakah sesuai atau tidak. Kita bisa menggunakan ini dengan gdb


7. kalian bisa menjalankan gdb dengan start dimulai dari MEMCMP


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


12. Terdapat list banyak register dan cobalah gunakan x/s dari setiap register tapi sesuai dengan note diatas



# Bonus!

7. Jika gdb kalian sudah gef, maka kalian bisa start saja langsung cek hasil rdi di bagian atas

 
