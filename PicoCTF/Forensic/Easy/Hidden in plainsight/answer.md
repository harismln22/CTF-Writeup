Hidden in plainsight

Author: Yahaya Meddy

Description

You’re given a seemingly ordinary JPG image. Something is tucked away out of sight inside the file. Your task is to discover the hidden payload and extract the flag. Download the jpg image here.

# Langkah
1. download file.jpg pada link tersebut.
2. karena ini gambar, kita bisa pastikan kemungkinan ini stego
3. Jalankan steghide pada gambar tersebut
	
		steghide extract -sf namaimg.jpg

4. Untuk extract membutuhkan password. Kita coba cek metadata pada gambar tersebut dengan exiftool

		exiftool namaimg.jpg

5. Ternyata terdapat encode base64 pada comment, convert kan dengan cyberchef (website) atau dengan base64 -d

		echo "c3RlZ2hpZGU6Y0VGNmVuZHZjbVE9" | base64 -d

6. Hasilnya adalah "echo "steghide:cEF6endvcmQ=" ini adalah passwordnya, tetapi karena masih dalam base64, decode sekali lagi dengan cara yang sama
7. hasil decode ke dua: pAzzword . Masukkan password tersebut ke steghide extract tadi
8. Setelah di extract, akan terdapat file baru bernama flag.txt. Buka file tersebut

# Flag
picoCTF{h1dd3n_1n_1m4g3_67479645}
