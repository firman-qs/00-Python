import os
import numpy as np

os.system('cls')

# resource
# https://www.cuemath.com/algebra/inverse-of-3x3-matrix/
# https://byjus.com/maths/cofactor/#:~:text=A%20cofactor%20is%20a%20number,based%20on%20the%20element's%20position.
# inverse -> https://numpy.org/doc/stable/reference/generated/numpy.linalg.inv.html
# determinant -> https://numpy.org/doc/stable/reference/generated/numpy.linalg.det.html

# matriks
a = np.array([[8,5],    # 2x2
              [2,4]])

b = np.array([[1,2,-1],  # 3x3
              [2,1,2],
              [-1,2,1]])

c = np.eye(2)


# Determinan 
det = np.linalg.det(b)
print(det)

# invers
inv = np.linalg.inv(b)
print(inv)

# adjoin = invers * determinan
adj = inv.dot(det)
print(adj)

# cofactor = Transpose adjoin 
cof = adj.transpose()
print(cof)