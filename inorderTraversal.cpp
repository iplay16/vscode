#include<stdio.h>
#include<stdlib.h>
#include "tree.h"
using namespace std;
 
void inorder(struct TreeNode* tree,int *a,int *asize){
    if(tree!=NULL){
        inorder(tree->left,a,asize);
        (*asize)++;
        a[*asize-1]=tree->val;
        inorder(tree->right,a,asize);
    }
}
int* inorderTraversal(struct TreeNode* root, int* returnSize) {
    int *a=(int*)malloc(sizeof(int)*300);
    int asize=0;
    inorder(root,a,&asize);
    *returnSize=asize;
    return a; 
}

int* test_inorderTraversal(){
    TreeNode *t=init();
    int rs=0;
    BFSprint(t);
    int *a=inorderTraversal(t,&rs);
    for(int i=0;i<rs;i++)
        printf("%d ",a[i]);
}

int main(){
    test_inorderTraversal();
    printf("hleL");
    getchar();
    exit(0);
}
