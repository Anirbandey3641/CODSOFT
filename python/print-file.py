import matplotlib.pylab as plt
import numpy as np
plt.figure(1)
x=np.linspace(-2*np.pi,2*np.pi,100)
plt.plot(x,x*(np.sin(x)))
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.title('$x and xsin(x)$')
plt.history('print-file.py')
plt.show()
  
