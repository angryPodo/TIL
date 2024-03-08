#include <stdio.h>

int main()
{
    double math[5], sum=0, avg;

    for(int i=0; i<5; i++)
    {
        printf("%d번째 학생의 수학 점수를 입력하시오:", i+1);
        scanf("%lf", &math[i]);
    }
    for(int i=0; i<5; i++)
    {
        sum += math[i];
    }
    avg = sum/5.0;
    printf("평균 성적:%lf", avg);
}