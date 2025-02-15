f = open('encrypted.txt')

text = f.read()
print(text)


hasil = ""
for i in range(len(text)):
    kata = text[i]


    if(kata.isupper()):
        hasil += chr((ord(kata) - 8-65) % 26 + 65)

    elif(kata.islower()):
        hasil += chr((ord(kata) - 8-97) % 26 + 97)
    
    else:
        hasil += kata

print(hasil) 

f.close()