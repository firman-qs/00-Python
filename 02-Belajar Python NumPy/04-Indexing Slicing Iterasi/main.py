# autoclear
import os 
os.system('cls')

# import numpy
import numpy as np


a = np.arange(10)**2
b = np.array([[1,2,3,7],[4,5,6,3],[7,8,9,3]])

print(f"a = {a}")
print(f"b = \n{b}")

# mengambil nilai (indexing)
print(f"elemen ke 0 dari a = {a[0]}")
print(f"elemen ke akhir dari a = {a[-1]}")
print(f"elemen ke 7 dari a = {a[7]}")
print(f"elemen ke 2,3,4 dari a = {a[[2,3,4]]}")
# [row, column] --> 2D array
print(f"elemen ke 0,0 dari b = {b[0,0]}")
print(f"elemen ke 1,2 dari b = {b[1,2]}")
print(f"elemen ke 2,2 dari b = {b[2,2]}")

# slicing
# [start:stop:step]
print(f"elemen ke 0-6 dari a = {a[0:6]}")  # [0,6)
print(f"elemen ke 0-6 dari a = {a[0:6:2]}")
print(f"elemen ke 3-ankhir dari a = {a[3:]}")
print(f"elemen ke awal-4 dari a = {a[:5]}")
print(f"elemen ke awal-akhir dari a = {a[:]}")
# Multidimensi --> 
print(f"baris ke-0 b = {b[0][0:]}")
print(f"baris ke-akhir b = {b[-1][0:]}")
print(f"baris ke-akhir b = {b[-1,0:]}") # common use
print(f"kolom tengah dari b = \n{b[:,1:3]}")

# iterasi
for x in b:
    for y in x:
        print("value =",y)