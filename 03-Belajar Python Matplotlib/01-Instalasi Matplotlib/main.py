import numpy as np
import matplotlib.pyplot as plt

# persamaan garis linear
# y = 2x + 1
x = np.arange(1,20,1)
y = x**2

# lingkaran
jari2 = 50
sudut = np.linspace(0,2*np.pi,50)
y2 = jari2*np.cos(sudut)
x2 = jari2*np.sin(sudut)

plt.plot(x,y)
plt.plot(x2,y2)

plt.show()