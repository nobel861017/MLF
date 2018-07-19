### function.py
from visual import *
from visual.graph import *
def sign(x):
	if x and x > 0:
		return 1
	else:
		return -1
a = 1
myScene = gdisplay(foreground=color.black,
                   background=color.white, xtitle='ax', ytitle='y')
myCurve = gcurve(color=color.black)
for i in range(0,50):
	y = sign(abs(a*i%4 - 2) - 1)
	myCurve.plot(pos=(i,y))