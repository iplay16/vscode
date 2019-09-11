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


#%%
c=(34>>4)
print(c)