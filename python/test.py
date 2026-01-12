import matplotlib.pylab as plt
import numpy as np
import math
t=np.linspace(-math.pi,math.pi,100)
print(len(t))
plt.plot(t,np.cos(t))
plt.show()
plt.clf()
plt.show()
plt.plot(t,np.sin(t))
plt.show()
plt.plot(np.sin(t)*np.sin(t))
plt.show()