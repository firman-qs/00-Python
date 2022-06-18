import os 
import numpy as np
os.system('cls')

a = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

b = np.arange(11,20,1)
b.resize(3,3)

print(f"""Matriks a =
{a}

Matriks b =
{b}""")

# horizontal stack
c = np.hstack((a,b))
# vertical stack
d = np.vstack((a,b))

print(f"""
Horizontal stack a dan b =
{c}

Vertical stack a dan b =
{d}""")
