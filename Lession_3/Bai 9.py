from __future__ import division, print_function, unicode_literals
import math

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(2)

x = np.random.randn(1000, 1)
y = 4+3*x+.2*np.random.randn(1000,1 )

#Create xbar
one = np.ones((x.shape[0],1))
xbar = np.concatenate((one,x),axis=1)
A = np.dot(xbar.T ,xbar)
B = np.dot(xbar.T ,y)
w_exact = np.dot(np.linalg.pinv(A),B)

def cost(w):
    return .5/xbar.shape[0]*np.linalg.norm(y-xbar.dot(w), 2)**2

def grad(w):
    return 1/xbar.shape[0] * xbar.T.dot(xbar.dot(w)-y)

def numerial_grad(w, cost):
    eps= 1e-4
    g = np.zeros_like(w)
    for i in range(len(w)):
        w_p = w.copy()
        w_n = w.copy()
        w_p[i] += eps
        w_n[i] -= eps
        g[i] = (cost(w_p) - cost(w_n))/(2*eps)
    return g

def check_grand(w, cost, grad):
    w=np.random.rand(w.shape[0],w.shape[1])
    grad1 = grad(w)
    grad2 = numerial_grad(w, cost)
    return True if np.linalg.norm(grad1-grad2) < 1e-6 else False
print('Check gradient...', check_grand(np.random.rand(2,1), cost, grad))

def GD_NAG(w_init, grad, eta, gamma):
    w = [w_init]
    v = [np.zeros_like(w_init)]
    for it in range(100):  # Sửa i thành it để trả về đúng số lần lặp
        v_new = gamma * v[-1] + eta * grad(w[-1] - gamma * v[-1])
        w_new = w[-1] - v_new  # Đổi dấu của v_new để đúng với NAG

        if np.linalg.norm(grad(w_new)) / len(w_new) < 1e-3:  # Bỏ dấu ngoặc không cần thiết
            break
        w.append(w_new)
        v.append(v_new)
    return (w, it)  # Trả về it thay vì biến không khai báo 'i'

w_init = np.array([[2], [1]])
(w_mm, it_mm) = GD_NAG(w_init, grad, 0.5, 0.9)


N = x.shape[0]
a1 = np.linalg.norm(y, 2)**2/N
b1 = 2*np.sum(x)/N
c1 = np.linalg.norm(x, 2)**2/N
d1 = -2*np.sum(y)/N
e1 = -2*x.T.dot(y)/N

matplotlib.rcParams['xtick.direction'] = 'out'
matplotlib.rcParams['ytick.direction'] = 'out'

delta = 0.025
xg = np.arange(1.5, 7.0, delta)
yg = np.arange(0.5, 4.5, delta)
Xg, Yg = np.meshgrid(xg, yg)
Z = a1 + Xg**2 + b1*Xg*Yg + c1*Yg**2 + d1*Xg + e1*Yg

import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

def save_gif2(eta, gamma):
    (w, it) = GD_NAG(w_init, grad, eta, gamma)
    fig, ax = plt.subplots(figsize=(4, 4))
    plt.cla()
    plt.axis([1.5, 7, 0.5, 4.5])

    def update(ii):
        if ii == 0:
            plt.cla()
            CS = plt.contour(Xg, Yg, Z, 100)
            manual_locations = [(4.5, 3.5), (4.2, 3), (4.3, 3.3)]
            animlist = plt.clabel(CS, inline=.1, fontsize=10, manual=manual_locations)

            plt.plot(w_exact[0], w_exact[1], 'go')
        else:
            animlist = plt.plot([w[ii-1][0], w[ii][0]], [w[ii-1][1], w[ii][1]], 'r')
        animlist = plt.plot(w[ii][0], w[ii][1], 'ro', markersize=4)
        xlabel = '$\\eta=$'+str(eta) + '; iter=%d/%d' %(ii, it)
        xlabel += '; ||grad||_2 = %.3f' % np.linalg.norm(grad(w[ii]))
        ax.set_xlabel(xlabel)
        return animlist, ax
    animl = FuncAnimation(fig, update, frames=np.arange(0, it), interval=200)
    fn = 'LR_NAG_contours.gif'
    animl.save(fn,dpi=100, writer='imagemagick')

eta = 1
gamma = .9
save_gif2(eta, gamma)





















