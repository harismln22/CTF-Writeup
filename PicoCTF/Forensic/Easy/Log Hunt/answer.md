LOG HUNT
Author: Yahaya Meddy

Description

Our server seems to be leaking pieces of a secret flag in its logs. The parts are scattered and sometimes repeated. Can you reconstruct the original flag? Download the logs and figure out the full flag from the fragments.

Langkah
1. Download log tersebut terlebih dahulu
2. gunakan grep untuk mencari string yang akan dicari
3. cat server.log | grep "FLAG"
4. akan terdapat flag bagian yang terpisah, dan urutkan saja sesuai format (picoCTF{kata1_kata2_angka})

# Flag
picoCTF{us3_y0urlinux_sk1lls_cedfa5fb}
