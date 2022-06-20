data = []
jumlah = 0
while True :
    inputUser = input("masukkan angka : ")
    if (inputUser == 'n') :
        break
    data.append(int(inputUser))

for y in data :
    jumlah += y
print(jumlah)    
