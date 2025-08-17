Author: Sanjay C
Description
What does asm3(0xd2c26416,0xe6cf51f0,0xe54409d5) return? Submit the flag as a hexadecimal value (starting with '0x'). NOTE: Your submission for this question will NOT be in the normal flag format. Source

1. Install file.S tersebut di deskripsi 
2. secara perhitungannya seperti Ini 

# Langkah Langkah
(0xd2c26416,0xe6cf51f0,0xe54409d5)

argument 1 (0xd2c26416)
argument 2 (0xe6cf51f0)
argument 3 (0xe54409d5)

xor eax, eax = 0x00000000
mov ah, byte ptr [ebp+0x9]
		
  	0x00000000 <- 0xd2c26416
	16 [ebp+0x8]
	64 [ebp+0x9]
	c2 [ebp+0xa]
	d2 [ebp+0xb]
	kenapa disini memisahkan nilai ptr? karena fungsi yang dipanggil adalah byte ptr dan bukan dword ptr (yang dimana tidak akan bisa juga karena ah itu 8 bit sedangkan dword itu 32 bit)
	berarti hasilnya 
	0x00006400

shl ax, 0x10
	
 	menggerakkan ke kiri shifting 0x10 atau 16 bit
	00000000 00000000 1000000 00000000
	0000000 00000000 00000000 00000000
	hasilnya 
	0x00000000

sub al, byte ptr [ebp+0xe]
	
 	0x00000000 dikurangi 0xe6cf51f0
	f0 0xc
	51 0xd
	cf 0xe
	e6 0xf
	0x00 dikurangi 0xcf
	hasilnya
	0x00000031
	- kenapa 31? karena di cpu itu tidak ada nilai minus, jadi pada saat -0xcf itu cpu akan melakukan metode komplemen dua yang dimana menjadi
	- 0xcf biner 1100 1111
	- inverskan bit (0 jadi 1 dan 1 jadi 0) tersebut menjadi 0011 0000
	- tambahkan 1 ke hasil: 0011 0000 + 1 = 0011 0001 (0x31)

add ah, byte ptr [ebp+0xf]
	
 	0x0000(00)31 ditambah 0xe6cf51f0
	sementara 0xf adalah e6 tetapi 'ah' syntaxnya, berarti
	0x00 + 0xe6
	hasilnya
	0x0000e631
	
xor ax, word ptr [ebp+0x12]
	
 	0x0000e631 xor 0xe54409d5
	d5 0x10
	09 0x11
	44 0x12
	e5 0x13
	0x0000(e631) xor 0xe544

perhitungan xor:

	1110011000110001 0xe631
	1110010101000100 0xe544
	0000001101110101
	hasilnya
	0x375
	0x00000375

