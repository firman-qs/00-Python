import matplotlib.pyplot as plt
import numpy as np

def sinusGenerator(amplitudo,frekuensi,tAkhir,tetha):
    t = np.arange(0,tAkhir,0.02)
    y1 = amplitudo*np.sin(2*np.pi*frekuensi*t + np.deg2rad(tetha))
    y2 = amplitudo*np.cos(2*np.pi*frekuensi*t + np.deg2rad(tetha))
    return t,y1,y2

t,y1,y2 = sinusGenerator(1,1,1.6,0)

# create plot & legend

# cara 1
# plt.plot(t,y1, label='sin(0)')
# plt.plot(t,y2, label='cos(0)')
# plt.legend()

# cara 2
# plt.plot(t,y1, label='sin(0)')
# plt.plot(t,y2, label='cos(0)')
# plt.legend(loc=1) # https://matplotlib.org/stable/api/legend_api.html

# cara 3
# plt.plot(t,y1, label='sin(0)')
# plt.plot(t,y2, label='cos(0)')
# plt.legend(loc=1, bbox_to_anchor=(0.1,1.2))

# cara 4
plt.figure()
ax = plt.subplot(111)
plt.plot(t,y1, label='sin(0)')
plt.plot(t,y2, label='cos(0)')
box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width*.9, box.height])
plt.legend(loc=2, bbox_to_anchor=(1,1))


# show plot
plt.show()