#include <stdio.h>

int get_first_digit(int x)
{
    if(x>0)
    {
        while(x>=10)
        {
            x/=10;
        }
        printf("가장 상위 자리수는 %d\n",x);
    }

    return x;
}

int is_prime(int num) {
    if (num <= 1) 
    {
        return 0; // 1 이하의 숫자는 소수가 아님
    }
    
    for (int i = 2; i < num; i++) 
    {
        if (num % i == 0) 
        {
            return 0; // num이 i로 나누어 떨어지면 소수가 아님
        }
    }
    
    return 1; 
}

int main()
{
    int null;
    printf("정수를 입력하시오:");
    scanf("%d",&null);
    get_first_digit(null);
    int prime=is_prime(null);
    if(prime==1)
    {
        printf("%d는 소수입니다.",null);
    }
    else
    {
        printf("%d는 소수가 아닙니다.",null);
    }
}