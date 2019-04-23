import os
import sys

sys.path.append('e:\\code\\vsworkspace')
MLpath='E:\\code\\vsworkspace\\machinelearninginaction'
from machinelearninginaction.Ch08 import regression
import numpy as np 
def regressionTest():
    xArr,yArr=regression.loadDataSet(MLpath+'\\Ch08\\ex0.txt')
    ws=regression.standRegres(xArr,yArr)



