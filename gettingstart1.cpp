#include<stdio.h>
#include<stdlib.h>
#include "tree.h"

bool isDumplicate(int *nums,int numsSize,int newnum){
    for(int i=0;i<numsSize;i++){
        if(nums[i]==newnum)
            return true;
    }
    return false;
}

bool isSameTree(struct TreeNode* p, struct TreeNode* q) {
    if(p==NULL&&q==NULL)
        return true;
    if(p==NULL&&q!=NULL)
        return false;
    if(p!=NULL&&q==NULL)
        return false;
    if(p->val==q->val){
        return isSameTree(p->left,q->left)&&isSameTree(p->right,q->right);
    }
    return false;
}


void LIS(){
    int maxlis[7]={89,256,78,1,46,78,8};
    int lissize=7;
    int maxlisnum[7]={0};
    int tempmaxlisnum=1;//本身自己一个
    maxlisnum[0]=1;
    for(int i=1;i<lissize;i++){//i在后,j在前
        //状态转移方程maxlis[i]=maxlis[i-1]+1;
        for(int j=0;j<i;j++){//大于之前的*任意*一个lis的最大值
            if(maxlis[i]>maxlis[j]){
                tempmaxlisnum=tempmaxlisnum>maxlisnum[j]+1?tempmaxlisnum:maxlisnum[j]+1;
            }
        }
        maxlisnum[i]=tempmaxlisnum;
        tempmaxlisnum=1;//置零,准备下一次循环
    }
    for(int i=0;i<lissize;i++){
        printf("%dhas %d | ",i,maxlisnum[i]);
    }
}


// void LCS(){
//     int lcs1={};
//     int lcs2={};
//     int lcsnum[][]={{1}};//lcsnum[x][y]为lcs1[x]和lcs2[y]的公共子序列
//     for(int )
//     if(lcs1[x]=lcs2[y])
//         lcs[x][y]=lcs[x-1][y-1];
//     if(lcs1=[x]!=lcs2[y])
//         max(lcsnum[x-1][y],lcsnum[x][y-1]);
// }

bool containsDuplicate(int* nums, int numsSize) {
    int *flag=(int*)malloc(sizeof(int)*numsSize);
    for(int i = 0; i < numsSize; i++)
    {
        flag[i]=0;
    }
    for(int i = 0; i < numsSize; i++)
    {
        if(flag[i]==0){
            flag[i]=1;
        }else{
            return true;
        }
    }
    return false;
}

bool canJump(int* nums, int numsSize) {
    int *reach=(int*)malloc(sizeof(int)*numsSize);
    for(int i=1;i<numsSize;i++){
        reach[i]=0;
    }
    reach[0]=1;
    if(numsSize==1)
        return true;
    for(int i=0;i<numsSize-1;i++){
        if(reach[i]){//如果自身可达
            if(i+nums[i]>=numsSize-1){
                printf("true");
                return true;
            }
            else{
                for(int j=i+1;j<i+nums[i]+1;j++){
                    reach[j]=1;
                }
            }
        }
    }
    printf("false");
    return false;
}

void test_canJump(){
    int nums[4]={2,5,0,0};
    canJump(nums,4);
}
//jump game II
int jump(int* nums, int numsSize) {
    int *reach=(int*)malloc(sizeof(int)*numsSize);
    for(int i=1;i<numsSize;i++){
        reach[i]=0;
    }

    int *reachnum=(int*)malloc(sizeof(int)*numsSize);
    for(int i=1;i<numsSize;i++){
        reachnum[i]=-1;
    }

    reach[0]=1;
    reachnum[0]=0;
    if(numsSize==1)
        return 0;
    for(int i=0;i<numsSize-1;i++){
        if(reach[i]){//如果自身可达
            if(i+nums[i]>=numsSize-1){
                printf("true");
                return reachnum[i]+1;
            }
            else{
                for(int j=i+1;j<i+nums[i]+1;j++){
                    reach[j]=1;
                    if(reachnum[j]==-1)
                        reachnum[j]=reachnum[i]+1;
                    else{
                        reachnum[j]=reachnum[i]+1<reachnum[j]?reachnum[i]+1:reachnum[j];
                    }
                }
            }
        }
    }
    printf("false");
    return -1;
}

void test_Jump(){
    int nums[5]={1,2,1,1,1};
    int jumpnum=jump(nums,5);
    printf("%d",jumpnum);
}

int* productExceptSelf(int* nums, int numsSize, int* returnSize) {
    int sum=1;
    int* product=(int*)malloc(sizeof(int)*numsSize);
    int psize=0;
    for(int i = 0; i < numsSize; i++)
    {
        sum*=nums[i];
    }
    for(int i = 0; i < numsSize; i++){
        nums[++psize-1]=sum/nums[i];
    }
    *returnSize=psize;
    return product;
}


int lengthOfLongestSubstring(char* s){
    int len=0;
    char *p=s;
    while(*p!='\0'){
        p++;
        len++;
    }

    int count=0;
    int lastmaxlen=1;
    int dindex=-1;//标记重复位置

    for(int i=1;i<len;i++){
        for(int j=dindex+1;j<i;j++){//判断是否重复
            if(s[i]==s[j]){//重复了
                dindex=i;//标记preindex
                lastmaxlen=count>lastmaxlen?count:lastmaxlen;
                count=0;//清零重新计数
                break;
            }
            count++;
        }
    }
    return lastmaxlen;
}

void test_lengthOfLongestSubstring(){
    char *s="abcabcbb";
    int a=lengthOfLongestSubstring(s);
    printf("%d",a);
}

int main(){
    test_lengthOfLongestSubstring();
}
