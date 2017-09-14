#include<stdio.h>
#include<stdlib.h>
#include<math.h>
void main(){
    int n,i,*arrx,*arry,*arrz,sumx=0,sumy=0,sumz=0;
    arrx = (int *)malloc(n * sizeof(int));
    arry = (int *)malloc(n * sizeof(int));
    arrz = (int *)malloc(n * sizeof(int));
    scanf("%d", &n);
    for (i = 0; i < n;i++){
        scanf("%d %d %d", &arrx[i], &arry[i], &arrz[i]);
    }
    for (i = 0; i < n;i++){
        sumx += arrx[i];
        sumy += arry[i];
        sumz += arrz[i];
    }
    if(sumx==sumy && sumx==sumz && sumx==0){
        printf("YES");
    }
    else{
        printf("NO");
    }
}