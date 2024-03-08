#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    srand((unsigned int)time(NULL));
    int lotto[6];
    for(int i=0;i<6;i++)
    {
        unsigned int randomNum = rand()%50;
        lotto[i] = randomNum;
    }
    for(int i=0;i<6;i++)
    printf("%d\n",lotto[i]);
}