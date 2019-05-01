
#%%
from sklearn import datasets
import numpy as np
import random
import numpy as np 
import imp
import matplotlib.pyplot as plt
import logging
import sys
sys.path.append('e:\\code\\vsworkspace')
from machinelearninginaction.Ch07 import adaboost
import os
logging.basicConfig(level=logging.DEBUG,
                    filename='f:\\adebug.txt',
                    filemode='w')

#%% main source

imp.reload(adaboost)
datArr,labelArr=adaboost.loadDataSet(os.getcwd()+'\\machinelearninginaction\\Ch07'+'\\horseColicTraining2.txt')
classifierArr,agg=adaboost.adaBoostTrainDS(datArr,labelArr,10)
testArr,testLabelArr=adaboost.loadDataSet(os.getcwd()+'\\machinelearninginaction\\Ch07'+'\\horseColicTest2.txt')
prediction10=adaboost.adaClassify(testArr,classifierArr)
errArr=np.mat(np.ones((67,1)))
errArr[prediction10!=np.mat(testLabelArr).T].sum()
quit()

#%% data
testArr,testLabelArr=adaboost.loadDataSet(os.getcwd()+'\\machinelearninginaction\\Ch07'+'\\horseColicTest2.txt')
testArr=np.array(testArr)
np.savetxt('f:\\data.txt',testArr,fmt='%.6f')