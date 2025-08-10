Author: Jason
Description
Find the pass, get the flag. Check out this file.

Skills gained: Apk Structure

1. Install dulu .apk pada deskripsi challenge
2. lalu buka android studio lalu jalankan emulatornya
3. Pada tampilan kali ini, terdapat kata tidak diperlukan bruteforce untuk mengisi password tersebut
4. Kemungkinan besar, passwordnya terdapat pada .apk
5. install apktools dahulu untuk extrack .apk tersebut lalu jalankan 
	apktool d one.apk
6. Biasanya dalam aplikasi, struktur menyimpan nilai itu terdapat pada folder /value
7. pakailah IDE apapun untuk membuka struktur folder tersebut dan cobalah cari file strings.xml dan cari kata password dengan ctrl+f (kalau memakai vscode)
8. dan hasilnya ada password bernama "opossum"
9. masukkan password tersebut ke tampilan emulator tadi lalu klik tombolnya


flag: PicoCTF{pining.for.the.fjords}
