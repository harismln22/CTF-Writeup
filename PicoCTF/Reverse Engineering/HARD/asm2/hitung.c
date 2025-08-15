#include <stdio.h>

int main(){ 	
	//int a = 0x2592;
	int a = 0x2d;	// variabel pertama berisi argumen kedua (ptr [ebp-0x4], ptr [ebp+0xc]) 
	int b = 0x4;	// variabel kedua berisi argumen pertama (ptr [ebp-0x8], ptr [ebp+0x8]

	/* +0xc itu artinya dia di deklarasikan sebelum dari angka 0x10 yang artinya dia adalah argumen kedua */
	/* +0x8 di deklarasikan sebelum 0xc yang artinya dia adalah argumen pertama */
	
	int c = 0x1;	// add untuk (a atau variabel pertama yang berisi argumen kedua) 
	int d = 0xd1;	// add untuk (b atau variabel kedua yang berisi argumen pertama)

	while(b <= 0x5fa1)
	{
		a += c;
		b += d;
	}

	printf("%x\n", a);
	printf("%x\n", b);

	return 0;
}
