#include "sqList.h"
ListNode *createListNode(int val){
    ListNode *p=(ListNode *)malloc(sizeof(ListNode));
    p->val=val;
    p->next=NULL;
    return p;
}

ListNode *createList(){
    int numsize=0;
    ListNode *p=NULL,*rear=NULL;
    printf("input numsize=\n");
    scanf("%d",&numsize);
    printf("\ninput nums=\n");
    int *nums=(int*)malloc(sizeof(int)*numsize);
    for(int i=0;i<numsize;i++)
        scanf("%d",&nums[i]);
    if(numsize==0)
        return NULL;
    p=createListNode(nums[0]);//第一个节点特殊处理
    rear=p;
    for(int i=1;i<numsize;i++)//尾插法
    {
        rear->next=createListNode(nums[i]);
        rear=rear->next;
    }
    return p;
}

ListNode *createListwithhead(){
    int numsize=0;
    printf("input numsize=\n");
    scanf("%d",&numsize);
    printf("\ninput nums=\n");
    int *nums=(int*)malloc(sizeof(int)*numsize);
    for(int i=0;i<numsize;i++)
        scanf("%d",&nums[i]);
    ListNode *head=createListNode(0);
    ListNode *rear=head;
    for(int i=0;i<numsize;i++){
        rear->next=createListNode(nums[i]);
        rear=rear->next;
    }
    return head;
}

void showList(ListNode *p){
    while(p){
        printf("%d->",p->val);
        p=p->next;
    }
    printf("NULL\n");
}

void showListwithhead(ListNode *head){
    ListNode *p=head->next;
    while(p){
        printf("%d->",p->val);
        p=p->next;
    }
    printf("NULL\n");
}

int listsize(ListNode *p){
    int size=0;
    while(p){
        p=p->next;
        size++;
    }
    return size;
}

int listsizewithhead(ListNode *head){
    ListNode *p=head->next;
    int size=0;
    while(p){
        p=p->next;
        p++;
    }
    return size;
}
// test
// void test_List(){
//     ListNode *list=createList();
//     showList(list);
// }
