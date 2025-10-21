Author: Yahaya Meddy

Description

This file seems broken... or is it? Maybe a couple of bytes could make all the difference. Can you figure out how to bring it back to life? Download the file here.

# Langkah
1. download file pada link tersebut.
2. jika kita mencoba membuka file tersebut, kemungkinan besar tidak akan bisa karena corrupted atau rusak.
3. Cek file tersebut dengan xxd
4. Ternyata yang membuat rusak itu adalah dimana header jpeg itu seharusnya ff d8 dan sementara di file ini bertuliskan 5c 78 (di paling awal)
5. Ubah hex tersebut dengan hexedit
6. Jika sudah, save file tersebut dan buka gambar tersebut dan di dalamnya akan menampilkan flagnya


# Flag
picoCTF{r3st0r1ng_th3_by73s_684e09bc}
