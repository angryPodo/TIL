/*
프로그래머 : 한민재 60201995
*/

#include <stdio.h>

void add(int x)
{
    x = x+1;
}

void addPoint(int *x)
{
    *x+=1;
}

int main() 
{
    int a=10, b=20, c=30;
    add(c);
    printf("add 호출 후 : %d\n", c);
    addPoint(&c);
    printf("addPointer 호출 후: %d", c);
}

