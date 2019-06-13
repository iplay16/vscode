#include<stdlib.h>
#include<stdio.h>
//int exitnum=20;
void backtrack(int x,int y,char **grid,int gridRowSize,int gridColSize,char **gridcheck,int direct){
/*      0
    3       1
        2
*/
    if(x>=gridRowSize||x<0||y>=gridColSize||y<0)
        return;
    else{
        if(grid[x][y]=='0'||gridcheck[x][y]=='1')//误入水域,或者已经检查过了,则什么也不做,退出(后者不检查会导致无限循环深度优先遍历)
            return;
        //处理,处理很简单,就是check置1
        else{
            //if(exitnum--==0)
            //    exit(1);
            gridcheck[x][y]='1';
            //printf("(x=%d,y=%d)",x,y);
        }
    }
    int from=(direct+2)%4;
    for(int direction=0;direction<4;direction++)//direction是新的要走的方向
        if(direction==from)
            continue;//跳过from的方向,即跳过来的方向
        else
        {   if(direction==0)//往上
                backtrack(x-1,y,grid,gridRowSize,gridColSize,gridcheck,direction);
            if(direction==1)//往右
               backtrack(x,y+1,grid,gridRowSize,gridColSize,gridcheck,direction);
            if(direction==2)//往下
                backtrack(x+1,y,grid,gridRowSize,gridColSize,gridcheck,direction);
            if(direction==3)//往左
                 backtrack(x,y-1,grid,gridRowSize,gridColSize,gridcheck,direction);
        }
        
}


int numIslands(char** grid, int gridRowSize, int gridColSize) {
    char **gridcheck=(char**)malloc(sizeof(char*)*gridRowSize);
    for(int i=0;i<gridRowSize;i++){
        gridcheck[i]=(char*)malloc(sizeof(char)*gridColSize);
        for(int j=0;j<gridColSize;j++){
            gridcheck[i][j]='0';
        }
    }
    int num=0;
    for(int x=0;x<gridRowSize;x++){
        for(int y=0;y<gridColSize;y++){
            if(grid[x][y]==gridcheck[x][y]){
                //因为gridcheck的初始化为0,所以当相同时为水域,不同时为岛屿
                //当遇到岛屿时,就会进入else部分,把岛屿部分置为1
                //这样,某个岛就会只记录一次
                continue;
            }else{
                backtrack(x,y,grid,gridRowSize,gridColSize,gridcheck,1);//从左往右扫,所以是往右方向
                num++;
            }
        }
    }
    for(int i=0;i<gridRowSize;i++){
        free(gridcheck[i]);
    }
    free(gridcheck);
    return num;
}

int test_numIslands(){
    int row=4,col=5,num=0;
    char **grid=(char**)malloc(sizeof(char*)*row);
    for(int i=0;i<row;i++){
        grid[i]=(char*)malloc(sizeof(char)*col);
        for(int j=0;j<col;j++)
            scanf("%c",&grid[i][j]);
    }
    printf("\n---------------------------------\n");
    for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            printf("%c",grid[i][j]);
        }
    }
    num=numIslands(grid,row,col);
    printf("\nnum=%d",num);
}

int main(){
    test_numIslands();
}

