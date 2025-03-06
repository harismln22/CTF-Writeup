picoCTF{5p311ch3ck_15_7h3_w0r57_f578af59}

1. Cobalah untuk berexperiment dengan shellnya seperti coba gunakan apabila memakai (), atau {}, atau syntax exec(), atau eval().
2. tetapi disini ada yang menarik ketika aku menekan ctrl+d

![menarik](https://github.com/user-attachments/assets/897e9bee-6efa-479a-8731-7ced5574ce6e)

kita menemukan kode dari shell ini

3. tapi ls tidak bisa disini

![nope](https://github.com/user-attachments/assets/dee41b70-c976-457a-8525-0a46164c14f9)

4. setelah banyak experiment, ternyata bisa diakali dengan environment variables (https://www.cherryservers.com/blog/how-to-set-list-and-manage-linux-environment-variables)

5. dan ternyata bisa membaca file tersebut dengan cara dibawah ini

![kode](https://github.com/user-attachments/assets/46039df4-7988-49f3-8e45-5afe159cc5f7)

6. karena tidak banyak yang kita bisa lakukan di shell ini, bagaimana kalau kita mencari flag dengan dari terminal python? karena shell tersebut adalah python, kita coba akses compilernya

![akses compiler](https://github.com/user-attachments/assets/f0058383-7baa-42c6-9e3b-4f831ef6f152)


7. ini membuat mencari flag sangat mudah, kita tinggal memakai import os dan syntax os dari python tersebut.

![Screenshot at 2025-03-06 14-46-57](https://github.com/user-attachments/assets/952e81d7-de76-464e-8630-0e0e1d74b3da)



