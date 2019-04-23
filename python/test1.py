
import numpy as np
import matplotlib.pyplot as plt
import os
import sys
sys.path.append('e:\\code\\vsworkspace')
from machinelearninginaction.Ch03 import trees
from machinelearninginaction.Ch03 import treePlotter
from machinelearninginaction.Ch04 import bayes
from machinelearninginaction.Ch05 import logRegres
from machinelearninginaction.Ch08 import regression
import logging

logging.basicConfig(level=logging.DEBUG)
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
def fun2():
    fr=open(os.getcwd()+r"\machinelearninginaction\Ch03\lenses.txt")
    lenses=[inst.strip().split('\t') for inst in fr.readlines()]
    lensesLabels=['age','prescript','astigmatic','tearRate']
    lensesTree=trees.createTree(lenses,lensesLabels)
    treePlotter.createPlot(lensesTree)

def bayTest():
    listOPosts,listClasses = bayes.loadDataSet()
    myVocabList= bayes.createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(bayes.setOfWords2Vec(myVocabList,postinDoc))
        logging.debug(bayes.setOfWords2Vec(myVocabList,postinDoc))
    logging.debug(trainMat)
    logging.debug(trainMat[0])
# bayTest()
#bookmark
def chap05logic():
    dataArr,labelMat=logRegres.loadDataSet()
    m=logRegres.gradAscent(dataArr,labelMat)
chap05logic()

