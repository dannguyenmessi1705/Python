import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(-1, 1, 1000)
s = np.zeros_like(t)
s[t >= 0] = 0

plt.plot(t, s)
plt.xlabel('t')
plt.ylabel('s(t)')
plt.title('Step Function')
plt.show()