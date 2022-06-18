import os
import numpy as np

os.system('cls')

# NumPy dot
# format ==> numpy.dot(a, b, out=None)
# https://numpy.org/doc/stable/reference/generated/numpy.dot.html
a = np.array([[1,2,3],
              [4,5,6]])
    
b = np.array([[2,3],
              [4,5],
              [8,9]])

# contoh vektor i,j
c = np.array([3,4,0])
d = np.array([6,8,0])

dot = np.dot(c,d)
print(dot)

# NumPy cross
# format ==> numpy.cross(a, b, axisa=- 1, axisb=- 1, axisc=- 1, axis=None) 
# https://numpy.org/doc/stable/reference/generated/numpy.cross.html
cross = np.cross(c,d) # cross vektor 2D

x = np.array(([1,2,0],
              [3,5,7],
              [5,6,7]))
y = np.array(([4,5,6],
              [2,4,8],
              [3,9,8]))

# cross vektor multiD (matriks)
print(np.cross(x, y, axis=0)) 
