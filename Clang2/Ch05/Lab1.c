#include <stdio.h>

int main()
{
    int price,pay; // 초기화 하지 않음
    int charge,paper5,paper1,coin5,coin1; // 초기화 하지 않음
    printf("물건 값을 입력하시오: ");
    scanf("%d",&price);

    printf("사용자가 낸 돈: ");
    scanf("%d",&pay);

    charge = pay-price;
    paper5 = charge / 5000; //몫 계산
    paper1 = (charge % 5000) / 1000; // 나머지 연산 후 몫 계산
    coin5 = (charge % 1000) / 500; // 나머지 연산 후 몫 계산
    coin1 = (charge % 500) / 100; // 나머지 연산 후 몫 계산

    printf("거스름돈 목록\n");
    printf("5천원권 %d장\n", paper5);
    printf("1천원권 %d장\n", paper1 );
    printf("5백원 %d개\n", coin5 );
    printf("1백원 %d개\n", coin1 );

}