import numpy as np
import matplotlib.pyplot as plt

# Tạo dãy giá trị của t từ 0 đến 10 với khoảng cách 0.1
t = np.arange(0, 10, 0.1)

# Tính giá trị của hàm số
y = 1/np.sqrt(1+t)

# Vẽ đồ thị
plt.plot(t, y)

# Đặt tiêu đề cho đồ thị và các trục
plt.title('Đồ thị của hàm số 1/sqrt(1+t)')
plt.xlabel('t')
plt.ylabel('y')

# Hiển thị đồ thị
plt.show()
