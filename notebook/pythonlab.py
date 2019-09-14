#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os
a=2
b=3
type(id(a))


#%%
def hashcode(h):
	return id(h)

def hashv(obj):
	if not obj:
		return 0
	h=hashcode(obj)
	return h^(h>>16)

def indexFor(hashval,length):
	return  (hashval & (length-1))
	

#%%
a=[4,7,9,234,6]
li=[None]*10
for x in a:
	# print(hash(x))
	print(indexFor(hash(x),10))


#%%
print('hello')

#%%
import numpy as np 
a = np.array([[1],[2],[3]])  
print(2**a)
print(a[2])
b=np.empty([3,4], dtype = float)
c=np.array([[1,2,3],[4,5,6]])
for x in c:
	print(x)
#%%
import numpy as np 
 
a = np.array([[1,2,3],[3,4,5]])  
b=np.array([99,100])
a[:,0]=b
print(a)

#%%
import numpy as np 
datamatrix=np.array([[1,2,3],[3,4,5]])
c=datamatrix/np.asarray([2,3]).reshape(2,1)
print(c)
#%%
from math import *
d=9/17
a=-d*log(d,2)
a

#%%
def afun(a,b):
	def bfun(x):
		return a+b+x
	return bfun

bf=afun(2,3)
bf(5)
#%%
import numpy as np
a=np.asarray([1,2,3])*np.asarray([4,5,6])
sum(a)
# list(a)

#%%
from math import log,exp
import numpy as np
np.power(exp(1),np.asarray([3,4,5,7]))
