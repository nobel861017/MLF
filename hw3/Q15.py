###Q15.py
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random
import math
def add_noise(n,f):
    pos = np.random.permutation(n)
    f[pos[0: round(0.1*n)]] *= -1
    return f

def preprocess_data(X1,X2,n):
	X_c = np.c_[X1, X2]
	X = np.c_[np.ones((n, 1)), X_c]
	return X

def make_Data(n):
	#make n x 1 array with elements falling in range[-1,1)
    X1 = np.random.uniform(-1, 1, n)
    X2 = np.random.uniform(-1, 1, n)
    X = preprocess_data(X1,X2,n)
    #print('X: ', X)
    f = np.sign(np.power(X1, 2)+np.power(X2, 2) - 0.6)
    f = add_noise(n,f)
    Y = f.reshape((n, 1))
    return X, Y


def trans(X):
    row, col = X.shape
    A = np.zeros((row, 6))
    A[:, 0:col] = X
    A[:, col] = X[:, 1]*X[:, 2]
    A[:, col+1] = X[:, 1]**2
    A[:, col+2] = X[:, 2]**2
    return A

times = 1000
data_size = 1000
sum_err = 0
array = []

for i in range(times):
    X, Y = make_Data(data_size)
    X_train_data = trans(X)
    w_lin = np.linalg.pinv(X_train_data.T.dot(X_train_data)).dot(X_train_data.T).dot(Y)
    test_data_X, Ytest_data_Y = make_Data(data_size)
    test_data_X_trans = trans(test_data_X)
    y_out = np.sign(test_data_X_trans.dot(w_lin))
    err = np.sum(y_out!=Ytest_data_Y)/1000.0
    array.append(err)
    sum_err += err
#print('theta: ', theta.T)
print "Average E_out: %lf" %(sum_err/1000.0)

#print array
#, bins = range(array.min, array.max)
#range(int(math.floor(min(array))), int(max(array)))
plt.hist(array, bins = 50, facecolor='blue', alpha=0.5)
plt.xlabel('err')
plt.ylabel('frequency')
plt.title(r'E_out Histogram')
plt.show()



