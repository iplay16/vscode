#!python
# -*- coding: UTF-8 -*-
#%%

import cgi, cgitb 
import json
import dbUtil
from pojo import User
# 创建 FieldStorage 的实例化
import mylogger
# 获取数据
cgitb.enable(display=0, logdir="f:\logdir")
form = cgi.FieldStorage() 
username = form.getvalue("username")
password = form.getvalue("password")
mylogger.debug(username)
mylogger.debug(password)
try:
    result=dbUtil.adduser(User(username,password))
    jsonobject=json.dumps(result)
    print("Content-type:json")
    print()
    print(jsonobject)
except BaseException:
    mylogger.debug("service throw excepttion"+result)
finally:
    pass
