#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<assert.h>
#define N 100
int main(){
    FILE *in=fopen("f:\\abc1.txt","wb");
    int a=65;
    int abuff;
    fwrite(&a,sizeof(int),1,in);
    fclose(in);
    FILE *out=fopen("f:\\abc12.txt","rb");
    assert(out!=NULL);
    fread(&abuff,sizeof(int),1,out);
    printf("a=%d",abuff);
    fclose(out);

    // FILE *fp=fopen("f:\\abc1.txt","r");
    // char str[N + 1];
    // if(fp==NULL){
    //     puts("open failed");
    //     exit(0);
    // }
    // fread(str, 100, 2,fp);
    //     printf("%d", str);
    // fclose(fp);
}

