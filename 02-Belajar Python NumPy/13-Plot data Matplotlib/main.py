import numpy as np
import matplotlib.pyplot as plt

# persamaan linear
# y = x**2 + 3
x = np.arange(-20,21,1)  # [0,20)
y = x**2 + 3

plt.plot(x,y)
plt.show()


# lingkaran
jari2 = 5
sudut = np.linspace(0,2*np.pi,1000)
x = jari2*np.cos(sudut)
y = jari2*np.sin(sudut)
