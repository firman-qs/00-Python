import os
import numpy as np

os.system('cls')

a = np.array([[2,3],
              [1,2]])

b = np.array([[23],
              [14]])

# menyelesaikan persamaan linier
c = np.linalg.inv(a)
d = c@b

print(d)

# menyelesaikan persamaan linier, cara 2
e = np.linalg.solve(a,b)
print(d)


