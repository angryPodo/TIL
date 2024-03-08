#include <stdio.h>

int main()
{
    int num0,num1;
    printf("정수 2개를 입력하시오:");
    scanf("%d,%d",&num0,&num1);

    for (int i = 1; i <=100; i++)
    {
        if(i%num0==0 && i%num1==0)
        {
            printf("1~100까지 정수중 사용자가 입력한 정수의 공배수:%d\n",i);
        }
        else
            continue;
    }
    return 0 ;
}