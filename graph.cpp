#include<vector>
#include<new>
#include<stdio.h>
#include<stdlib.h>
#include<list>
#include<queue>
#include<set>
using namespace std;

typedef struct AdjMatrix{
    int cost;
}AdjMatrix;

typedef struct GeneralEdge{
    int fromvertex;
    int tovertex;
    int cost;
}GeneralEdge;

typedef struct Edge{
    int nextNode;
    int cost;
}Edge;

int Tree[10];
int findRoot(int x){
    if(Tree[x]==-1) 
        return x;
    else {
        int root=findRoot(Tree[x]);
        Tree[x]=root; //x直接指向根
        return root;
    }
}

typedef  struct adjGraph{
    vector<Edge*> *vertexnode;//顶点数组
    int vertexnum;
}adjGraph;

Edge *createEdge(int nextNode,int cost){
    Edge *newedge=(Edge*)malloc(sizeof(Edge));
    newedge->nextNode=nextNode;
    newedge->cost=cost;
    return newedge;
}

adjGraph *createAdjGraph(int vertexnum){
    adjGraph *g=(adjGraph*)malloc(sizeof(adjGraph));
    g->vertexnum=vertexnum;
    //初始化顶点数组
    g->vertexnode=new vector<Edge*>[g->vertexnum];
    return g;
}

void GraphDFS(adjGraph *g,int x,int *visted){
    if(visted[x]==1)
            return;
    else{
        //visit()
        printf("vist %d\n",x);
        visted[x]=1;
        for(int i=0;i<(g->vertexnode[x].size());i++){//遍历第x个节点的edge,从vertexnode[x][0]到vertexnode[x][size-1]
            GraphDFS(g,g->vertexnode[x][i]->nextNode,visted);//深度优先遍历
        }
    }
}

void GraphDFSTraverse(){
    int vertexnum=0;
    printf("input vertexnum:");
    scanf("%d",&vertexnum);
    adjGraph *g=createAdjGraph(vertexnum);
    int fromvertex=-1,tovertex=-1,inputcost=-1;
    printf("input edges,format is:fromvertex tovertex cost\n");
    while(scanf("%d%d%d",&fromvertex,&tovertex,&inputcost)!=EOF){
        g->vertexnode[fromvertex].push_back(createEdge(tovertex,inputcost));
    }
    for(int i=0;i<g->vertexnum;i++){
        printf("%d",i);
        for(int j=0;j<g->vertexnode[i].size();j++){
            printf("--->(cost:%d,nextvertex:%d)",g->vertexnode[i][j]->cost,g->vertexnode[i][j]->nextNode);
        }
        printf("\n");
    }
    int visted[10]={0};
    for(int t=0;t<g->vertexnum;t++){//
        if(visted[t]==0)
            GraphDFS(g,t,visted);//从0节点开始深度优先遍历
    }
    // //创建节点
    // g->vertexnode[0].push_back(createEdge(1,6));
    // printf("%d",g->vertexnode[0][0]->cost);
}

/*
测试数据,cost都等于1即可,即最后一个数字等于1
input Sample:
4
0 1 1
0 2 1
1 3 1
0 4 1
^z(ctrl+z)


Output Sample:

GraphDFSTraverse:
vist 0
vist 1
vist 3
vist 2
vist 4

如果是广度优先则会是:
BFS
visit 1
visit 2
visit 4
visit 3

*/

void GraphBFS(adjGraph *g){
    queue<int> nodequeue;
    int visited[10]={0};
    int p;
    printf("BFS\n");
    for(int t=0;t<g->vertexnum;t++){//从第x个节点开始广度遍历
        if(visited[t]==0){
            visited[t]=1;
            printf("visit %d\n",t);
            nodequeue.push(t);
            while(!nodequeue.empty()){
                p=nodequeue.front();
                nodequeue.pop();
                for(int i=0;i<g->vertexnode[p].size();i++){
                    int nextnode=g->vertexnode[p][i]->nextNode;
                    if(visited[nextnode]==0){
                        printf("visit %d\n",nextnode);
                        visited[nextnode]=1;
                        nodequeue.push(nextnode);
                    }
                }
            }
        }
    }
}

void GraphBFSTaverse(){
        int vertexnum=0;
    printf("input vertexnum:");
    scanf("%d",&vertexnum);
    adjGraph *g=createAdjGraph(vertexnum);
    int fromvertex=-1,tovertex=-1,inputcost=-1;
    printf("input edges,format is:fromvertex tovertex cost\n");
    while(scanf("%d%d%d",&fromvertex,&tovertex,&inputcost)!=EOF){
        g->vertexnode[fromvertex].push_back(createEdge(tovertex,inputcost));
    }
    for(int i=0;i<g->vertexnum;i++){
        printf("%d",i);
        for(int j=0;j<g->vertexnode[i].size();j++){
            printf("--->(cost:%d,nextvertex:%d)",g->vertexnode[i][j]->cost,g->vertexnode[i][j]->nextNode);
        }
        printf("\n");
    }
    GraphBFS(g);
}

void shortestDistance(){
    int vertexnum=0;
    printf("input vertexnum:");
    scanf("%d",&vertexnum);
    int fromvertex=-1,tovertex=-1,inputcost=-1;
    AdjMatrix m[7][7];
    //初始化距离无穷大
    for(int i=0;i<vertexnum;i++){
        for(int j=0;j<vertexnum;j++){
            m[i][j].cost=-1;
        }
    }
    printf("input edges,format is:fromvertex tovertex cost\n");
    while(scanf("%d%d%d",&fromvertex,&tovertex,&inputcost)!=EOF){
        m[fromvertex][tovertex].cost=inputcost;
    }

    for(int i=0;i<vertexnum;i++){//打印矩阵
        printf("\n");
        for(int j=0;j<vertexnum;j++){
            printf("%d ",m[i][j].cost);
        }
    }

    int vset[10]={0};//0代表该顶点未加入,1代表该顶点已加入
    int vx;
    int tempdistance;
    int v0distance[7]={-1};
    v0distance[0]=0;
    for(int i=1;i<vertexnum;i++){
        v0distance[i]=m[0][i].cost;
    }
    //贪心算法加入顶点
    for(int i=1;i<vertexnum;i++){//i表示躺数,并未在for循环里面用到
        //debug
        for(int u=0;u<vertexnum;u++){
            printf("v%d=%d,",u,v0distance[u]);
        }
        printf("\n");
        for(int j=1,min=1000;j<vertexnum;j++){//从v0distance中选出最小距离的顶点和最小距离
            if(v0distance[j]==-1||vset[j]==1)//跳过无穷大距离和已加入vset的顶点
                continue;
            if(v0distance[j]<min){
                min=v0distance[j];
                vx=j;
            }
        }
        vset[vx]=1;//加入该顶点
        //计算v0->vmin->vk的距离
        //其中v0->vmin的最短距离保存在之前的v0distance里
        for(int k=1;k<vertexnum;k++){//计算通过minv的顶点后的距离,如果比原来小则进行松弛
             if(m[vx][k].cost==-1){//跳过无穷大点 
                continue;
            }else{
                tempdistance=v0distance[vx]+m[vx][k].cost;
                //松弛
                if(v0distance[k]==-1){
                    v0distance[k]=tempdistance;
                }else{
                    v0distance[k]=v0distance[k]<tempdistance?v0distance[k]:tempdistance;
                }
            }
        }
    }


}

int main(){
    shortestDistance();
    exit(0);
}
