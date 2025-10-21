Riddle Registry

Author: Prince Niyonshuti N.

Description

Hi, intrepid investigator! 📄🔍 You've stumbled upon a peculiar PDF filled with what seems like nothing more than garbled nonsense. But beware! Not everything is as it appears. Amidst the chaos lies a hidden treasure—an elusive flag waiting to be uncovered. Find the PDF file here Hidden Confidential Document and uncover the flag within the metadata.


# Langkah
1. install pdf tersebut
2. Cek pdf tersebut. Terdapat beberapa kata kata yang di sensor, meskipun kita coba kopas dengan klik 2 kali hasilnya bukan mengarah flag
3. kita coba lihat metadatanya dengan exiftool, jalankan exiftool namafile.pdf
4. hasilnya terdapat encode base64 pada author. Copas base64 tersebut lalu convert dengan cyberchef (website) atau dengan cara di terminal: 

		echo "cGljb0NURntwdXp6bDNkX20zdGFkYXRhX2YwdW5kIV9lZTQ1NDk1MH0=" | base64 -d


# Flag
picoCTF{puzzl3d_m3tadata_f0und!_ee454950}
