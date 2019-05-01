#### runmatlab
matlab -nosplash -nodesktop -sd e:\code\vsworkspace -r "run('e:\code\vsworkspace\matlab\test.m');"
#### settings.json
%APPDATA%\Code\User\settings.json

it is also needed to backup

#### showmdfile
crl+shit+v

#### python2to3
python "D:\Program Files\Python37\Tools\Scripts\2to3.py" -w E:\code\vsworkspace\

#### quickopen
ctrl+p

#### md5
CertUtil -hashfile C:\xxx.tar MD5

##### vscode插件推荐
AREPL
bookmark
gitignore
todo hilight
faker

##### array升维降维
升维 reshape


降维 squeeze
另外，reshape(-1)也可以“拉平”多维数组


##### python 与jupyter的debug

对于jupyter,目前也需要用python的debug方式

使用pdb,插入set_trace(),即可交互式方式debug
ipdb似乎也一样,目前还没细看


##### 文件读取
C语言 fread()与fwrite()函数说明与示例
1.作用

　　读写文件数据块。

2.函数原型

　　(1)size_t fread ( void * ptr, size_t size, size_t count, FILE * stream );

　　　　　其中，ptr：指向保存结果的指针；size：每个数据类型的大小；count：数据的个数；stream：文件指针

　　　　　函数返回读取数据的个数。

　　(2)size_t fwrite ( const void * ptr, size_t size, size_t count, FILE * stream );

　　　　   其中，ptr：指向保存数据的指针；size：每个数据类型的大小；count：数据的个数；stream：文件指针

　　　　　函数返回写入数据的个数。

3.注意

　　(1)写操作fwrite()后必须关闭流fclose()。

　　(2)不关闭流的情况下，每次读或写数据后，文件指针都会指向下一个待写或者读数据位置的指针。

4.读写常用类型

　　(1)写int数据到文件
```
#include <stdio.h>
#include <stdlib.h>
int main ()
{
  FILE * pFile;
  int buffer[] = {1, 2, 3, 4};
  if((pFile = fopen ("myfile.txt", "wb"))==NULL)
  {
      printf("cant open the file");
      exit(0);
  }
  //可以写多个连续的数据(这里一次写4个)
  fwrite (buffer , sizeof(int), 4, pFile);
  fclose (pFile);
  return 0;
}
```

(2)读取int数据
```
#include <stdio.h>
#include <stdlib.h>

int main () {
    FILE * fp;
    int buffer[4];
    if((fp=fopen("myfile.txt","rb"))==NULL)
    {
      printf("cant open the file");
      exit(0);
    }
    if(fread(buffer,sizeof(int),4,fp)!=4)   //可以一次读取
    {
        printf("file read error\n");
        exit(0);
    }

    for(int i=0;i<4;i++)
        printf("%d\n",buffer[i]);
    return 0;
}
```

5.读写结构体数据

　　(1)写结构体数据到文件
```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct{
    int age;
    char name[30];
}people;

int main ()
{
    FILE * pFile;
    int i;
    people per[3];
    per[0].age=20;strcpy(per[0].name,"li");
    per[1].age=18;strcpy(per[1].name,"wang");
    per[2].age=21;strcpy(per[2].name,"zhang");

    if((pFile = fopen ("myfile.txt", "wb"))==NULL)
    {
        printf("cant open the file");
        exit(0);
    }

    for(i=0;i<3;i++)
    {
        if(fwrite(&per[i],sizeof(people),1,pFile)!=1)
            printf("file write error\n");
    }
    fclose (pFile);
    return 0;
}
```

　(2)读结构体数据
```
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
typedef struct{
    int age;
    char name[30];
}people;

int main () {
    FILE * fp;
    people per;
    if((fp=fopen("myfile.txt","rb"))==NULL)
    {
      printf("cant open the file");
      exit(0);
    }

    while(fread(&per,sizeof(people),1,fp)==1)   //如果读到数据，就显示；否则退出
    {
        printf("%d %s\n",per.age,per.name);
    }
    return 0;
}
```


#####使用notepad实现python2to3
cmd /k python "D:\Program Files\Python37\Tools\Scripts\2to3.py" -w "$(FULL_CURRENT_PATH)" & PAUSE & EXIT

