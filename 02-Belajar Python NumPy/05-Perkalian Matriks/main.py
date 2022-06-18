import os
os.system('cls')
import numpy as np

# Matriks
a = np.array([[1,2],
              [3,4]])
b = np.ones([2,2])

print(f"Matriks a =\n{a}")
print(f"Matriks b =\n{b}")

# perkalian matriks
c1 = np.dot(a,b)
c2 = a.dot(b)
c3 = a @ b
print(f"Matriks a . b =\n{c1}")
print(f"Matriks a . b =\n{c2}")
print(f"Matriks a . b =\n{c3}")

