import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,1,100)
y = np.sin(x)

fig = plt.figure()

plt.plot(x,y,".r")

plt.show()
