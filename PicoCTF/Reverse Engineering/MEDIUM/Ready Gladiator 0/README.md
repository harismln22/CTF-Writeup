picoCTF{h3r0_t0_z3r0_4m1r1gh7_f1e207c4}

Requirement: assembly language or coreWars, (or low-level operations)
gain: syntax assembly knowledge

1. Cobalah mengutak-atik movnya
2. ubah mov yang kita menjadi 2, 3


# why?
Dalam CoreWars, tujuan permainan adalah untuk mengalahkan lawan dengan menimpa 
instruksinya di memori hingga lawan tidak dapat berjalan lagi. 

Jika kalian familiar dengan assembly, kalian pasti akan mengenali dengan namanya mov.
Apa itu mov? mov itu menggerakkan suatu nilai dalam alamat. 
Tetapi ada perbedaan bahasa coreWars(codered) dengan assembly.
- kalau redcode itu memorinya berbentuk sirkular sedangkan assembly berbentuk linear.
- redcode menyalin instruksi dari alamat A ke alamat B sedangkan assembly menyalin data dari register/memory ke register/memory lainnya
- redcode tidak memiliki register sementara assembly terdapat register AX,BX, dll.
secara singkat, coreWarsnya hanya menyalin instruksi sedangkan assembly menyalin data.

misalkan terdapat [...][A][B][C][D][...]
mov 0, 1
Langkah 1:
	sumber = 0 -> ambil data dari A (posisi saat ini adalah + 0 offset = A
	tujuan = 1 -> salin data ke B (posisi sekarang adalah + 1 offset = A+1) 

Langkah 2:
	Saat di B, instruksi yang baru saja di salin akan dieksekusi
	Proses ini diulang hingga akhir
yang artinya, si imp itu terus menyalin dirinya sendiri ke sel memori berikutnya, bergerak maju seperti kelabang.

lalu kenapa dengan mov 2, 3?
mov 2, 3
karena tidak mereplica atau menyimpan alamat sebelum/sesudah pindah. Dan yang membuat bisa menetap di suatu alamat adalah 0

tapi bagaimana jika mov 0,2? (kita bisa mendapatkan flag dengan cara ini juga)
tetap saja akan gagal, karena jika kita balik lagi menggunakan analogi
[A][B][C][D][...]
mov tersebut memang melewati dua langkah sekaligus dan menetap setelah pergerakan (2 langkah terlewat), tetapi tetap saja gagal karena dia langsung melewati [B] (karena langsung loncat ke [C]). CPU tidak akan berjalan jika ada alamat yang terlewati dan yang berakhir dead.
