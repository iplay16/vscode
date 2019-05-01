#%%
import numpy as np 
import imp

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
cycle=600000
for k in range(cycle):
    # 第0轴沿着行的垂直往下，第1轴沿着列的方向水平延伸。
    h=logRegres.sigmoid(np.sum(weights*dataArr,axis=1))
    h=h.reshape(num,1)
    err=labelMat-h
    weights=weights+step*np.sum(np.multiply(err,dataArr),axis=0)
print(np.linalg.norm(err))
weights

#%%
a=np.array([[4,5,6],[7,8,9],[11,12,13]])
b=np.array([[1],[2],[3]])
np.multiply(a,b)

#%%
from machinelearninginaction.Ch05 import logRegres
import imp
imp.reload(logRegres)
dataArr,labelMat=logRegres.loadDataSet()
logRegres.gradAscent(dataArr,labelMat)

#%%
import pdb
a = np.array([[1, 2, 3],[4,5,6],[7,8,9]])
b = np.array([[1, 2, 3]])
pdb.set_trace()
print(a)
print(b)
# np.dot(b,a)
np.sum(a*b.T,axis=0)
# ;print(c);print(c.shape);print(type(c))

#%%
import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set(xlim=[0.5, 4.5], ylim=[-2, 8], title='An Example Axes',
       ylabel='Y-Axis', xlabel='X-Axis')
plt.show()

#%%
i = np.matrix('1,2;3,4') 
print(i)
print(i[:,1])

#%%
from machinelearninginaction.Ch02 import kNN
import os
dd,dl=kNN.file2matrix(os.getcwd()+r'\machinelearninginaction\Ch02'+r'\datingTestSet2.txt')
fig=plt.figure()
ax=fig.add_subplot(111)
dd=dd[0:5,:]
dl=dl[0:5]
ax.scatter(dd[:,1],dd[:,2],25*np.array(dl),25*np.array(dl))
#%%
retArray = np.array([[1,2,3,4,5]])
indata = np.array([[1,2,3,4,5]])
retArray[indata>3]=-1
retArray
#%%
from machinelearninginaction.Ch07 import adaboost
import imp
import numpy as np 
imp.reload(adaboost)
import logging
imp.reload(logging)
logging.basicConfig(level=logging.DEBUG,
                    filename='f:\\adebug.txt',
                    filemode='w')
datMat,classLabels=adaboost.loadSimpData()
adaboost.loadSimpData()
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(np.squeeze(np.array(datMat[:,0]).T).T,np.squeeze(np.array(datMat[:,1]).T),(2+np.array(classLabels))*25,(np.array(classLabels)+2)*25)
D=np.mat(np.ones((5,1))/5)
adaboost.adaBoostTrainDS(datMat,classLabels,9)

#%%
from machinelearninginaction.Ch07 import adaboost
imp.reload(adaboost)
datMat,classLabels=adaboost.loadSimpData()
adaboost.loadSimpData()
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(np.squeeze(np.array(datMat[:,0]).T).T,np.squeeze(np.array(datMat[:,1]).T),(3+np.array(classLabels))*45,(np.array(classLabels)+3)*45)

#%%
import os
datArr,labelArr=adaboost.loadDataSet(os.getcwd()+'\\machinelearninginaction\\Ch07'+'\\horseColicTraining2.txt')
classifierArr=adaboost.adaBoostTrainDS(datArr,labelArr,10)
testArr,testLabelArr=adaboost.loadDataSet(os.getcwd()+'\\machinelearninginaction\\Ch07'+'\\horseColicTest2.txt')
prediction10=adaboost.adaClassify(testArr,classifierArr)
errArr=mat(ones(67,1))
errArr[prediction10!=mat(testLabelArr).T].sum()

#%%
import re
m=re.search("{*}","{dfk}")
m.group()
