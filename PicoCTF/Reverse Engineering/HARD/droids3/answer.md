Author: Jason
Description
Find the pass, get the flag. Check out this file.

1. Install apk pada deskripsi tersebut
2. lalu jalankan emulator pada adnroid studio dan install aplikasi tersebut kedalamnya (dengan cara drag)
3. di tampilan tersebut menyatakan kalau "make your app own" yang bisa disimpulkan kalau kita harus mengubah/modifikasi dari file three ini
4. decompile three.apk tersebut dengan cara apktool d three.apk lalu carilah file Flagstaffhill.smali dengan fungsi getflag
5. pada fungsi getflag tersebut terdapat metode didalamnya yang dimana terdapat nope() dan yep(). Caranya ubahlah arus input fungsi dari nope() menjadi yep()
6. jika sudah, save lalu rebuild menjadi apk lagi. Caranya dengan apktool 
	apktool:
	apktool b three.apk -o new_three.apk

7. selanjutnya dengan cara jarsigner
	jarsigner:
	jarsigner -verbose -sigalg SHA1withRSA -digestalg SHA1 keystore ~/.android/debug.keystore three.apk androiddebugkey

	dengan passphrase 'android'
7. lalu selanjutnya optimalisasikan dengan zipalign pada android studio sdk (pergi menuju ke sdk/buildtools dan cari zipalign
	zipalign:
	./zipalign -v 4 new_three.apk aligned.apk

8. sesudah itu masuk ke emulator lagi, jalankan lalu install apk baru tersebut dan langsung saja klik tombolnya

flag: PicoCTF{tis.but.a.scratch}
