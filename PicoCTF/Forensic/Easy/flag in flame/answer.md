Flag in Flame

Author: Prince Niyonshuti N.

Description

The SOC team discovered a suspiciously large log file after a recent breach. When they opened it, they found an enormous block of encoded text instead of typical logs. Could there be something hidden within? Your mission is to inspect the resulting file and reveal the real purpose of it. The team is relying on your skills to uncover any concealed information within this unusual log. Download the encoded data here: Logs Data. Be prepared—the file is large, and examining it thoroughly is crucial .

# Langkah
1. download logs data pada link tersebut
2. cobalah buka file logs tersebut dengan cat. Hasilnya adalah penuh dengan base64
3. decode base64 tersebut dengan cara:

		base64 -d logs.txt >> namabebas.png

4. setelah berhasil diubah menjadi gambar, buka file tersebut. Hasilnya adalah terdapat hex di gambar tersebut.
5. Untuk mendapatkan hex tersebut, gunakan tesseract dan jalankan:
		
		tesseract namabebas.png output.txt

6. Buka output.txt tersebut, copy hex nya lalu convertkan dengan cyberchef (website) atau dengan terminal
	
		echo "7069636F4354467B666F72656E736963735F616E616C797369735F69735F616D617A696E675F61633165333538347D" | xxd -r -p

# Flag
picoCTF{forensics_analysis_is_amazing_ac1e3584}
