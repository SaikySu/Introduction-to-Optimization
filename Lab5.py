import numpy as np
from scipy.optimize import minimize
def rosen_with_args(x, a, b):
    return  sum(a*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0) + b
x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen_with_args, x0, method='nelder-mead', args=(0.5, 1.),
               options={'xatol': 1e-8, 'disp': True})
print(res.x)
