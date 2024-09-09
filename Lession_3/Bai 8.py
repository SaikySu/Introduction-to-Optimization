from __future__ import division, print_function, unicode_literals
import math
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(2)
x = np.random.randn(1000, 1)
y = 4+3*x+.2*np.random.randn(1000,1 ) #random data

#Crete Xbar
one = np.ones((x.shape[0],1))
xbar = np.concatenate((x,one),axis=1)
A = np.dot(xbar.T ,xbar)
B = np.dot(xbar.T ,y)
w_lr = np.dot(np.linalg.inv(A),B)
print('Solution found: ', w_lr.T)

#Output
w = w_lr
w_0 = w[0][0]
w_1 = w[1][0]
x0 = np.linspace(0,1,2, endpoint=True)
y0 = w_0 + w_1*x0

#Draw strain line and data
plt.plot(x.T, y.T, 'r.') #data
plt.plot(x0, y0, 'b', linewidth=3) #stain line
plt.axis([0,1,0,10])
plt.show()