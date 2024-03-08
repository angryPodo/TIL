#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main()
{
    srand((unsigned)time(NULL));
    for(int i=1; i<7; i++)
    {
        int rotto = 1+rand()%45;
        printf("%d번째 로또 번호:%d\n",i,rotto);
    }

    return 0;
}