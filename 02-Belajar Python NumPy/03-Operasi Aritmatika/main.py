import os
import numpy as np

# autoclear
os.system("cls")

# list python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# array NumPy
a_np = np.array([1,2,3,4,5])
b_np = np.array([6,7,8,9,10])

# Operasi NumPy --> ELEMENTWISE
# Penjumlahan
hasil = a + b
hasil = a_np + b_np

# Pengurangan
hasil = a_np - b_np

# Perkalian
hasil = a_np * b_np

# Pembagian
hasil = a_np / b_np

# Kuadrat
hasil = a_np ** 2

# multidimensional array (matriks)
c = np.array([[1,2,3],[4,5,6],[7,8,9]])
d = np.array([[7,-8,9],[-1,2,-3],[4,-5,6]])

hasil = c + d
hasil = c * d
print(hasil)



print('')