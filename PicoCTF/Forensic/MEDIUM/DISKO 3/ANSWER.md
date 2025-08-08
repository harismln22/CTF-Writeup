Author: Darkraicg492
Description
Can you find the flag in this disk image? This time, its not as plain as you think it is! 
Download the disk image here.

Skills gained: Mounting image.dd

1. Download image dulu di deskripsinya
2. Extract .gz tersebut dengan gunzip
3. Mount file tersebut dengan cara
	mount -o loop,ro <image.dd> /mnt/
4. cd ke tempat mount tersebut, lalu cobalah 'ls' dan cari zip bernama flag.gz
5. gunzip flag tersebut lalu baca filenya 


flag: picoCTF{n3v3r_z1p_2_h1d3_654235e0}
