import numpy as np
def mse(y, y_pred):
    return np.sum((y - y_pred) ** 2)/np.size(y)
y, y_pred = 1.0, 0.5
print(mse(y, y_pred))