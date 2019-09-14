##############################
#
#       by linxiaowei
#       2019/09/10    
# 
##############################
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
    distancematrix=np.zeros([m,k])
    while(flag!=0):
        ####build distancematrix
        for i,line in enumerate(meanmatrix):
            tmp=(((datamatrix-line)**2).sum(axis=1))**(1/2)
            distancematrix[:,i]=tmp

        #build clusterv
        flag=buildclusterv(distancematrix,clusterv)

        #first,clean meanmatrix
        for i in range(k-1):
            for j in range(n-1):
                meanmatrix[i,j]=0
        
        #clusternumberv is the Statistics of clusterv
        clusternumberv=np.zeros(k,int)
        for x in clusterv:
            clusternumberv[x]+=1
        
        #build meanmatrix
        for i,x in enumerate(clusterv):
            meanmatrix[x]+=datamatrix[i]
        meanmatrix=meanmatrix/(clusternumberv.reshape([k,1]))
        return meanmatrix

def buildclusterv(distancematrix,clusterv):
    flag=0
    num=0
    for n,line in enumerate(distancematrix):
        num=0
        shortestd=line[0]
        for i,distance in enumerate(line):
            if distance<shortestd:
                shortestd=distance
                num=i
        if clusterv[n]!=num:
            flag=1
            clusterv[n]=num
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
    x=datamatrix[:,0]
    y=datamatrix[:,1]
    plt.plot(x,y,"ob")
    res=kmeans(datamatrix,4)
    x=res[:,0]
    y=res[:,1]
    plt.plot(x,y,"or")
    print(res)
    plt.show()
