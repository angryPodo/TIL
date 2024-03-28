#include <stdio.h>

int main()
{
    double cTemp,fTemp;

    printf("화씨 온도를 입력하세요: ");
    scanf("%lf", &fTemp);

    cTemp = (fTemp - 32) * 5 / 9; // 입력 받는 값이 double 이므로 자동 캐스팅이 일어남

    printf("섭씨 온도는 : %f 입니다.", cTemp);

    return 0;
}