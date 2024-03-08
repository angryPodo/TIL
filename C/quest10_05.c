#include <stdio.h>
#include <math.h>

double susik(double a, double b)
{
    double result;
    // result 변수에 저장
    result = (pow(a, 3) + 7 * pow(b, 2)) / 3;
    return result; // 계산 결과를 반환
}

int main()
{
    double x, y;
    printf("실수 두개를 입력하세요:"); 
    scanf("%lf,%lf", &x, &y); // 두 개의 실수 입력 받음
    double result = susik(x, y); // susik 함수를 호출,result 변수에 저장
    printf("계산결과:%lf", result); // 계산 결과를 출력
    return 0;
}


/*
double susik(double a,double b)
{
    double result;
    result = (pow(a,3)+7*pow(b,2))/3;
    printf("계산결과:%lf",result);
    return result;
}


int main()
{
    double x,y;
    printf("실수 두개를 입력하세요:");
    scanf("%lf,%lf",&x,&y);
    susik(x,y);
    return 0 ;

}
*/