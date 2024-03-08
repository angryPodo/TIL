#include <stdio.h>

int main() {
    char c;
    int count = 0;
    int inWord = 0;  // 단어 안에 있는지 여부를 나타내는 변수

    while ((c = getchar()) != EOF) 
    {
        // 공백 문자를 기준으로 단어의 시작과 끝을 판단
        if (c == ' ' || c == '\n' || c == '\t') 
        {
            inWord = 0;  // 현재 문자가 공백 문자라면 단어 안에 있지 않음
        } 
        else
        {
            if (!inWord) 
            {
                count++;  // 단어의 시작이라면 단어 개수 증가
                inWord = 1;  // 단어 안에 있음으로 표시
            }
        }
    }

    printf("%d\n", count);

    return 0;
}
