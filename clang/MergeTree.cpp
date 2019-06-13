#include "tree.h"
#include<stdio.h>

struct TreeNode* mergeTrees(struct TreeNode* t1, struct TreeNode* t2) {
    TreeNode *newtree=NULL;
    if(t1==NULL&&t2==NULL)
        return NULL;
    else
    {
        if(t1==NULL){
            return  copytree(t2);
        }
        if(t2==NULL){
            return copytree(t1);
            }
        newtree=createnode(t1->val+t2->val);
        newtree->left=mergeTrees(t1->left,t2->left);
        newtree->right=mergeTrees(t1->right,t2->right);
    }
    return newtree;
}
