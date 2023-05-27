import numpy as np

# membuat vektor 1D
a = np.array([1, 2, 3, 4, 5])
b = np.array([1.3, 2, 3, 4.7, 5])

print(f"{a}\n{b}")

# membuat vektor dengan range
c = np.arange(1, 20, 2)
print(c)

# membuat linspace
d = np.linspace(0, 20, 5)
print(d)

# array multidimensi/matriks
e = np.array([(1, 2, 3), 
              (4, 5, 6)])
print(e)

# matriks dengan nilai nol
f = np.zeros((5,5))
print(f)

# matriks dengan nilai nol
g = np.ones((5,5))
print(g)

# matriks identitas
h = np.identity(5)
j = np.eye(5)
print(h)
print(j)