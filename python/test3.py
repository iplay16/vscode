import sys
sys.path.append('e:\\code\\vsworkspace')
from machinelearninginaction.Ch05 import logRegres
dataArr,labelMat=logRegres.loadDataSet()
w=logRegres.gradAscent(dataArr,labelMat)
print(w)