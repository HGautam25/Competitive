#include<stdio.h>
#include<stdlib.h>
int main(){
    int n,i,j,k,sum1=0,sum2=0;
    scanf("%d",&n);
    int arr[n][n];
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            scanf("%d",&(arr[i][j]));
        }
    }
    for(i=0;i<n;i++){
        for(j=0;j<n;j++){
            printf("%d ",(arr[i][j]));
        }
        printf("\n");
    }
    for(i=0,k=n-1;i<n,k>=0;i++,k--){
        sum1+=arr[i][i];
        sum2+=arr[i][k];
    }
    printf("%d",abs(sum1-sum2));
}