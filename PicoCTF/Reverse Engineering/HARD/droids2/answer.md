Author: Jason
Description
Find the pass, get the flag. Check out this file.

Skills gained: smali structure

1. install apk tersebut pada di deskripsi
2. lalu buka android studio dan jalankan simulatornya
3. kali ini menyatakan "smali ikea book" yang berarti kita harus extract zip ini
4. extract menggunakan apktool d two.apk
5. Masuk ke folder smali dan cari file FlagsraffHill.smali
6. Ternyata password-password tersebut dimasuki secara acak dan juga terdapat perhitungannya pada fungsi getflag


# Langkah perhitungannya
1. Membuat array
    const/4 v0, 0x6 → v0 = 6

    new-array v0, v0, [Ljava/lang/String; → v0 = reference ke array witches (panjang 6)

2. Mengisi witches (index → value)

    witches[0] = "weatherwax"

    witches[1] = "ogg"

    witches[2] = "garlick"

    witches[3] = "nitt"

    witches[4] = "aching"

    witches[5] = "dismass"

    catatan: Smali menggunakan aput-object v2, v0, v1 → simpan v2 ke array v0 pada index v1.

3. Menetapkan first dll. (register arithmetic)

    const/4 v1, 0x3 → v1 = 3 (kita panggil ini first)

    sub-int v2, v1, v1 → v2 = 3 - 3 = 0 (second)

    div-int v3, v1, v1 → v3 = 3 / 3 = 1
    add-int/2addr v3, v2 → v3 = v3 + v2 = 1 + 0 = 1 (third)

    add-int v4, v3, v3 → v4 = 1 + 1 = 2
    sub-int/2addr v4, v2 → v4 = 2 - 0 = 2 (fourth)

    add-int v5, v1, v4 → v5 = 3 + 2 = 5 (fifth)

    add-int v6, v5, v2 → v6 = 5 + 0 = 5
    sub-int/2addr v6, v3 → v6 = 5 - 1 = 4 (sixth) 

	jadi finalnya: 
	v1=3, v2=0, v3=1, v4=2, v5=5, v6=4

4. Ambil elemen array (indexing) — per aget-object

    aget-object v7, v0, v5 → ambil witches[v5] = witches[5] = "dismass" → v7 = "dismass"
    kemudian diikuti rangkaian concat:

        start: const-string v8, "" ; v8.concat(v7) → hasil "dismass" disimpan ke v7

        v7.concat(".") → "dismass."

        v7.concat( witches[v3] ) → witches[v3] = witches[1] = "ogg" → "dismass.ogg"

        v7.concat(".") → "dismass.ogg."

        v7.concat( witches[v2] ) → witches[v2] = witches[0] = "weatherwax" → "dismass.ogg.weatherwax"

        v7.concat(".") → "dismass.ogg.weatherwax."

        v7.concat( witches[v6] ) → witches[4] = "aching" → "dismass.ogg.weatherwax.aching"

        v7.concat(".") → "dismass.ogg.weatherwax.aching."

        v7.concat( witches[v1] ) → witches[3] = "nitt" → "dismass.ogg.weatherwax.aching.nitt"

        v7.concat(".") → "dismass.ogg.weatherwax.aching.nitt."

        v7.concat( witches[v4] ) → witches[2] = "garlick" → final "dismass.ogg.weatherwax.aching.nitt.garlick"

# Detail contoh
const/4 v1, 0x0                # v1 = 0 (indeks 0)
const-string v2, "weatherwax"  # v2 = "weatherwax"
aput-object v2, v0, v1         # witches[ v1 ] = v2

v0 → referensi array witches
v1 → indeks (di sini 0)
v2 → nilai string yang mau disimpan ("weatherwax")
aput-object artinya: masukkan object v2 ke array v0 di indeks v1

jadi hasilnya:
witches[0] = "weatherwax"


# Hasil password
dismass.ogg.weatherwax.aching.nitt.garlick


# Flag
flag: PicoCTF{what.is.your.favourite.colour}
