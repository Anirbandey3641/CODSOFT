import matplotlib.pylab as plt
import numpy as np
x=np.linspace(-5,5,100)
plt.plot(x,4*(x*x))
plt.plot(x,(2*x)+3)
plt.legend(['$y=4x^2$','$y=2x+3$'])
plt.show()