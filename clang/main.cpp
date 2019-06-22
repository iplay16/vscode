#include<stdio.h>

int main(){
    const char *s=" 1 2 3 4 5 6 7 ";
    int wordnum=0;
    const char *p=s;
    int newwordflag=1;
    for(;*p!='\0';p++){
        if(*p==' '){
            newwordflag=1;
            continue;
        }
        if(*p!=' '&&newwordflag==1){
            wordnum+=1;
            newwordflag=0;
            continue;
        }
    }
    printf("%d",wordnum);
    getchar();
}
