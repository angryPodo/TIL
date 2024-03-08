#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand((unsigned)time(NULL));
    int dice[6];
    
    for(int i=0; i<6; i++)
    {
        dice[i] = 2 + (rand()%6)+(rand()%6);
    }

    for (int i = 0; i < 6; i++) 
    {
        if (i % 2 == 0) {
            printf("%d번째 주사위 숫자: ",i+1);
            printf("%d\n", dice[i]);
        }
    }
}