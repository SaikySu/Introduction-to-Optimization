import numpy as np
def cross_entropy(y, y_pred):
    return -np.sum(y * np.log(y_pred) + (1 - y) * np.log(1 - y_pred))
y, y_pred = 1.0, 0.5
print(cross_entropy(y, y_pred))