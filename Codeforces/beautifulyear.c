#include<stdio.h>
#include<stdlib.h>
int isuniq(int n);
int main(){
    int num;
    scanf("%d",&num);
    num++;
    while(isuniq(num)!=1){
        num++;
    }
    printf("%d",num);
}
int isuniq(int n){
    int arr[10]={0},i;
    for(i=0;i<10;i++){
        if(n>0){
            arr[n%10]++;
            n/=10;
        }
    }
    for(i=0;i<10;i++){
        if(arr[i]>1){
            return 0;
        }
    }
    return 1;
}