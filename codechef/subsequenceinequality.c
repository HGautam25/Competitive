#include<stdio.h>
#include<stdlib.h>
int main(){
    int n;
    scanf("%d",&n);
    for(i=0;i<n;i++){
        char* arr=(char*)malloc(100*sizeof(char));
        scanf("%s",arr);
        for(j=0;arr[j]!='\0';j++){
            for(k=1;arr[k]!='\0';k++){
                if(arr[j]==arr[k]){
                    flag=1;
                }
            }
        }
        if(flag==1){
            printf("Yes");
        }
        else{
            printf("No");
        }
    }
}