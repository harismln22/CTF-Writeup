# JUDUL, DESKRIPSI
Author: Darkraicg492
Description
Can you find the flag in this disk image? The right one is Linux! One wrong step and its all gone! Download the disk image here.

Skills gained: Extract dd, Strings

# LANGKAH
1. File tersebut merupakan ekstensi .dd yang dimana bisa dilakukannya mount
2. di deskripsi bertuliskan yang linux, cek dengan fdisk -l <file.dd>. Hasil:
<img width="581" height="278" alt="fdisk -l" src="https://github.com/user-attachments/assets/f615e50c-84f1-47fe-836d-0fcdf3fa120b" />


3. terdapat dua 'os' dalam satu .dd tersebut, tapi fokuskan yang linux.
4. karena ini forensik, kemungkinan besar bisa di cek dengan 'Strings'
5. ya setelah dijalankan dan hasil dari strings tersebut memunculkan banyak sekali flag yang berbeda. Sekarang mana yang asli?
6. tapi ini mungkin karena .dd itu biasanya bersifat raw atau mentah, berarti bagaimana kalau kita coba cek yang biasanya bisa dikatakan versi 'bersihnya'?
7. extract dd tersebut menjadi .img dengan cara:
	dd if=disko-2.dd of=part1.img bs=512 skip=2048 count=51200

9. kita coba lagi dengan Strings, dan hasilnya:
<img width="406" height="238" alt="strings part1" src="https://github.com/user-attachments/assets/ecf24677-5865-426f-950b-c51c4c2a6a9a" />


10. Ya, terdapat dua flag yang dimana hasilnya sama dan versi benarnya. 


flag: picoCTF{4_P4Rt_1t_i5_a93c3ba0}
