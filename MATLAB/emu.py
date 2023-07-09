import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0, 5, 0.01)
y = np.exp(-t)

plt.plot(t, y)
plt.xlabel('t')
plt.ylabel('e^-t')
plt.title('Đồ thị của hàm số e^-t')
plt.show()
