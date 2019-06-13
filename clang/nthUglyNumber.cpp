#include<stdio.h>
#include<stdlib.h>

bool isUgly(int n){
    if(n%2==0){
        return true;
    }
    if(n%3==0){
        return true;
    }
    if(n%5==0){
        return true;
    }
    return false;
}

int nthUglyNumber(int n){
    int nth=1;
    if(n=1){
        return 1;
    }
    int i=2;//i is number
    while(true){
        if(isUgly(i)){
            nth++;
        }
        if(nth==n){
            return i;
        }
        i++;
    }
}


int main(){
    int n=nthUglyNumber(2);
    printf("%d\n",n);
    nthUglyNumber(10);
    n=printf("%d\n",n);
    exit(0);

}