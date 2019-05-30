#!python
# -*- coding: UTF-8 -*-
#%%
import sys
# sys.path.append('f:\\pythoncgi')
import dbUtil
import json
from pojo import User
userlist=dbUtil.fetchuserlist()
ju=json.dumps(userlist)
print('Content-type:json')
print()
print(ju)
