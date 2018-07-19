import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import random

data = open('train_data','r');
arr = [ ]
#arr = np.array
for line in data.readlines():
	y = [float(i) for i in line.split( )]
	y.insert(0, float(1))
	arr.append(y)
n = len(arr)
"""arr = np.array([])"""

"""for i in range(0,n):
	for j in range(0,5):
		arr[i][j] /= 20"""

#print arr

def PLA(arr):
	correct_counter = 0
	idx = 0
	flag = 0
	step = 0
	w = [0,0,0,0,0]
	while flag == 0 :
		if arr[idx][5] == sign(vector_dot(w,arr,idx)):
			correct_counter += 1
		else:
			update_weight(w,arr,idx)
			correct_counter = 0
			step += 1
		if idx == n-1:
			idx = 0
		else:
			idx += 1
		if correct_counter == n:
			flag = 1
	return step

def update_weight(w,arr,idx):
	for i in range (0,5):
		w[i]+= arr[idx][5]*arr[idx][i]


def sign(value):
	if value < 0:
		return -1
	else:
		return 1

def vector_dot(v1,v2,index):
	tmp = 0
	for i in range (0,5):
		tmp += v1[i]*v2[index][i]
	return tmp

array = []
total_step = 0
for i in range (1,2001):
	tmp = PLA(arr)
	random.shuffle(arr)
	array.append(tmp)
	total_step += tmp
	print "ith %d, step = %d\n" %(i,tmp)
#print array
print "average update times %d" %(total_step/2000)
plt.hist(array, bins = range(min(array), max(array)), facecolor='blue', alpha=0.5)
plt.xlabel('steps')
plt.ylabel('Frequency')
plt.title(r'Histogram')
plt.show()





