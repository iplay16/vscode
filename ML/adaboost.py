
#good article https://www.cnblogs.com/ScorpioLu/p/8295990.html
from math import log,exp
import numpy as np
def alphaweight(err):
    return 1/2*log((1-err)/err)

#X is a vector
def baseclassfier(threshold,X):
    res=[0]*len(X)
    for i,x in enumerate(X):
        if x<threshold:
            res[i]=1
        else:
            res[i]=-1
    return res

def generateclassfier(Dweightv,sampleres):
    length=len(Dweightv)
    bestwrongrate=1
    threshold=0
    for i in range(length):
        wrongrate=0
        for j in range(i):
            if sampleres[j]==-1:
                wrongrate+=Dweightv[j]
        for k in range(i,length):
            if sampleres[k]==1:
                wrongrate+=Dweightv[k]
        if wrongrate<bestwrongrate:
            bestwrongrate=wrongrate
            threshold=i
    return threshold,bestwrongrate

def updateDweight(Dweightv,alpha,sampleresv,threshold):
    v1=np.asarray(baseclassfier(threshold,X))
    v2=-alpha*np.asarray(sampleresv)*v1
    Dweightv=np.asarray(Dweightv)*np.power(exp(1),v2)
    Dweightv=Dweightv/sum(Dweightv)
    return Dweightv

def sign(X):
    res=[0]*len(X)
    for i,x in enumerate(X):
        if x>=0:
            res[i]=1
        else:
            res[i]=-1
    return res
    
def H(X,alphaweightv,classfier):
    hv=[0]*len(X)
    for i,c in enumerate(classfier):
        hv+=alphaweightv[i]*np.asarray(baseclassfier(c,X))
    res=sign(hv)
    return res

if __name__ == "__main__":
    X = [0, 1, 2, 3, 4, 5,6,7,8,9]
    Y = [-1, 1, 1, 1, -1, 1,1,1,-1,1]
    classfier=[]
    alphaweightv=[]
    Dweightv=[1/len(X)]*len(X)
    for t in range(10):
        threshold,err=generateclassfier(Dweightv,Y)
        # if err>0.5: break
        alpha=alphaweight(err)
        Dweightv=updateDweight(Dweightv,alpha,Y,threshold)
        classfier.append(threshold)
        alphaweightv.append(alpha)
    l=H(X,alphaweightv,classfier)
    print(l)