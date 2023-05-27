import numpy as np
import matplotlib.pyplot as plt

# color: https://matplotlib.org/stable/api/colors_api.html
# line: https://matplotlib.org/stable/api/lines_api.html
# marker: https://matplotlib.org/stable/api/markers_api.html

# Fungsi Sinus
# y = A.sin(θ)
# y = A.sin(ωt)
# y = A.sin(ωt + θ)
# y = A.sin(2πft + θ)

# def sinusGenerator(amplitudo,frekuensi,tAkhir,tetha):
# 	t = np.arange(0,tAkhir,0.02)
# 	y = amplitudo*np.sin(2*np.pi*frekuensi*t + np.deg2rad(tetha))
# 	return t,y

# t1,y1 = sinusGenerator(5,1,1,0)
# plt.plot(t1,y1,'y')

# t2,y2 = sinusGenerator(5,1,1,30)
# plt.plot(t2,y2,'b')

# t3,y3 = sinusGenerator(5,1,1,60)
# plt.plot(t3,y3,'k--')

# t4,y4 = sinusGenerator(5,1,1,90)
# plt.plot(t4,y4,'-ro')

# plt.show()






def dampedOscillation(Amplitudo, m, b, w, t):
    horizontal = np.arange(0, t, 0.1)
    vertikal = Amplitudo*np.exp((-b*t)/(2*m))*np.cos(w*t)
    return horizontal,vertikal

t, y = dampedOscillation(Amplitudo=20, b=1, m=2, w=6, t=20)
plt.plot(t, y)
plt.show()








