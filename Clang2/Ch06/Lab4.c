#include <stdio.h>

int main(){
    int a,b,c;

    printf("삼각형의 3변을 입력하시오: ");
    scanf("%d %d %d" , &a, &b ,&c); 

    if ((c+b)>a && (a+c)>b && (a+b)>c){
        printf("올바른 삼각형");
    }
    else{
        printf("올바르지 않은 삼각형");
    }

    return 0;
    
}