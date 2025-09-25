# Challenge
Need For Speed

Author: Alexander Bushkin

Description

The name of the game is speed. Are you quick enough to solve this problem and keep it above 50 mph? need-for-speed.

# Langkah
1. Install file binary tersebut terlebih dahulu. lalu jalankan ghidra
2. terdapat banyak function pada main, function pada header hanya menunjukkan untuk mengeluarkan output "keep this thing over 50 mph!" dengan iterasi loop. Lalu terdapat set_timer() yang (mungkin) hanya mendelay hanya 1 detik?. Untuk get_key() di dalamnya terdapat fungsi calculate_key(): menghitung berapa kunci, tapi ada yang aneh disini. Kenapa dari menghitung kunci ini ujung ujungnya mengembalikan pada 'return' dengan cara hardcode?. Pada fungsi print_flag() itu terdapat decrypt_flag().
3. Yang kita lakukan ini hanyalah cara analisis statik, bagaimana kalau dinamis? buka gdb
4. Karena kita tahu fungsi fungsi sebelumnya pada ghidra, kita bisa ketik start dan break di main terlebih dahulu
5. Lalu jalankan x/64i $rip untuk mencari alamat print_flag(). Jika ketemu langsung saja break di alamat itu dan klik c agar lanjut.
6. Jika dijalankan x/64i $rip lagi, akan terlihat alamat untuk <flag>. Karena alamat flag sudah terlihat, break di bagian <flag> lalu bisa melakukan x/s <alamat flag>

<img width="1068" height="211" alt="perintah next flag" src="https://github.com/user-attachments/assets/100cc82c-519d-4b0f-aa09-9c808c86a018" />


<img width="840" height="70" alt="FLAG" src="https://github.com/user-attachments/assets/84ca5876-9cec-4275-aa83-9b0bbfd25c32" />

# Flag
PICOCTF{Good job keeping bus #24c43740 speeding along!}
