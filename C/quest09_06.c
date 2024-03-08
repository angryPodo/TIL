#include <stdio.h>

int main()
{
    int mul = 0;

    for(int i = 1; i<=10; i++)
        if(i%3==1)//증감을 1씩하는 대신 나머지로 1,4,7,10
        {
            for(int j = 1; j <10; j++)
            {
                mul=i*j;
                printf("%d*%d=%d\n",i,j,mul);
            }
            
        }
        else
            continue;
     /* 2번째 방법!
    int mul = 0;

        for (int i = 1; i <=10; i+=3)//증감을 3씩
        {
            for (int j = 1; j < 10; j++)
            {
                mul=i*j;
                printf("%d*%d=%d\n",i,j,mul);
            }
                
        }
    */

    return 0 ;
}

