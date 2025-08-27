No way out
Author: Kris
Description
Put this flag in standard picoCTF format before submitting. If the flag was h1_1m_7h3_f14g submit picoCTF{h1_1m_7h3_f14g} to the platform. Windows game, Mac game Use password picoctf to unzip archives.

# Langkah Langkah
1. install file di link tersebut
2. terdapat file seperti unity player.. berarti engine game nya udah pasti unity
3. Karena ini unity, install dnSpy dahulu untuk membuka kode dari game ini.

		https://github.com/dnSpy/dnSpy

4. Cobalah mainkan game dulu tersebut.
5. Untuk mendapatkan flag, katanya kita bisa harus keluar dari tempat ini, tetapi meskipun kita udah ke atas tangga tetap saja tidak bisa karena terdapat dinding penghalang.. yang berarti antara kita harus menghapus dinding tersebut, atau membuat karakter kita menembus atau lompat tinggi.
6. Saatnya membuka dnSpy lalu bukalah file file di dalam pico_data. Biasanya di folder ini yang menyimpan semua dari game tersebut (untuk engine unity)
7. di dalam pico_data terdapat level0. Ini biasanya layer awal atau scene pertama awal permainan. Cobalah cek dengan strings
8. hasilnya ada file dari model-model yang dipakai, tapi lihat ke paling akhir.

<img width="489" height="374" alt="strings level0" src="https://github.com/user-attachments/assets/4e40e022-0764-4014-9136-8b5af5774e66" />

9. Terdapat kata "escape" ketika kita masuk awal game tersebut, dan juga terdapat kata welcome to unity.. sepertinya ini hanya template kode awal ketika membuka unity
10. sekarang kita masuk ke folder managed dan buka dnSpy.
11. karena kita disini membutuhkan antara membuat dinding penghalang tersebut menghilang atau karakter kita diperkuat.. mungkin kita coba dengan memperkuat karakter kita yaitu loncatnya terlebih dahulu agar kita tau apakah tembok ini menuju sampai keatas? dan jika ini iya kita perlu menghapus tembok penghalang tersebut
12. untuk sekarang cobalah cari file yang mengontrol pergerakan player, dan tepatnya pada di file Assembly-CSharp.dll 
13. sekarang kita coba cari kode/variabel mana yang membuat player ini loncat atau bergeraknya. Biasanya dalam game penamaan loncat itu adalah antara jump atau gravity.
14. Tapi.. biasanya yang membuat karakter itu terbatas (dalam hal lompat) dimana ada terdapat variabel true/false yang biasanya isGrounded atau Ground.
15. disini kita menemukan if player loncat DAN player bergerak DAN berada di tanah DAN tidak sedang di tangga, maka pergerakan atas bawah akan diatur oleh jumpspeednya.

<img width="974" height="604" alt="AWAL KETEMU GROUNDED" src="https://github.com/user-attachments/assets/701c07d6-b0ac-4cdc-bd8a-232b2dda73f1" />

16. dari sini kita bisa menghapus isGrounded, karena if tersebut menunjukkan kalau loncat tersebut tidak bisa berkali kali dan hanya bisa sekali kalau pada saat si karakternya di tanah doang.

<img width="466" height="123" alt="FIX HAPUS GROUND" src="https://github.com/user-attachments/assets/059e298b-bd58-4d1f-b2e9-4ff48063b342" />


17. Hapus isGrounded tersebut, lalu klik file, save module dan ok. Lalu buka lagi gamenya dan cobalah loncat terus terus hingga ke flag putih tersebut.

<img width="1679" height="736" alt="HASIL" src="https://github.com/user-attachments/assets/622eccda-02f9-4834-927e-556af6880019" />


# Flag
flag: picoCTF{WELCOME_TO_UNITY!!}
