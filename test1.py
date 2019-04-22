
import numpy as np
import matplotlib.pyplot as plt
import os
from machinelearninginaction.Ch03 import trees
from machinelearninginaction.Ch03 import treePlotter
def fun1():    
    # filename=os.getcwd()+r"\machinelearninginaction\Ch02\datingTestSet2.txt"
    # fr = open(filename)
    # b=fr.readlines()
    # print(b)
    myDat,labels=trees.createDataSet()
    mytree=trees.createTree(myDat,labels)
    print(mytree)
    treePlotter.createPlot(mytree)

    # filename=os.getcwd()+r"\machinelearninginaction\Ch02\datingTestSet2.txt"

fr=open(os.getcwd()+r"\machinelearninginaction\Ch03\lenses.txt")
lenses=[inst.strip().split('\t') for inst in fr.readlines()]
lensesLabels=['age','prescript','astigmatic','tearRate']
lensesTree=trees.createTree(lenses,lensesLabels)
treePlotter.createPlot(lensesTree)