#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main(){
    int arr[5][5],i,j,temp,tempi,tempj,steps=0;
    for (i = 0; i < 5;i++){
        for (j = 0; j < 5;j++){
            scanf("%d",&temp);
            if(temp==1){
                tempi = i;
                tempj = j;
            }
            arr[i][j] = temp;
        }
    }
    steps = abs(2 - tempi);
    steps += abs(2 - tempj);
    printf("%d",steps);
}