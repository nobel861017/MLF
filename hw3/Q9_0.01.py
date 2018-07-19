#Q9_0.01.py
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import pandas
from visual import *
from visual.graph import *
import random

myScene = gdisplay(foreground=color.black,
                   background=color.white, xtitle='t', ytitle='E_out')
myCurve1 = gcurve(color=color.blue)
myCurve2 = gcurve(color=color.black)
def h(x):
    return 1/(1+np.exp(-1*x))

def cal_E_out(X, Y, w):
    y = X.dot(w)
    y[y > 0] = 1
    y[y <= 0] = -1
    err = np.sum(y != Y)/float(len(Y))
    #print(err)
    return err

def do_logistic_regression(X, Y, X_test, Y_test, eta, T, type):
    row, col = X.shape
    w = np.zeros((col, 1))
    num = 0
    N = row
    for i in range(0,T):
        if type == 0:	#GD
            grad = (-1*X*Y).T.dot(h(-1*X.dot(w)*Y))/N
            w -= eta*grad
            E_out_of_wt = cal_E_out(X_test, Y_test, w)
            myCurve1.plot(pos=(i,E_out_of_wt))
        elif type == 1:	#SGD
            if num >= row:
                num = 0
            grad = -Y[num, 0]*X[num: num+1, :].T*h(-1*X[num, :].dot(w)[0]*Y[num, 0])
            num += 1
            w -= eta*grad
            E_out_of_wt = cal_E_out(X_test, Y_test, w)
            myCurve2.plot(pos=(i,E_out_of_wt))
    return w

def get_Data(filename):
    data = pandas.read_csv(filename, sep='\s+', header=None)
    data = data.as_matrix()
    col, row = data.shape
    X = np.c_[np.ones((col, 1)), data[:, 0: row-1]]
    Y = data[:, row-1:row]
    return X, Y

eta = 0.01
T = 2000
X, Y = get_Data('hw3_test.dat.txt')
X_train, Y_train = get_Data('hw3_train.dat.txt')
w = do_logistic_regression(X_train, Y_train, X, Y, eta, T, 0)
E_out = cal_E_out(X, Y, w)
print "eta = 0.001:\n"
print "GD, E_out = %f\n" %E_out

w = do_logistic_regression(X_train, Y_train, X, Y, eta, T, 1)
E_out = cal_E_out(X, Y, w)
print "SGD, E_out = %f" %E_out