##### 动态页面类型
网页:https://blog.51cto.com/andyxu/2306579
```
1、mod_php
即模块的方式，把php服务做为模块来进行调用，模块将相关函数嵌入web服务请求处理流程，不需要额外的解释器进程。例如apache的libphp5.so模块，注意libphp5.so是php提供的，不是apache自带的。
下面是apache配置文件里php模块的配置内容

DirectoryIndex index.php index.html index.html.var
LoadModule php5_module modules/libphp5.so
<IfModule mime_module>
AddType application/x-httpd-php .php
AddType applicaiton/x-httpd-php-source .phps
简单来讲，就是apache将php做为自己的一个模块来使用。
2、CGI
这个模式很少人使用，因为每次调用它都需要fork一个解释器进程来执行php脚本，执行结束后进程随之退出。一个请求就需要fork一个进程，周而复始，效率低下不说，还大量消耗服务器资源。
下面是apache关于CGI的配置
配置文件里启用CGI模式

#LoadModule php5_module modules/libphp5.so
Action application/x-httpd-php /cgi-bin/php-cgi
然后将CGI脚本文件拷贝到apache的cgi-bin目录下
cp /usr/bin/php-cgi /var/www/cgi-bin/
3、FastCGI
FastCGI模式是指由单独的进程管理器如php-fpm启动并管理多个解释器进程，web服务器只需将脚本传给php-fpm执行即可。执行完毕后解释器进程不会退出，而是等待下一个请求。这种方式既适用于本地部署，也适用于分布式架构，并且多个进程并行处理，不仅配置灵活，而且效率高。
以下是nginx配置文件里关于FastCGI的配置内容

location ~ \.php$ {
    root           html;
    fastcgi_pass   127.0.0.1:9000;
    fastcgi_index  index.php;
    fastcgi_param  SCRIPT_FILENAME  $document_root$fastcgi_script_name;
    include        fastcgi_params;
}
4、简单总结
假设web服务器是一家公司，那么mod_php方式就如同php是它的一个部门，关于php的问题这个部门可以直接处理；CGI模式相当于公司没有专门处理php问题的部门，遇到php相关的事情需要处理，就临时拉人成立一个工作小组，问题解决后这个临时小组也就解散了；FastCGI模式相当于公司之间的合作，web和php分别是两家公司，web公司将php业务外包给php公司负责。
说了这么多，那到底在动态页面处理方面，apache好还是nginx好呢？
其实无论是mod_php、还是FastCGI，都有其自己的优势。以前在FastCGI技术还不成熟的时候，自然是mod_php稳定、处理速度更快一些，可是社会是不断在向前进步的，现如今FastCGI技术已经非常成熟了，网上也有很多人做了相关的测试，说是FastCGI比mod_php更稳定、速度更快。我个人认为，如果是单机部署的话，可考虑使用mod_php方式，因为毕竟多启一个进程对系统而言就多了一些资源消耗；如果分开部署的话，可考虑使用FastCGI，现在越来越多的人使用nginx+php架构了。
```


#### python json
dumps 方法:把dic对象转换为json对象
load方法:把str对象转换为dic对象

对于json要传输正确的json,如果拿到一个object,需要把它转为dic,再用dump方法
如果拿到str对象,如果str完全符合json格式,则直接传输;如果str不完全符合标准,则可能会传输出错,所以比较通用的做法是先用loads转为dic或者list,再取出dic对象dumps为json对象再传输,这样可以在传输之前就报错,便于排查故障

##### logging的使用

https://blog.csdn.net/hunt_ing/article/details/82080923
https://blog.csdn.net/sunwukong_hadoop/article/details/80092009

```
import logging
import datetime
import sys

logger = logging.getLogger('mylogger')
logger.setLevel(logging.INFO)
rf_handler = logging.StreamHandler(sys.stderr)#默认是sys.stderr
rf_handler.setLevel(logging.DEBUG) 
#rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(name)s - %(message)s"))
 
f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))
 
logger.addHandler(rf_handler)
logger.addHandler(f_handler)
 
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
```


##### ajax表单提交
https://blog.csdn.net/guo147369/article/details/78928898
https://www.jianshu.com/p/10cdbb35ac87
```
 $.ajax({
            url:'/pythoncgi/increaseuser.py',
            type:'post',
            contentType :"application/x-www-form-urlencoded; charset=utf-8",
            data:$("#formofincreaseuser").serialize(),
            //    data:JSON.stringify({                    
            //    a: parseInt($('input[name="username"]').val()),  
            //    b: parseInt($('input[name="password"]').val())
            //}), 
            dataType:'text',
            success:function(data){
                alert(data['result']);
            },
            error:function(data){
                alert(data.status+"error");
            }
        });
```