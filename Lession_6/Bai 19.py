import numpy as np
def mbe(y, y_pred):
    return np.sum(y-y_pred)/np.size(y)
y, y_pred = 1.0, 0.5
print(mbe(y, y_pred))