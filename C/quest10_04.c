#include <stdio.h>

void numberDecision(int i)
{
    if (i > 0) // 입력된 값이 양수인 경우
    {
        printf("양수입력!");
    }
    else if (i < 0) // 입력된 값이 음수인 경우
    {
        printf("음수입력!");
    }
    else // 입력된 값이 0인 경우
    {
        printf("0입력!");
    }
}

int main()
{
    int num0; // 입력 받을 정수를 저장할 변수
    printf("정수를 입력하시오."); 
    scanf("%d", &num0); // 정수 입력 받음
    numberDecision(num0); // 정수 판단 함수 호출

    return 0;
}
