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
a = np.arange(9, dtype = np.float_).reshape(3,3)  
print ('第一个数组：')
print (a)
print ('\n')
print ('第二个数组：')
b = np.array([10,10,10])  
print (b)
print ('\n')
print ('两个数组相加：')
print (np.add(a,b))
print ('\n')
print ('两个数组相减：')
print (np.subtract(a,b))
print ('\n')
print ('两个数组相乘：')
print (np.multiply(a,b))
print ('\n')
print ('两个数组相除：')
print (np.divide(a,b))
print(a)