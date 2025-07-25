Author: Prince Niyonshuti N.
Description
A digital ghost has breached my defenses, and my sensitive data has been stolen! 😱💻 Your mission is to uncover how this phantom intruder infiltrated my system and retrieve the hidden flag. 
To solve this challenge, you'll need to analyze the provided PCAP file and track down the attack method. 
The attacker has cleverly concealed his moves in well timely manner. Dive into the network traffic, apply the right filters and show off your forensic prowess and unmask the digital intruder! Find the PCAP file here Network Traffic PCAP file and try to get the flag. 

skills gained: Wireshark

1. download file pcap tersebut lalu buka dengan wireshark
2. jika diteliti, terdapat encode base64 pada setiap packet dan packet itu terdapat 22.
3. Tapi sepertinya terdapat false base64? (atau bukan base64), karena base64 itu biasanya diakhiri dengan "==" dan sementara hanya "="
4. tapi untuk harus copy paste bolak balik 22 kali pasti cape, ada terdapat cara pintasnya
5. adalah dengan cara tshark (terminal wireshark)
	tshark -r myNetworkTraffic.pcap -Y 'tcp contains "=="' -T fields -e tcp.payload | xxd -r -p
	-r <file.pcap>: membuka file pcap
	-Y 'tcp contains "==": hanya menampilkan paket TCP yang payloadnya mengandung "=="
	-T fields: hanya menampilkan nilai fields
	-e tcp.payload: menampilkan field payload TCP
	 xxd -r -p: konversi dari hex ke biner (karena tcp.payload berupa hex)

6. Hasil dari command tersebut:
	bnRfdGg0dA==fQ==ZTFmZjA2Mw==XzM0c3lfdA==ezF0X3c0cw==cGljb0NURg==YmhfNHJfMg==

7. jika kalian langsung decode dengan base64 -d atau cyberchef, pasti hasil dari decode ini tidak rapih dan ini karena dari paket sebelumnya yang memang acak
8. agar rapih, harus di copy satu persatu dan untuk hasil urutannya seperti ini
	cGljb0NURg==ezF0X3c0cw==bnRfdGg0dA==XzM0c3lfdA==YmhfNHJfMg==ZTFmZjA2Mw==fQ==

hasil decode: picoCTF{1t_w4snt_th4t_34sy_tbh_4r_2e1ff063} 
