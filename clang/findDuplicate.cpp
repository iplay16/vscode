#include<stdlib.h>
#include<stdio.h>
#include<math.h>
int findDuplicate(int* nums, int numsSize) {
    int *a=(int*)malloc(sizeof(int)*(numsSize+1));
    int dumplicatenum=0;
    for(int i=0;i<numsSize;i++){
        a[i]=0;
    }
    for(int i=0;i<numsSize;i++){
        if(a[nums[i]]==0)
            a[nums[i]]=nums[i];
        else
        {
            dumplicatenum=a[nums[i]];
            break;
        }
    }
    return dumplicatenum;
}


void subsets_get(int *a,int asize,const int* nums,const int maxsize,int **result,int *resultsize,int *columnSizes,int isadd){
    //操作a
    a[++asize-1]=isadd;
    
    //a满条件下,操作result
    if(asize==maxsize){
        //写入result
        (*resultsize)++;
        int count=0;
        for(int i=0;i<maxsize;i++) //统计该行长度,并写入第*resultsize行的第count个元素
            if(a[i]==1) result[*resultsize-1][++count-1]=nums[i];
            //写入第*resultsize行的数量
        columnSizes[*resultsize-1]=count;
        //printf("%d %d %d\n",(*columnSizes)[0],(*columnSizes)[1],(*columnSizes)[3]);
        
            for(int j=0;j<columnSizes[*resultsize-1];j++)
                printf("%d ",result[*resultsize-1][j]);
        
        printf("\n");
        //停止递归
        return;
    }
    subsets_get(a,asize,nums,maxsize,result,resultsize,columnSizes,1);//1代表添加
    subsets_get(a,asize,nums,maxsize,result,resultsize,columnSizes,0);
}

//该函数放回了三个值,**a,*columnSize和returnSize,两个放在参数位置,要传入地址
int** subsets(int* nums, int numsSize, int** columnSizes, int* returnSize) {
    int *a=(int*)malloc(sizeof(int)*numsSize);
    int **result=(int**)malloc(sizeof(int*)*3000);
    for(int i=0;i<3000;i++){
        result[i]=(int*)malloc(sizeof(int)*numsSize);
    }
    int asize=0;
    int maxsize=numsSize;
    int resultrow=0;
    int *cs=(int*)malloc(sizeof(int)*(int)(pow(2,numsSize)));
    subsets_get(a,asize,nums,maxsize,result,&resultrow,cs,1);
    subsets_get(a,asize,nums,maxsize,result,&resultrow,cs,0);
    *columnSizes=cs;
    *returnSize=resultrow;
    return result;
}


void test_subsets(){
    int nums[10]={1,2,3,4,5,6,7,8,10,0};
    int *cs=NULL;
    int rs=0;
    for(int i=0;i<10&&i==0;i++)
        printf("%d ",i);

    subsets(nums,10,&cs,&rs);
    printf("%d",rs);
}

char* decodeString(char* s);

char* decodeString(char* s) {
    char *result=(char*)malloc(sizeof(char)*5000);
    int resultsize=0;
    int *indexstack=(int*)malloc(sizeof(int)*5000);
    int indexstatcksize=0;
    char *symstack=(char*)malloc(sizeof(char)*500);
    int symstacksize=0;
    int *numstack=(int*)malloc(sizeof(int)*500);
    int numstacksize=0;
    int times=0;
    int rear=0;
    char *p=s;
    char charnum[5];
    int charnumsize=0;
    int total=0;
    for(int i=0;p[i]!='\0';i++){
        ;
    }
    for(int i=0;p[i]!='\0';i++){
        if(p[i]=='['){
            symstack[++symstacksize-1]='[';
            indexstack[++indexstatcksize-1]=resultsize;
            
            for(int j=0;j<charnumsize;j++)
                total+=(charnum[j]-48)*(int)pow(10,charnumsize-j-1);
            numstack[++numstacksize-1]=total;//入栈
            total=0;//total清零
            charnumsize=0;//字符清零
            continue;
        }
        if(p[i]==']'){
            times=numstack[numstacksize---1];//数字出站
            rear=resultsize;
            for(int j=0;j<times-1;j++){//复制times-1遍
                for(int k=indexstack[indexstatcksize-1];k<rear;k++){
                result[++resultsize-1]=result[k];
                }

            }
                for(int m=0;m<resultsize;m++){
                    printf("%c",result[m]);
                }
                 printf("\n");
            indexstatcksize--;
            symstacksize--;
            continue;
        }

        if(p[i]>=48&&p[i]<=57){
            charnum[++charnumsize-1]=p[i];
            continue;
        }

        result[++resultsize-1]=p[i];
    }
    result[++resultsize-1]='\0';
    free(symstack);
    free(indexstack);
    free(numstack);
    return result;
}

void test_decodeString(){
    char *s="3[z]2[2[y]pq4[2[jk]e1[f]]]ef";
    printf("input:%s\n",s);
    char *result=NULL;
    result=decodeString(s);
    printf("%s",result);
}

int majorityElement(int* nums, int numsSize) {
    int major=nums[0];
    int count=0;
    for(int i=0;i<numsSize;i++){
       if(count==0){
           major=nums[i];
           count++;
        }else{
            if(major==nums[i]){
                count++;
            }else{
                count--;
            }
        }
    }
    return major;
}

void test_majorityElement(){
    int nums[3]={3,3,4};
    int major=majorityElement(nums,3);
    printf("%d",major);
}



int main(){
    test_majorityElement();
}

