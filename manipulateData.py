import re
import numpy as np
from math import sqrt,sin,cos,atan
a=88.5
b=185.63415
x0=155
y0=420-113
def ovalDistance(radians):
    dis=sqrt(pow(a*cos(radians),2)+pow(b*sin(radians),2))
    return dis
data=open("G:\data.txt","r")
data=data.readlines()
x=[]
y=[]
for line in data:
    if line=="\n":
        continue
    else:
        dots=re.findall(r"\d+",line)
        x.append(eval(dots[0]))
        y.append(eval(dots[1]))
x=np.array(x)
y=np.array(y)
dotRad=np.arctan((y-y0)/(x-x0))
dotDis=np.sqrt(pow(x-x0,2)+pow(y-y0,2))
liqWid=[]
for i in range(len(dotRad)):
    if y[i]>=113:
        Dis=dotDis[i]-a
    else:
        Dis=dotDis[i]-ovalDistance(dotRad[i])
    liqWid.append(Dis)
print(liqWid)