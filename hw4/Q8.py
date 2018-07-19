import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from visual import *
from visual.graph import *
import math
def load_file(path):
    fp = open(path, 'r')
    buf = fp.read().split('\n')
    fp.close()
    del buf[-1] # Delete the last element
    Xdata = list()
    Ydata = list()
    for data in buf:
        data = data.split()
        Xdata.append([])
        buff = list(map(lambda x: float(x.replace(",", "")), data[:-1])) # data[:-1] returns all elements [:] except the last one -1
        buff.insert(0, float(1))
        Xdata[-1].extend(buff)
        Ydata.append(int(data[-1]))

    X = np.array(Xdata)
    Y = np.array(Ydata)
    return X, Y

def Find_wreg(X,Y,lamda):
    m, n = X.shape
    wreg = np.linalg.pinv(X.T.dot(X) + lamda*np.eye(n)).dot(X.T).dot(Y) #eye(n) is the identity matrix
    return wreg

def calculate_err(X, Y, wreg):
    m, n = X.shape
    return 1 - (np.sum(np.sign(X.dot(wreg)) == Y)/float(m))

X_train, Y_train = load_file('hw4_train.txt')
X_test, Y_test = load_file('hw4_test.txt')

xplot = list()
yplotEtrain = list()
yplotEval = list()

for i in range (-10,3):
    wreg = Find_wreg(X_train[0:120], Y_train[0:120], pow(10,i))
    xplot.append(i)
    E_train = calculate_err(X_train[0:120], Y_train[0:120], wreg)
    E_val = calculate_err(X_train[120:], Y_train[120:], wreg)
    E_out = calculate_err(X_test, Y_test, wreg)
    yplotEtrain.append(E_train)
    yplotEval.append(E_val)
    print "log_10 lamda ="  ,i
    print "E_train = %lf" %E_train
    print "E_val = %lf" %E_val
    print "E_out = %lf\n" %E_out

plt.plot(xplot, yplotEtrain, label = 'E_train')
plt.plot(xplot, yplotEval, label = 'E_val')
plt.legend(loc='upper left', shadow=True)
plt.xlabel('log_10 lambda')
plt.ylabel('E')
plt.show()
raw_input()








