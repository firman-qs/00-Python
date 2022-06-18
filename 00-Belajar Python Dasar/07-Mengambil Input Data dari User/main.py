
#? Mengambil Input Data dari User

## Data yang diinputkan pasti berupa string
data = input("Masukkan Data:")
print("Data =",data, ",Tipe =", type(data))

## Jika ingin mengambil data berupa integer
dataInt = int(input("Masukkan Data:"))
print("Data =",dataInt, ",Tipe =", type(dataInt))

## Jika ingin mengambil data berupa bool
dataBool = bool(int(input("Masukkan Data:")))
print("Data =",dataBool, ",Tipe =", type(dataBool))

