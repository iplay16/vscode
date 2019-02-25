#include<vector>
#include<new>
#include<stdio.h>
#include<stdlib.h>
#include<list>
#include<queue>
using namespace std;

typedef struct GeneralEdge{
    int fromvertex;
    int tovertex;
    int cost;
}GeneralEdge;

typedef struct Edge{
    int nextNode;
    int cost;
}Edge;

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
int main(){
    GraphDFSTraverse();
    exit(0);
}
