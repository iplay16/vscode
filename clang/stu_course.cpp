/*
Sample Input:
10 5
ZOE1 2 4 5
ANN0 3 5 2 1
BOB5 5 3 4 2 1 5
JOE4 1 2
JAY9 4 1 2 5 4
FRA8 3 4 2 5
DON2 2 4 5
AMY7 1 5
KAT3 3 5 4 2
LOR6 4 2 4 1 5
*/

/*

Sample Output:
1 4
ANN0
BOB5
JAY9
LOR6
2 7
ANN0
BOB5
FRA8
JAY9
JOE4
KAT3
LOR6
3 1
BOB5
4 7
BOB5
DON2
FRA8
JAY9
KAT3
LOR6
ZOE1
5 9
AMY7
ANN0
BOB5
DON2
FRA8
JAY9
KAT3
LOR6
ZOE1

*/
#include<stdlib.h>
#include<stdio.h>
typedef struct stu_course{
  char *name;
  int coursesize;
  int *course;
}stu_course;

int main(){
  stu_course *sc=NULL;
  int stunum=0,coursenum=0;
  scanf("%d%d",&stunum,&coursenum);
  sc=(stu_course*)malloc(sizeof(stu_course)*100);
  for(int i=0;i<stunum;i++){
    sc[i].name=(char*)malloc(sizeof(char)*20);
    sc[i].course=(int*)malloc(sizeof(int)*coursenum);
  }

  for(int i=0;i<stunum;i++){
     scanf("%s %d",sc[i].name,&(sc[i].coursesize));
     for(int j=0;j<sc[i].coursesize;j++){
         if(scanf("%d",&sc[i].course[j]))//PTA平台不处理scanf的返回值会产生告警
                ;
     }

  }
    int *count=(int*)malloc(sizeof(int)*stunum);
    for(int i=0;i<stunum;i++){
        count[i]=0;
    }
  for(int coursetype=1;coursetype<=coursenum;coursetype++){
    for(int i=0;i<stunum;i++){
        for(int j=0;j<sc[i].coursesize;j++){
            if(sc[i].course[j]==coursetype){
                count[coursetype-1]++;
            }
        }
    }
  }

for(int coursetype=1;coursetype<=coursenum;coursetype++){
    printf("%d %d\n",coursetype,count[coursetype-1]);
    for(int i=0;i<stunum;i++){
        for(int j=0;j<sc[i].coursesize;j++){
            if(sc[i].course[j]==coursetype){
               printf("%s\n",sc[i].name);
            }
        }
    }
  }
  exit(0);
}


// char s[5];
// int x;
// scanf("%s%d",s,&x);
// printf("%s %d",s,x);

// for(int i=0;i<10;i++){
//     printf("%s\n",sc[i].name);
// }
 //printf("%s %d %d %d",sc[0].name,sc[0].coursesize,sc[0].course[0],sc[0].course[1]);

/*
//sort(sc,sc+10,cmp);
bool cmp(stu_course t1,stu_course t2)
{
    if(t1.coursesize>t2.coursesize)
        return true;
    return false;
}
*/
