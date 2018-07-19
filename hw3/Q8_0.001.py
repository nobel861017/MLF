#Q8_0.001.py
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import pandas
from visual import *
from visual.graph import *
import random

myScene = gdisplay(foreground=color.black,
                   background=color.white, xtitle='t', ytitle='E_in')
myCurve1 = gcurve(color=color.blue)
myCurve2 = gcurve(color=color.black)
def h(x):
    return 1/(1+np.exp(-1*x))

def cal_E_in(X, Y, w):
    y = X.dot(w)
    y[y > 0] = 1
    y[y <= 0] = -1
    err = np.sum(y != Y)/float(len(Y))
    #print(err)
    return err

def do_logistic_regression(X, Y, eta, T, type):
    row, col = X.shape
    w = np.zeros((col, 1))
    num = 0
    N = row
    for i in range(0,T):
        if type == 0:	#GD
            grad = (-1*X*Y).T.dot(h(-1*X.dot(w)*Y))/N
            w -= eta*grad
            E_in_of_wt = cal_E_in(X, Y, w)
            #print "E_in_of_wt: %f\n" %E_in_of_wt
            myCurve1.plot(pos=(i,E_in_of_wt))
        elif type == 1:	#SGD
            if num >= row:
                num = 0
            grad = -Y[num, 0]*X[num: num+1, :].T*h(-1*X[num, :].dot(w)[0]*Y[num, 0])
            num += 1
            w -= eta*grad
            E_in_of_wt = cal_E_in(X, Y, w)
            #print "E_in_of_wt: %f\n" %E_in_of_wt
            myCurve2.plot(pos=(i,E_in_of_wt))
    return w

def get_Data(filename):
    data = pandas.read_csv(filename, sep='\s+', header=None)
    data = data.as_matrix()
    col, row = data.shape
    X = np.c_[np.ones((col, 1)), data[:, 0: row-1]]
    Y = data[:, row-1:row]
    return X, Y
eta = 0.001
T = 2000
X, Y = get_Data('hw3_train.dat.txt')

w = do_logistic_regression(X, Y, eta, T, 0)
E_in = cal_E_in(X, Y, w)
print "eta = 0.001:\n"
print"GD, E_in = %f\n" %E_in

w = do_logistic_regression(X, Y, eta, T, 1)
E_in = cal_E_in(X, Y, w)
print"SGD, E_in = %f" %E_in

