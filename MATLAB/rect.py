import numpy as np
import matplotlib.pyplot as plt

# Khởi tạo biến
A = 1
T = 2*np.pi
t = np.linspace(-5, 5, 1000) # Tạo một vector thời gian từ -5 đến 5

# Tạo tín hiệu xung hình chữ nhật
x = np.zeros(len(t))
for i in range(len(t)):
    if abs(t[i]) <= T/2:
        x[i] = A
    else:
        x[i] = -A

# Vẽ đồ thị
plt.plot(t, x)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Square Waveform')
plt.grid(True)
plt.show()
