#!python
# -*- coding: UTF-8 -*-
#%%
import pymysql
import pymysql.cursors
import mylogger
from pojo import resultStatus
from pojo import User

def getconnection():
    # try:
    # with pymysql.Connect(host="127.0.0.1",user='root', password='root123', db="herogame",charset="utf8mb4") as conn:
    #         print(type(conn))
    #         return conn
    # except:
    #     return 
    try:
        conn=pymysql.Connect(host="127.0.0.1",user='root', password='root123', db="herogame",charset="utf8mb4")
        if(not conn):
            mylogger.debug("connect failed")
            print("connect failed,quit()")
            quit()
        else:
            return conn
    except:
        print("connect failed,quit()")
        quit()        
        # return
    
def fetchuserlist():
    conn=getconnection()
    try:
        c=conn.cursor()
        c.execute("select * from usertableofheros")
        value=c.fetchall()
        return value
    except BaseException:
        conn.rollback()
        mylogger.debug(BaseException+"Error happenedd")
    finally:
        conn.close()

def adduser(user):
    username=user.username
    password=user.password
    if(len(username)==0 or len(password)==0):
        return resultStatus("length of string is zero")
    if(username is None or password is None):
        return resultStatus("None data")
    conn=getconnection()
    try:
        c=conn.cursor()
        c.execute('insert into usertableofheros (username,password) values(%s,%s)',(username,password))
        conn.commit()
        return resultStatus("insert success")
    except:
        mylogger.debug(BaseException)
        conn.rollback()
        return resultStatus("error happened")
    finally:
        conn.close()

def updateWeapon(weaponid):
    conn=getconnection()
    try:
        c=conn.cursor()
        c.execute('update weapontable set val=val+20 where weaponid=%s',(weaponid))
        conn.commit()
        return resultStatus("update success")
    except:
        conn.rollback()
        mylogger.debug("update error")
        return resultStatus("update error")
    finally:
        conn.close()

if __name__ == '__main__':
    adduser(User("nammmmmmmmm","234325"))
