#include <stdio.h>

int main()
{
    int num[6];
    
    for(int i=0; i<6; i++)
    {   
        printf("%d번째 정수를 입력하시오:", i+1);
        scanf("%d", &num[i]);
    }

    for(int j=0;j<6;j++)
    {
        if(j%2==0)
        {
            printf("%d번째 입력된 수:%d\n", j+1, num[j]);
        }
    }
    
    return 0;
}