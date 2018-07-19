import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

data1 = open('data1','r');
data2 = open('data2','r');
E_in = []
E_out = []
for line in data1.readlines():
        E_in = [float(i) for i in line.split( )]
for line in data2.readlines():
        E_out = [float(i) for i in line.split( )]

plt.scatter(E_in , E_out , s = 10)
plt.xlabel('E_in')
plt.ylabel('E_out')
plt.title('Scatter Plot')
plt.show()
