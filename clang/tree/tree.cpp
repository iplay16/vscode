#include <stdio.h>
#include <stdlib.h>
#include "tree.h"
#include <queue>
#include <iostream>

using namespace std;
int max(int a,int b){
    return a>b?a:b;
}

TreeNode *createnode(int val)
{
    struct TreeNode *p=(struct TreeNode*)malloc(sizeof(struct TreeNode));
    p->val=val;
    p->left=NULL;
    p->right=NULL;
    return p;
}

int depth(TreeNode *tree){
    if(tree==NULL){
        return 0;
    }
    int leftdepth=1+depth(tree->left);
    int rightdepth=1+depth(tree->right);
    return max(leftdepth,rightdepth);
}

void test_depth(){
    TreeNode *p=init();
    int d=depth(p);
    printf("%d",d);
}

void preorder(TreeNode *root)
{
    if(root!=NULL)
    {
        printf("%d,",root->val);//visit
        preorder(root->left);
        preorder(root->right);
    }
}

TreeNode *init()
{
    int a[]= {3721,1,-1,2,-1,-1,3};//第一位数任意
    int asize=6;
    struct TreeNode *root=NULL;
    struct TreeNode *treequeue[6];
    for(int i=0; i<=asize; i++)
    {
        if(a[i]==-1)
        {
            treequeue[i]=NULL;
        }
        else
        {
            treequeue[i]=createnode(a[i]);
        }
    }

    for(int i=0; i<asize; i++)
    {
        if(2*i<=asize&&treequeue[i]){
            treequeue[i]->left=treequeue[2*i];
        }
        if(2*i+1<=asize&&treequeue[i])
            treequeue[i]->right=treequeue[2*i+1];
    }
    root=treequeue[1];

    return root;
}

void test_init()
{
    TreeNode *p=NULL;
    p=init();
    preorder(p);
}

void BFSprint(TreeNode *p){
    int *a=(int*)malloc(sizeof(int)*1000);
    int asize=-1;
    TreeNode* q=NULL;
    int queuesize;
    int deepth=0;
    char temp;
    queue<char> cq;
    queue<TreeNode*> treequeue;
    if(p!=NULL)
    {
        treequeue.push(p);
        while(!treequeue.empty())
        {
            a[++asize]=treequeue.back()->val;
            queuesize=treequeue.size();
            for(int i=0; i<7-deepth; i++)
                printf(" ");
            for(int i=0; i<queuesize; i++)
            {
                q=treequeue.front();
                treequeue.pop();
                printf("%d",q->val);

                for(int i=0; i<6-deepth; i++)
                    printf(" ");

                if(q->left){
                    treequeue.push(q->left);
                    cq.push('/');
                    }
                if(q->right){
                    treequeue.push(q->right);
                    cq.push('\\');
                }
            }
            printf("\n      ");
            while(!cq.empty()){
                temp=cq.front();
                cq.pop();
                printf("%c ",temp);
            }
            printf("\n");
            deepth++;
        }
    }
}

void test_BFSprint(){
    TreeNode *p=init();
    BFSprint(p);
}

TreeNode *copytree(TreeNode *t){
    TreeNode *newtree=NULL;
    if(t!=NULL){
        newtree=createnode(t->val);
        newtree->left=copytree(t->left);
        newtree->right=copytree(t->right);
    }
    return newtree;
}

void BFStree(TreeNode *p){
    int *a=(int*)malloc(sizeof(int)*1000);
    int asize=-1;
    TreeNode* q=NULL;
    int queuesize;
    queue<TreeNode*> treequeue;
    if(p!=NULL)
    {
        treequeue.push(p);
        while(!treequeue.empty())
        {
            a[++asize]=treequeue.back()->val;
            queuesize=treequeue.size();
            for(int i=0; i<queuesize; i++)
            {
                q=treequeue.front();
                treequeue.pop();
                printf("%d",q->val);

                if(q->left){
                    treequeue.push(q->left);
                    }
                if(q->right){
                    treequeue.push(q->right);
                }
            }
            printf("\n");
        }
    }
}

void test_copytree(){
    TreeNode *t=init();
    TreeNode *newtree=NULL;
    BFSprint(t);
    newtree=copytree(t);
    BFSprint(newtree);
}

// int main(){
//     test_copytree();
// }
