import numpy as np
import matplotlib.pyplot as plt

def sinCosTanGenerator(amplitudo,frekuensi,tAkhir,tetha):
	t  = np.arange(0,tAkhir+1,0.02)
	y  = amplitudo*np.sin(2*np.pi*frekuensi*t + np.deg2rad(tetha))
	y2 = amplitudo*np.cos(2*np.pi*frekuensi*t + np.deg2rad(tetha))
	return t,y,y2

t,y,y2 = sinCosTanGenerator(10,1,1,0)

plt.plot(t,y)
plt.plot(t,y2)

# set axis
# plt.axis([xmin, xmax, ymin, ymax])
plt.axis([0,1,-10,10])

plt.show()
