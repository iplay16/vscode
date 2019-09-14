##############################
#
#       by linxiaowei
#       2019/09/10    
# 
# there are several important matrixs or vectors
# meanmatrix:the matrix of meanpoint
# clusterv:a vector that contain the n'th point that assign to the certain meanpoint 
#
#
#
##############################
import sys
import random
import numpy as np
from matplotlib import pyplot as plt
def kmeans(datamatrix,k):
    #init meanmatrix
    shape=datamatrix.shape
    m=shape[0]
    n=shape[1]
    meanmatrix=np.zeros([k,n])
    #klist store the random number
    klist=[]
    while(len(klist)!=k):
        tmp=random.randint(0,m-1)
        if tmp not in klist:
            klist.append(tmp)
    for i,x in enumerate(klist):
        meanmatrix[i]=datamatrix[x]
    
    #0 is unchanged
    flag=1
    clusterv=[-1]*m
    # while(flag!=0):
    for _ in range(500):
        #count distance and distribute cluster,clusterv was built
        flag=countclusterv(datamatrix,meanmatrix,clusterv)
        #count mean
        meanmatrix=countmean(datamatrix,clusterv,meanmatrix)
    return meanmatrix,clusterv

def distance(av,bv):
    return (np.sum((av-bv)**2))**(1/2)

#datamatrix and clusterv has the same line number
def countmean(datamatrix,clusterv,meanmatrix):
    #clean meanmatrix
    for i in range(meanmatrix.shape[0]):
	    for j in range(meanmatrix.shape[1]):
		    meanmatrix[i,j]=0
    k=len(meanmatrix)
    m=len(clusterv)
    clustercount=[0]*len(meanmatrix)
    for i in range(m):
        c=clusterv[i]
        meanmatrix[c]+=datamatrix[i]
        clustercount[c]+=1
    countv=np.asarray(clustercount).reshape(k,1)
    return meanmatrix/countv

def countclusterv(datamatrix,meanmatrix,clusterv):
    m=len(datamatrix)
    k=len(meanmatrix)
    flag=0
    for i in range(m):
        shortestd=sys.maxsize
        c=-1
        for j in range(k):
            tmp=distance(datamatrix[i],meanmatrix[j])
            if tmp<shortestd:
                shortestd=tmp
                c=j
        if clusterv[i]!=c:
            clusterv[i]=c
            flag=1
    return flag

def loadDataSet(fileName):      #general function to parse tab -delimited floats
    dataMat = []                #assume last column is target value
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        dataMat.append(curLine)
    return np.asarray(dataMat,dtype=float)

if __name__=='__main__':
    datamatrix=loadDataSet('ML/testSet.txt')
    meanmatrix,clusterv=kmeans(datamatrix,4)
    # x=datamatrix[:,0]
    # y=datamatrix[:,1]
    for m in range(len(clusterv)):
        if clusterv[m]==0:
            plt.plot(datamatrix[m:,0],datamatrix[m:,1],"om")
        if clusterv[m]==1:
            plt.plot(datamatrix[m:,0],datamatrix[m:,1],"ob")
        if clusterv[m]==2:
            plt.plot(datamatrix[m:,0],datamatrix[m:,1],"oy")
        if clusterv[m]==3:
            plt.plot(datamatrix[m:,0],datamatrix[m:,1],"og")
    print(meanmatrix)
    x=meanmatrix[:,0]
    y=meanmatrix[:,1]
    plt.plot(x,y,"or")
    plt.show()
