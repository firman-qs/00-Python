import numpy as np
import matplotlib.pyplot as plt

# membuat data
def sinusGenerator(amplitudo,frekuensi,tAkhir,tetha):
	t = np.arange(0,tAkhir,0.02)
	y = amplitudo*np.sin(2*np.pi*frekuensi*t + np.deg2rad(tetha))
	return t,y

t1,y1 = sinusGenerator(1,1,1.5,0)
t2,y2 = sinusGenerator(1,1,1.5,60)
t3,y3 = sinusGenerator(1,1,1.5,120)

# membuat plot
data1 = plt.plot(t1,y1)
data2 = plt.plot(t2,y2)
data3 = plt.plot(t3,y3)

# set properties
plt.setp(data1, c='r', linestyle='-',  linewidth='2', marker='_', markersize='10')
plt.setp(data2, c='b', linestyle='--', linewidth='1.5')
plt.setp(data3, c='k', linestyle='-.', linewidth='1')

# menampilkan data
plt.show()


