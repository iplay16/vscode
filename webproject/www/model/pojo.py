#!python

class resultStatus(dict):
    
    def __init__(self,result):
        self['result']=result

class User:

    def  __init__(self,username,password):
       self.username=username
       self.password=password
    

