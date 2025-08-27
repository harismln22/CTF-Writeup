# Title, description, difficulty.
<img width="583" height="639" alt="Screenshot at 2025-08-25 06-54-08" src="https://github.com/user-attachments/assets/4ffd76ea-8c3b-4bbb-8008-b0d141f20c36" />

GIFT

Diff: Easy


# Langkah
1. Install vm tersebut pada virtualbox, lalu jalankan 
2. kita coba cek  vm tersebut dengan nmap

    <img width="796" height="360" alt="nmap" src="https://github.com/user-attachments/assets/05f935c1-284c-4db1-b709-49bbe2ab253c" />

    
3. Terdapat dua port yang terbuka, cek dari websitenya terlebih dahulu

    <img width="1654" height="912" alt="isi web" src="https://github.com/user-attachments/assets/b9756966-5477-4c90-94c1-1ee22d5e975d" />


4. katanya "simple", untuk sshnya pasti membutuhkan kredensial. Kita cek website tersebut dengan gobuster 

<img width="851" height="422" alt="gobuster common" src="https://github.com/user-attachments/assets/8f894566-9ac7-49d9-8b23-24dc34ea500d" />


5. Hanya index.html saja yang ditemukan, bagaimana kalau kita pakai wordlist yang lebih besar?

<img width="1063" height="420" alt="gobuster2" src="https://github.com/user-attachments/assets/b83b23bb-e2bd-4367-b1b0-e8202d315481" />


6. tidak ada hasil? coba dengan nikto 
    
<img width="1919" height="356" alt="nikto" src="https://github.com/user-attachments/assets/e908b0b8-3fdb-40a7-a4b5-10b2b2422411" />

        
7. bahkan nikto tidak mendapatkan apapun, tapi balik lagi. Dari clue yang kita dapatkan di website ini adalah "Dont overthink. Really, Its simple"
8. Apakah maksud dari clue itu adalah "simple" sebagai password? sudahlah, kita coba aja bruteforce pakai hydra untuk ssh nya 

<img width="1919" height="326" alt="hydra" src="https://github.com/user-attachments/assets/f32334d9-72c9-4c0b-8c0c-19dabda4ae4e" />


9. ternyata benar saja wkwk, ya sudahlah. Masukkan username sebagai root dan passwordnya juga di ssh

<img width="338" height="228" alt="SSH" src="https://github.com/user-attachments/assets/752e0318-cfca-494b-bc54-c2313b458899" />


# Flag  
-user:
HMV665sXzDS

-root:
HMVtyr543FG
