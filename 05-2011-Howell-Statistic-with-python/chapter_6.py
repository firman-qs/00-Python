import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

mean = 25
sdev = 5
mean2 = 30
sdev2 = 10
fontsz = 12

# set vertical line
for i in range(-5, 8):
    plt.axvline(mean+i*sdev, color='yellow', ls='--', lw=.5,
                label=r'$mean+(i\times std.\ deviasi)$' if i == 0 else None)
# set x axis range
plt.axvline(mean, color='blue', ls='-', lw=1.5)
plt.axvline(mean2, color='red', ls='-', lw=1.5)
x = np.arange(-5, 65, 1)

# set plot
plt.plot(x, norm.pdf(x, mean, sdev), color='blue', lw=2, label='Kelas 4')
plt.plot(x, norm.pdf(x, mean2, sdev2), color='yellow', lw=2, label='Kelas 9')

# set ticks
plt.xticks([x for x in range(-5, 65, 5)],
           [f"{x}\nmean" if x == 25 else f"{x}\nmean" if x == 30 else x for x in range(-5, 65, 5)], fontsize=fontsz)
plt.yticks(fontsize=fontsz)

plt.autoscale(enable=True, axis='x', tight=True)
plt.legend(fontsize=fontsz)
plt.show()
