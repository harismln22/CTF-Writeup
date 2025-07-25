Author: Shuailin Pan (LeConjuror)
Description
RED, RED, RED, RED Download the image: red.png

skills gained: zsteg

category: Stegonography

1. install file tersebut dan jika dilihat dari ekstensi file tersebut adalah .png
2. karena ini file berbentuk gambar. Kita bisa mengecek metadata terlebih dahulu dengan exiftool atau strings.

hasil dari strings:


hasil dari metadata:


3. tidak terdapat clue untuk flag, kita coba dengan tools zsteg

hasil dari zsteg:


4. terdapat encode base64, decode tersebut dengan cyberchef atau 
	echo '[encode base64]' | base64 -d

flag: picoCTF{r3d_1s_th3_ult1m4t3_cur3_f0r_54dn355_}

