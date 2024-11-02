import numpy as np
def Huber(y, y_pred, delta):
    condition = np.abs(y - y_pred) < delta
    l = np.where(condition, 0.5*(y - y_pred)**2,
         delta*(np.abs(y - y_pred)-0.5*delta))
    return np.sum(l)/np.size(y)
y,y_pred, delta = 1.0, 0.5, 0.25
print(Huber(y,y_pred, delta))