#include <stdio.h> 
int main()
{
    double light_speed = 300000; //빛의 속도
    double distance = 149600000; //태양과 거리
    double time; //초기화 하지 않아도 됨
    
    time = distance / light_speed;

    printf("빛의 속도: %fkm/s \n", light_speed);
    printf("태양과 지구와의 거리: %fkm \n", distance); 
    printf("도달 시간: %f초\n", time);

    return 0; 
}