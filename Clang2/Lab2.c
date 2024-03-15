#include <stdio.h>

int main(){
    const double koPyeong = 3.3058; //상수
    int input;
    double result;

    printf("평을 입력하세요: ");
    scanf("%d",&input);

    result = input*koPyeong;
    printf("%lf 평방미터입니다.",result);

    return 0;
}