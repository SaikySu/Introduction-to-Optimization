import numpy as np

def adam(X, y, theta, learning_rate, iteration, beta1=0.9, beta2=0.999, epsilon=1e-8):
    m = len(y)
    m_t = np.zeros(theta.shape)
    v_t = np.zeros(theta.shape)
    t = 0

    for _ in range(iteration):
        for i in range(m):
            t+=1
            X_i = X[i, :].reshape(1, -1)
            y_i = y[i]
            prediction = np.dot(X_i,theta)
            error = prediction - y_i
            gradient = X_i.T * error

            m_t = beta1 * m_t + (1 - beta1) * gradient
            v_t = beta2 * v_t + (1 - beta2) * (gradient**2)

            m_t_hat = m_t / (1 - beta1**t)
            v_t_hat = v_t / (1 - beta2**t)

            theta = theta - learning_rate * m_t_hat / (np.sqrt(v_t_hat) + epsilon)
    return theta

X = np.array([[1, 2], [3, 4]]) # Ví dụ dữ liệu X
y = np.array([0, 1])           # Ví dụ dữ liệu y
theta = np.array([0.1, 0.1])   # Ví dụ tham số theta ban đầu
learning_rate = 0.01
iteration = 1000

# Gọi hàm adam và in ra kết quả
theta = adam(X, y, theta, learning_rate, iteration)
print(theta)