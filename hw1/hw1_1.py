from matplotlib import pyplot as plt
import numpy as np

T=1
t = np.arange(-5,5,0.01)
y = np.exp(-t/T)

plt.plot(t, y, 'r')

plt.xlabel("t")
plt.ylabel("y")
plt.title("y = exp(-t/T)")
plt.figtext(0, 0, "T=1")

plt.show()
