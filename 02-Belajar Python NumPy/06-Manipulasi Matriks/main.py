import os
import numpy as np

os.system('cls')

# Manipulasi Matriks
a = np.array([[1,2,3],
              [4,5,6]])

print(f"Matriks a dengan ukuran {a.shape} =\n{a}")

# Transpose
print(f"Transpose Matriks a =")
print(a.transpose())
print(np.transpose(a))
print(a.T)

# Vektor baris --> flatten array
print(f"Flatten Matriks a =")
print(a.ravel())
print(np.ravel(a))
print(a.flatten())

# reshape
print(f"Reshape Matriks a =")
print(a.reshape(3,2))

# resize matriks
a.resize(3,2)
print(f"Reshape Matriks a =")
print(a)
print(f"Matriks a dengan ukuran {a.shape}")































