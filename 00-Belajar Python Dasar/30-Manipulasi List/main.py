
# Manipulasi List

'''daftar isi
1. indexing list
2. mengambil data dari list menggunakan index
3. mengambil info jumlah data dari list
4. manipulasi data list 
    - menambahkan item pada list di posisi tertentu
    - menambahkan item pada list di posisi akhir
    - menambahkan list pada list
    - merubah data list
    - me-remove data list
    - me-remove data pada posisi tertentu
    - me-remove data paling belakang
'''

# 1. indexing List
# index ==>  [0] or [-3]  [1] or [-2]     [2] or [-1]
data =      ["Alchemist","Bloodseeker","Nature Prophet"]
print(data)

# 2. Mengambil data berdasarkan index
dataAlche = data[0]
print(f"data ke 0 \t\t= {dataAlche}")

dataBs = data[-2]
print(f"data ke -2 \t\t= {dataBs}")

# 3. mengambil info jumlah data pada list
jumlah = len(data)
print(f"jumlah data dalam list \t= {jumlah}")

# 4. Manipulasi data list
## menambahkan item pada list di posisi tertentu
data.insert(-1, "Anti Mage") # menambahkan data "Anti mage" pada posisi/index ke -1 (tidak menjadi paling akhir)
print(f"data sekarang = {data}")

## menambahkan item pada list di posisi terakhir
data.append("Invoker")
print(f"data sekarang = {data}")

## menambahkan list pada list
data2 = ["Radiance","Mjolnir","Tango"]
data.extend(data2)
print(f"data sekarang = {data}")
### cara lain
# data += data2
# print(f"data sekarang2 = {data}")

## merubah data
data[-1] = "Healing Selve" # merubah tango ke healing selve
print(f"data sekarang = {data}")

## merubah data pada range
dataz = ["satu","dua","tiga","empat","lima"]
dataz[:2] = ["one","two"]
print(dataz)

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)

## me-remove data
data.remove("Healing Selve")
print(f"data remove = {data}")

## me-remove data pada posisi tertentu
data.remove(data[2])
print(f"data remove[i] = {data}")

## me-remove beberapa data dengan for range
for i in range(2): # sebanyak 2 data dari data ke (dibawah)
    data.remove(data[2]) # mulai dari data ke-2 (Nature Prophet)
print(f"data sekarang = {data}")

## me-remove data paling akhir
data = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
data.pop() # pop remove specified index, pop(1) remove item in index-1
print(f"data akhir = {data}")

data.pop(2) # pop remove specified index, pop(1) remove item in index-1
print(f"data akhir = {data}")

for i in range(0,2):
    data.pop(i)
print(f"data akhir = {data}")

# remove data menggunakan del
thislist =  ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
del thislist[0:2]
print(thislist)

del thislist[2:4]
print(thislist)