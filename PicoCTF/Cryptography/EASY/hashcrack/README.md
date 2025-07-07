Author: Nana Ama Atombo-Sackey

Description
A company stored a secret message on a server which got breached due to the admin using weakly hashed passwords. Can you gain access to the secret stored within the server?
Access the server using nc verbal-sleep.picoctf.net 57819

skills gained: John, cracking hash, identifying hash

1. challenge ini kamu ditugaskan untuk meng-cracking semua hash. Ada banyak cara untuk cracking hash tapi aku memakai john
2. masukan semua hash kedalam satu file bernama "hash.txt"
3. tapi kamu harus bisa mengidentifikasi hash dahulu sebelum cracking
4. bisa mengecek hash tersebut dengan dari online yang ada, atau dari hashid github
5. format john:
	john --format=raw-sha256 hash.txt --wordlist=/usr/share/wordlists/rockyou.txt
6. Sebelumnya kalian harus punya file rockyou.txt karena file ini adalah kumpulan dictionary untuk setiap password (jika cracking melalui file)
7. karena deskripsi menyebutkan kalau keamanan password disini lemah, kemungkinan besar mereka memakai hash yang paling umum, md5, sha1, atau sha256
8. untuk cracking, kalian bisa mengubah --format john sesuai dengan hash tersebut. tapi untuk di challenge ini memakai 3 yang umum tadi, raw-md5, raw-sha1, raw-sha256.
9. untuk melihat hasil dari cracking hash, bisa memakai --show <file.txt>

flag: picoCTF{UseStr0nG_h@shEs_&PaSswDs!_869e658e}
