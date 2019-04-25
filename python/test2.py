#%%
import numpy as np 


#%%
a=np.array([[1,2],[3,4]])

a*b

#%%
c=np.array([[4, 3], [2, 1]])
for xi in c:
    print(xi)

#%%
for xi in xmatrix
    error=yi-weight*xi
    weight=weight+step*xi*error

#%%
import time
import numpy as np 
from machinelearninginaction.Ch05 import logRegres
dataArr,labelMat=logRegres.loadDataSet()
dataArr=np.array(dataArr)
num=len(labelMat)
labelMat=np.array(labelMat).reshape(num,1)
weights=np.ones((1,3))
err=10
step=0.001
# while(np.linalg.norm(err)>1.5):
cycle=500
while cycle>0:
    # 第0轴沿着行的垂直往下，第1轴沿着列的方向水平延伸。
    h=logRegres.sigmoid(np.sum(weights*dataArr,axis=1))
    h=h.reshape(num,1)
    err=labelMat-h
    weights=weights+step*np.sum(np.multiply(err,dataArr),axis=0)
    cycle=cycle-1
weights

#%%
a=np.array([[4,5,6],[7,8,9],[11,12,13]])
b=np.array([[1],[2],[3]])
np.multiply(a,b)