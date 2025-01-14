#include <stdio.h>

int main(int argc, char *argv[]) {  // edi dan rsi di assembly menunjukkan argc dan argv
    int rbp4 = 0x9fe1a;  // 654874 dalam desimal
    
    if (rbp4 > 0x2710) {  // 0x2710 adalah 10000 dalam desimal
        rbp4 -= 0x65;  // 0x65 adalah 101 dalam desimal
    } else {
        rbp4 += 0x65;  // Bagian ini ada di assembly tapi tidak akan dieksekusi dalam kasus ini
    }
    
    return rbp4;  // Nilai akhir dikembalikan di eax
}
