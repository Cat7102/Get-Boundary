import re
import numpy as np
from math import sqrt,sin,cos,atan
a=89.5
b=285.9634146341463
r=79.5
x0=(201)/2
y0=211-r-7

def ovalDistance(radians):
    dis=sqrt(pow(a*cos(radians),2)+pow(b*sin(radians),2))
    return dis

mdata=open("G:\液体.txt","r")
data=mdata.readlines()
x=[]
y=[]
for line in data:
    if line=="\n":
        continue
    else:
        dots=re.findall(r"\d+",line)
        x.append(eval(dots[0]))
        y.append(211-eval(dots[1]))
mdata.close()
x=np.array(x)
y=np.array(y)
dotRad=np.arctan((y-y0)/(x-x0))
dotDis=np.sqrt(pow(x-x0,2)+pow(y-y0,2))
liqWid=[]
n=0
for i in range(len(dotRad)):
    #if y[i]>y0:
        #Dis=dotDis[i]-a
    #else:
        #Dis=dotDis[i]-ovalDistance(dotRad[i])
    Dis=dotDis[i]-r
    if Dis<0:
        n+=1
        continue
    liqWid.append(Dis)
liqWid=np.array(liqWid)
wid_ave=liqWid.sum()*12.7/len(liqWid)/r
print(wid_ave)
print(len(liqWid))
print(n)