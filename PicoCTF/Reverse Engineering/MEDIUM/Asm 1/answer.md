Author: Sanjay C
Description
What does asm1(0x6fa) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source

skills gained: Assembly


1. download dulu file Assembly tersebut
2. buka file tersebut dengan file editor
3. di deskripsi menyebutkan kalau apa hasil dari 0x6fa, dan hex itu terdapat pada +37

begini cara perhitungannya

# Langkah perhitungannya
1. dimulai dari cmp nilai ptr ebp dengan 0x3a2
2. jika ptr tersebut lebih besar dari pada 0x3a2, maka lompat ke +37
3. tapi jika tidak, maka akan dibandingkan lagi dengan 0x358
4. dan jika mereka mempunyai nilai tidak sama (equal) maka akan loncat ke +29
5. tapi jika sama maka ptr tersebut masuk ke register eax, lalu menambahkan eax dengan 0x12
6. jika lanjut lagi maka akan lompat ke +60 dan alamat itu adalah dimana kalau kode tersebut langsung selesai (tapi dibagian alur kode ini tidak ada hubungan dengan 0x6fa)
7. jadi yang pasti di salah satu perbandingan ini yang berhubungan dengan alurnya dan itu adalah yang lompat ke +37.
8. Kenapa yang lompat +37 atau bagian barisan +3. Karena jika kita mencoba mengikuti alur yang lompat +29 itu sama berakhir ke +60 (yang dimana tidak hubungannya dengan 0x6fa)
9. Sekarang di +37 dan membuat perbandingan lagi antara ptr dengan 0x6fa
10. jika hasilnya keduanya tidak sama, maka akan memasukkan ptr ke eax
11. lalu menambahkan hasil eax dengan 0x12

Sekarang pertanyaannya
bagaimana kita tau hasil dari dword ptr [ebp+0x8]? jawabannya adalah sudah ada dari deskripsi (0x6fa) karena disini kita bukan mencari nilai dari ptr ini tapi mengikuti/membaca alur dari input hingga return

# Hasil 
karena kita sudah tau isi dari ptr tersebut, jadinya tinggal mengikuti alurnya
sebagai contoh di awal cmp 0x6fa > 0x3a2 maka dia termasuk ke jump if great dan loncat ke +37 (dan hasil ptr tersebut selalu 0x6fa)

# Tips
jg (jump if greater): Lompat jika A > B

jge (jump if greater or equal): Lompat jika A >= B

jl (jump if less): Lompat jika A < B

jle (jump if less or equal): Lompat jika A <= B

je (jump if equal): Lompat jika A == B

jne (jump if not equal): Lompat jika A != B

add : penambahan A dan B

sub : pengurangan A dan B

# Flag
flag: 0x6e8
