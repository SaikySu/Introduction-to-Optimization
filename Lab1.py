#BT1: Bài toán tối ưu - giảm tốc độ và biến

import numpy as np
#Định nghĩa hàm grendient f(x) = 2x
def gradient(x):
    return 2*x
#Hàm tối ưu hóa Grandient descent
def grandient_descent(gradient, start, lean_rate, n_iter = 50, tolerance = 1e-6):
    vector = start
    for _ in range(n_iter):
        diff = -lean_rate * gradient(vector)
        if np.all(np.abs(diff) <= tolerance):
            break
        vector+=diff
    return vector
#Nhập số điểm ban đầu
start = 5.0
#Tỉ lệ huấn luyện
learning_rate = 0.1
#Số lần lặp
n_iter = 50
#Số hội tụ
tolerance = 1e-6
#Hàm tối ưu hóa giảm độ dốc
result = grandient_descent(gradient, start, learning_rate, n_iter, tolerance)
print(result)

#Với đầu ra là số thực (7.136238463529802e-05)