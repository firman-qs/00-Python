import numpy as np
import matplotlib.pyplot as plt

'''
1. Menentukan data
2. Membuat plot
3. menampilkan plot
'''

x = np.array([1,2,3,4,5])
y = x**2
y2 = y**2

plt.plot(x,y)
plt.plot(x,y2)

plt.show()
