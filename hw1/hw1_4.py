from matplotlib import pyplot as plt
import numpy as np

A=1
w=1
T=1
th1=0
th2=45/180*np.pi
th3=90/180*np.pi

t = np.arange(-5,5,0.01)
y1 = A*np.exp(-t/T)*np.sin(w*t+th1)
y2 = A*np.exp(-t/T)*np.sin(w*t+th2)
y3 = A*np.exp(-t/T)*np.sin(w*t+th3)

plt.plot(t, y1,label='Angle=0')
plt.plot(t,y2,label='Angle=pi/4')
plt.plot(t,y3,label='Angle=pi/2')
plt.xlabel("t")
plt.ylabel("y")
plt.title("y = A*exp(-t/T)*sin(w*t+th)")
plt.legend(loc='best')
plt.figtext(0, 0, "A=1,W=1,T=1")
plt.show()