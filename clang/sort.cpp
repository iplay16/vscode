#include<stdlib.h>
#include<stdio.h>

int findpivotpos(int *a,int high,int low);
void QuickSort(int *a,int low,int high);
void QuickSort(int *a,int low,int high){
    int pivotpos;
    if(high>low){
         pivotpos = findpivotpos(a, low, high);
         QuickSort(a, low,pivotpos-1);
         QuickSort(a, pivotpos+1, high);
    }
}

int findpivotpos(int *a,int low,int high){
    int pivot=a[low];
    while(high>low){
        while(high>low&&a[high]>=pivot) high--;
        a[low]=a[high];
        while(high>low&&a[low]<=pivot) low++;
        a[high]=a[low];
        }

        a[low]=pivot;
        return low;
}

void test_QuickSort(){
    int a[10]={1,-2,4,5,-3,0,3,6,6,7};
    int pivotpos=findpivotpos(a,0,9);
    printf("%d\n",a[pivotpos]);
    QuickSort(a,0,9);
    for(int i=0;i<10;i++)
        printf("%d,",a[i]);
 }

 bool containsDuplicate(int* nums, int numsSize) {
    QuickSort(nums,0,numsSize-1);
    for(int i = 0; i < numsSize-1; i++)
    {
        if(nums[i]==nums[i+1])
            return true;
    }
    return false;
}

void test_containDuplicate(){
    int nums[4]={1,2,3,1};
    int numssize=4;

    
    containsDuplicate(nums,numssize-1);
        for(int i = 0; i < numssize; i++)
    {
        printf("%d ",nums[i]);
    }
}

int main(){
    test_containDuplicate();
    exit(0);
}
