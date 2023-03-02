
from matplotlib import pyplot as plt
import numpy as np

A=1
B=1

t = np.arange(-5,5,0.01)
y = A*np.exp(-t/2)+B*np.exp(-t/10)

plt.plot(t, y, 'r')
plt.xlabel("t")
plt.ylabel("y")
plt.title("y =A*exp(-t/2)+B*exp(-t/10)")
plt.figtext(0, 0, "A=1,B=1")
plt.show()