#include <stdio.h>
#include <stdlib.h>
int main()
{
    int n, t = 0, i, j, temp, t_max;
    scanf("%d %d", &n, &t_max);
    char *arr = (char *)malloc((n + 1) * sizeof(char));
    scanf("%s", arr);
    while(t<t_max){
    for (i = 0; i < n-1;i++){
        if (arr[i] == 'B' && arr[i + 1] == 'G')
            {
                temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                i++;
            }
    }
    t++;
    }
    printf("%s\n", arr);
}
