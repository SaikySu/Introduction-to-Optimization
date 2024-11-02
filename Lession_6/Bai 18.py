import numpy as np
def mae(y, y_pred):
    return np.sum(np.abs(y-y_pred))/np.size(y)
y, y_pred = 1.0, 0.5
print(mae(y, y_pred))