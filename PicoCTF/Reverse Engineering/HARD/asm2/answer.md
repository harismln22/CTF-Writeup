Author: Sanjay C
Description
What does asm2(0x4,0x2d) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source

Skills Gained: more Assembly

1. Download file.S tersebut dahulu 

# Langkah langkahnya

(Cobalah memahami bagaimana flow Assembly dulu)

1. [ebp+0xc] <- argumen kedua (0x2d)
2. [ebp-0x4] <- variabel pertama berisi argumen kedua
3. [ebp+0x8] <- argumen pertama (0x4)
4. [ebp-0x8] <- variabel kedua berisi argumen pertama

5. -0x4 -> berisi argumen kedua
6. -0x8 -> berisi argumen pertama

7. compare argumen pertama <= 0x5fa1
8. hasilnya 0x4 lebih kecil dari 0x5fa1

9. tambah variabel pertama (-0x4) berisi (0x2d) dengan 0x1 (0x2d + 0x1) = 0x2e
10. tambah variabel kedua (-0x8) berisi (0x4) dengan 0xd1 (0x4 + 0xd1) = 0xd5

        hasilnya a masih lebih kecil (0xd5 <= 0x5fa1)

--------------------------------------------------------------------------------
ulang lagi

1. tambah (x2) variabel pertama (-0x4) berisi (0x2e) dengan 0x1 (0x2e + 0x1) = 0x2f
2. tambah (x2) variabel kedua (-0x8) berisi (0xd5) dengan 0xd1 (0xd5 + 0xd1) = 0x1a6

       hasilnya a masih lebih kecil (0x1a6 <= 0x5fa1)

--------------------------------------------------------------------------------
ulang lagi (x3)

1. tambah -0x4 berisi (0x2f) dengan 0x1 = 0x30
2. tambah -0x8 berisi (0x1a6) dengan 0xd1 = 0x277

        hasilnya a masih kecil (0x277 <= 0x5fa1)

anjir lah lama, mending code aja langsung (ke hitung.c)

# Flag
flag: 0xa3
