git在push/push to时需要使用到user.name和user.email，一般通过git bash来进行配置或修改。

#### 查看user.name/user.email
```
查看user.name
git config user.name

查看user.email
git config user.email
```
#### 配置user.name/user.email
```
配置"user.name"
git config --global user.name "your user name"

配置user.email
git config --global user.email "your user email"
```
> 这里需要注意的是，该命令只能用于初次配置user.name/email，如果不小心配置错误，或者重复配置，不可以通过重复执行以上命令来修改user.name/email，否则可能或报错说无法重复配置，或者导致一个key配置了多个value。

#### 修改user.name/user.email
如果想要修改已经配置过的user.name或email，有两种方式，一种是通过git bash来修改；一种是直接修改.gitconfig文件。
```
1. git bash
修改user.name
git config --global --replace-all user.name "your user name"

修改user.email
git config --global --replace-all user.email"your user email"

2. 修改.gitconfig文件
该文件是隐藏文件，位于C:\Users\{user}\.gitconfig，直接修改里边的name或者email，如果有重复的name或email，可以将其删掉，只剩下一个就好。
修改完，通过git bash输入git config –list可以查看是否修改成功了。
```
————————————————
版权声明：本文为CSDN博主「雨临Lewis」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/lewky_liu/article/details/78708589