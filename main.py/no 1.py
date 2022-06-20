data = [["319005", "Ayu Ashelia", "Akuntansi"], ["319008", "Wulan Pradnyadewi", "Akuntansi"],
        ["319010", "Ari Purnama", "Akuntansi"]]
x = 0
print("Silahkan Pilih nama mahasiswa berikut : ")
print(f"1. {data[0] [1]}")
print(f"2. {data[1] [1]}")
print(f"3. {data[2] [1]}")
user = int(input("Silahkan pilih mahasiswa berikut : "))

if user == 1:
    print(data[0])
elif user == 2:
    print(data[1])
elif user == 3:
    print(data[2])