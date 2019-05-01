#%%
import json
 
#python字典类型转换为json对象
data = {
    'id' : 1,
    'name' : 'test1',
    'age' : '1'
}
data2 = [{
    'id' : 1,
    'name' : 'test1',
    'age' : '1'
},{
    'id' : 2,
    'name' : 'test2',
    'age' : '2'
}]

for d in data2:
	for x in d:
		print(x)