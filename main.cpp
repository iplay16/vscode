#include <iostream>
#include<stdlib.h>
#include<stdio.h>
using namespace std;
typedef struct node{
    int val;
    struct node *left;
    struct node *right;
}node,*tree;

int main(int, char**) {
    node *p=(node*)malloc(sizeof(node));
    void *vp;
    p->val=1;
    vp=p;
    printf("%d",((node*)vp)->val);
exit(0);
}
