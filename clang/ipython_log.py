# IPython log file

#%%
from machinelearninginaction.Ch07 import adaboost
imp.reload(adaboost)
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='f:\\adebug.txt',
                    filemode='w')
datMat,classLabels=adaboost.loadSimpData()
adaboost.loadSimpData()
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(np.squeeze(np.array(datMat[:,0]).T).T,np.squeeze(np.array(datMat[:,1]).T),(2+np.array(classLabels))*25,(np.array(classLabels)+2)*25)
D=np.mat(np.ones((5,1))/5)
adaboost.buildStump(datMat,classLabels,D)
#%%
from machinelearninginaction.Ch07 import adaboost
import importlib
imp.reload(adaboost)
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='f:\\adebug.txt',
                    filemode='w')
datMat,classLabels=adaboost.loadSimpData()
adaboost.loadSimpData()
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(np.squeeze(np.array(datMat[:,0]).T).T,np.squeeze(np.array(datMat[:,1]).T),(2+np.array(classLabels))*25,(np.array(classLabels)+2)*25)
D=np.mat(np.ones((5,1))/5)
adaboost.buildStump(datMat,classLabels,D)
#%%
from machinelearninginaction.Ch07 import adaboost
import imp
imp.reload(adaboost)
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='f:\\adebug.txt',
                    filemode='w')
datMat,classLabels=adaboost.loadSimpData()
adaboost.loadSimpData()
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(np.squeeze(np.array(datMat[:,0]).T).T,np.squeeze(np.array(datMat[:,1]).T),(2+np.array(classLabels))*25,(np.array(classLabels)+2)*25)
D=np.mat(np.ones((5,1))/5)
adaboost.buildStump(datMat,classLabels,D)
#%%
import numpy as np 
import imp
#%%
from machinelearninginaction.Ch07 import adaboost

imp.reload(adaboost)
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='f:\\adebug.txt',
                    filemode='w')
datMat,classLabels=adaboost.loadSimpData()
adaboost.loadSimpData()
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(np.squeeze(np.array(datMat[:,0]).T).T,np.squeeze(np.array(datMat[:,1]).T),(2+np.array(classLabels))*25,(np.array(classLabels)+2)*25)
D=np.mat(np.ones((5,1))/5)
adaboost.buildStump(datMat,classLabels,D)
#[Out]# ({'dim': 0, 'thresh': 1.3, 'ineq': 'lt'}, matrix([[0.2]]), array([[-1.],
#[Out]#         [ 1.],
#[Out]#         [-1.],
#[Out]#         [-1.],
#[Out]#         [ 1.]]))
matplotlib.style.use('dark_background')
import sys
sys.version
#[Out]# '3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)]'
import sys
sys.executable
#[Out]# 'D:\\Program Files\\Python37\\python.exe'
import notebook
notebook.version_info
#[Out]# (5, 7, 8)
#%%
from machinelearninginaction.Ch07 import adaboost

imp.reload(adaboost)
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='f:\\adebug.txt',
                    filemode='w')
datMat,classLabels=adaboost.loadSimpData()
adaboost.loadSimpData()
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(np.squeeze(np.array(datMat[:,0]).T).T,np.squeeze(np.array(datMat[:,1]).T),(2+np.array(classLabels))*25,(np.array(classLabels)+2)*25)
D=np.mat(np.ones((5,1))/5)
adaboost.buildStump(datMat,classLabels,D)
#[Out]# ({'dim': 0, 'thresh': 1.3, 'ineq': 'lt'}, matrix([[0.2]]), array([[-1.],
#[Out]#         [ 1.],
#[Out]#         [-1.],
#[Out]#         [-1.],
#[Out]#         [ 1.]]))
#%%
from machinelearninginaction.Ch07 import adaboost

imp.reload(adaboost)
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='f:\\adebug.txt',
                    filemode='w')
datMat,classLabels=adaboost.loadSimpData()
adaboost.loadSimpData()
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(np.squeeze(np.array(datMat[:,0]).T).T,np.squeeze(np.array(datMat[:,1]).T),(2+np.array(classLabels))*25,(np.array(classLabels)+2)*25)
D=np.mat(np.ones((5,1))/5)
adaboost.buildStump(datMat,classLabels,D)
#[Out]# ({'dim': 0, 'thresh': 1.3, 'ineq': 'lt'}, matrix([[0.2]]), array([[-1.],
#[Out]#         [ 1.],
#[Out]#         [-1.],
#[Out]#         [-1.],
#[Out]#         [ 1.]]))
#%%
from machinelearninginaction.Ch07 import adaboost

imp.reload(adaboost)
import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='f:\\adebug.txt',
                    filemode='w')
datMat,classLabels=adaboost.loadSimpData()
adaboost.loadSimpData()
# fig=plt.figure()
# ax=fig.add_subplot(111)
# ax.scatter(np.squeeze(np.array(datMat[:,0]).T).T,np.squeeze(np.array(datMat[:,1]).T),(2+np.array(classLabels))*25,(np.array(classLabels)+2)*25)
D=np.mat(np.ones((5,1))/5)
adaboost.buildStump(datMat,classLabels,D)
#[Out]# ({'dim': 0, 'thresh': 1.3, 'ineq': 'lt'}, matrix([[0.2]]), array([[-1.],
#[Out]#         [ 1.],
#[Out]#         [-1.],
#[Out]#         [-1.],
#[Out]#         [ 1.]]))
