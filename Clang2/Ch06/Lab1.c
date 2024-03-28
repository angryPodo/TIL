#include <stdio.h>

void operate(int x, int y, char op){
    int result = 0;
    if (op=='+') result = x + y;
    else if (op=='-') result = x - y;
    else if (op=='*' || op == 'x') result = x * y;
    else if (op=='/') result = x / y;
    else if (op=='%') result = x % y;
    else {
        printf("지원되지 않는 연산자입니다."); 
        return;
    }
    printf("%d %c %d = %d",x,op,y,result);
}

int main(){
    int x,y;
    char op;

    printf("수식을 입력하시오.\n(예: 2 + 5 )\n>>");
    scanf("%d %c %d",&x ,&op ,&y);
    
    operate(x,y,op);
    return 0;

}