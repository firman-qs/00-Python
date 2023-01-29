import numpy as np
import os
os.system('cls')

# membuat matriks dengan type data tertentu
a = np.array([[1, 2, 3],
              [4, 5, 0]], dtype=float)

# membuat array dengan menggunakan function
def kuadrat(row, height):
    return height**2

b = np.fromfunction(kuadrat, (1, 10), dtype=int)


def tambah(kolom, baris):
    return kolom + baris

c = np.fromfunction(tambah, (2, 3), dtype=int)

# membuat array dengan interasi
iterasi = [x*x for x in range(10)]
d = np.fromiter(iterasi, dtype=int)

# multitype array
tipedata = [('nama', 'S20'), ('tinggi', float)]
data = [
    ('ucup', 150),
    ('otong', 170),
    ('mario', 170)
]

e = np.array(data, dtype=tipedata)

print(c)
