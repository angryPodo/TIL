#include <stdio.h>

int main()
{
    int inputYear, result;

    printf("연도를 입력하세요: ");
    scanf("%d",&inputYear);

    result = ((inputYear%4==0) && (inputYear%100!=0) || (inputYear % 400 == 0));
    
    printf("%d",result);

    return 0;
}