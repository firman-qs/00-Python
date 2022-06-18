# clear before run code
from dataclasses import dataclass
import os
os.system('cls')

#? for loop (perulangan)

""" author: https://github.com/kelasterbuka 

# for kondisi:
# 	aksi

# ini dengan list
angka2_list = [0,2,4,8,10] # ini adalah list
print(angka2_list)

for i in angka2_list:
	print(f"i sekarang -> {i}")

print("akhir dari program 1 \n")

# ini dengan range
angka2_range = range(5)

for i in angka2_range:
	print(f"i sekarang -> {i}")

print("akhir dari program 2 \n")

angka2_range = range(1,10)

for i in angka2_range:
	print(f"i sekarang -> {i}")
	# print("saya keren")

print("akhir dari program 3 \n")

# menggunakan string

data_str = "saya ganteng abiees"

for huruf in data_str:
	print(huruf)

print("akhir dari program 4 \n")

"""
# bilangan2 berkiut kecuali
kecuali = int(input("Masukkan Pengecualian : "))

# set range
r = int(input("Masukkan batas maksimum : "))

# Bilangan prima dengan loop
bar = " Bilangan Prima ".center(36,"~")
print(bar)

for n in range(0, (r+1)):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        if n != kecuali :
            print(n)


# Bilangan genap dengan loop
bar = " Bilangan Genap ".center(36,"~")
print(bar)
for b in range (0, (r+1)):
    if b % 2 == 0 and b != kecuali : 
        print(b)


# Bilangan ganjil dengan loop
bar = " Bilangan Ganjil ".center(36,"~")
print(bar)
for b in range (0, (r+1)):
    if b % 2 != 0 and b != kecuali : 
        print(b)