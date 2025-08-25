# Title, description, difficulty.
GIFT

Diff: Easy


# Langkah
1. Install vm tersebut pada virtualbox, lalu jalankan 
2. kita coba cek  vm tersebut dengan nmap
    
        ![Nmap hasil](/home/Pictures/GIFT/nmap.png)

3. Terdapat dua port yang terbuka, cek dari websitenya terlebih dahulu

        ![website hasil](/home/Pictures/GIFT/isi\ web.png)

4. katanya "simple", untuk sshnya pasti membutuhkan kredensial. Kita cek website tersebut dengan gobuster 

        ![gobuster hasil](/home/Pictures/GIFT/gobuster\ common.png)

5. Hanya index.html saja yang ditemukan, bagaimana kalau kita pakai wordlist yang lebih besar?

        ![gobsuter 2 hasil](/home/Pictures/GIFT/gobuster2.png)

6. hasilnya sama aja? coba dengan nikto 
    
        ![Nikto hasil](/home/Pictures/GIFT/nikto.png)
        
7. bahkan nikto tidak mendapatkan apapun, tapi balik lagi. Dari clue yang kita dapatkan di website ini adalah "Dont overthink. Really, Its simple"
8. Apakah maksud dari clue itu adalah "simple" sebagai password? sudahlah, kita coba aja bruteforce pakai hydra untuk ssh nya 

        ![Nmap hasil](/home/Pictures/GIFT/hydra.png)

9. ternyata benar saja wkwk, ya sudahlah. Masukkan username sebagai root dan passwordnya juga di ssh

        ![Nmap hasil](/home/Pictures/GIFT/SSH.png)

# Flag  
-user:
HMV665sXzDS

-root:
HMVtyr543FG
