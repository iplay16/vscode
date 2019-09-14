##############################
#
#       by linxiaowei
#       2019/09/13   
# 
# there are several important matrixs ,vectors or data structures
#
# columnmap:contain a column's property values
# 
# reference:https://www.jianshu.com/p/60f875cf0e8e
##############################
from math import log
import numpy as np
def countcolumnmap(column,classresult):
    columnmap={}
    for i,x in enumerate(column):
        if x not in columnmap:
            columnmap[x]=[0,0,-1]
        if classresult[i]==Truevalue():
            columnmap[x][0]+=1  
        else:
            columnmap[x][1]+=1
    #count every ent
    for x in columnmap:
        p1=columnmap[x][0]/(columnmap[x][0]+columnmap[x][1])
        p2=columnmap[x][1]/(columnmap[x][0]+columnmap[x][1])
        columnmap[x][2]=ent([p1,p2])
    return columnmap

def countbaseent(classresult):
    rightnum=0
    for x in classresult:
        if x==Truevalue():
            rightnum+=1
    wrongnum=len(classresult)-rightnum
    p1=rightnum/(wrongnum+rightnum)
    p2=wrongnum/(wrongnum+rightnum)
    return ent([p1,p2])

def countgrain(totalnum,columnmap,classresult):
    #count total ent
    baseentry=countbaseent(classresult)
    sum=0
    for x in columnmap:
        sum+=(columnmap[x][0]+columnmap[x][1])/totalnum*columnmap[x][2]
    return baseentry-sum

def ent(pv):
    sum=0
    for x in pv:
        if x==0:
            continue
        sum+=-x*log(x,2)
    return sum

def Truevalue():
    return '是'

from pandas import Series,DataFrame,read_csv
if __name__=='__main__':
    datatable=read_csv('ML/watermelonSet.txt')
    ##删除A列，不改变原来的data数据，返回删除后的新表data_2。axis为1表示删除列，0表示删除行。inplace为True表示直接对原表修改。
    datatable.drop('编号',axis=1,inplace=True)
    (rown,coln)=datatable.shape
    lastcol=datatable.iloc[:,-1]
    baseent=countbaseent(lastcol)
    print(baseent)
    print('----------')
    columnmap=None
    totalrow=rown
    tablemap={}
    for i in range(0,5):
        columnmap=countcolumnmap(datatable.iloc[:,i],lastcol)
        print(columnmap)
        propertytag=list(datatable)[i]
        tablemap[propertytag]=countgrain(rown,columnmap,lastcol)
        print(propertytag,':',tablemap[propertytag])
        print('-----------------')
    print(tablemap)