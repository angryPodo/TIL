#include <stdio.h>
#include <stdlib.h>  // rand 함수 사용을 위한 헤더
#include <time.h>    // srand 함수 사용을 위한 헤더


void menu1(int kor95[], int math95[], char initial[], double preAvgList[],int size);

void menu2(int kor95[], int math95[], double avgList[], int size);

void menu3(double avgList[], char grade_list[], int size);

void menu3_pre(double preAvgList[], char preGrade_list[], int size);

void menu4(double avgList[], double preAvgList[], int judge[], int size);

void menu5(char* initial, int* kor95, int* math95, double* avgList, char* grade_list, int* judge, int* scholarship);

int main()
{

    int scholarship[2] = {4560000,0};
    int choice = 0;
    //오류 방지 더미데이터
    int kor95[2] = {0, 0};
    int math95[2] = {0, 0};
    int judge[2] = {0, 1};
    char initial_list[2];
    char grade_list[2] = {'a', 'b'};
    char preGrade_list[2] = {'a', 'b'};
    double avgList[2] = {0, 0};
    double preAvgList[2] = {0, 0};

    // srand를 사용하여 시드값 설정
    srand((unsigned int)time(NULL));

    // 무한 반복
    while (1)
    {
        // 메뉴 출력
        printf("******************* MJU 성적 프로그램 ********************\n"
               "<1> 자료 입력\n"
               "<2> 평균 계산\n"
               "<3> 학점 계산\n"
               "<4> 장학금 여부\n"
               "<5> 프린트\n"
               "<0> 종료\n\n"
               "메뉴를 선택하시오 :");
        scanf(" %d", &choice);
        printf("**********************************************************\n\n");
        if (choice == 0)
        {
            // 종료 메시지 출력
            printf("항목 0을 선택했습니다. 프로그램을 종료합니다.\n");
            break; // 프로그램 종료를 위한 브레이크
        }
        else if (choice == 1)
        {
            menu1(kor95, math95, initial_list, preAvgList,2);
        }
        else if (choice == 2) // 평균 계산
        {
            // 항목 2 선택 시 평균 계산 및 출력
            menu2(kor95, math95, avgList,2);
            for (int i = 0; i < 2; i++)
            {
                printf("%d번째 학생의 이번학기 평균은 %.2lf,전학기 평균은 %.2lf입니다.\n", i + 1, avgList[i], preAvgList[i]);
                printf("\n");
            }
        }
        else if (choice == 3) // 등급 계산
        {
            // 항목 3 선택 시 등급 계산 및 출력
            menu3(avgList, grade_list,2);
            menu3_pre(preAvgList, preGrade_list,2);
            for (int i = 0; i < 2; i++)
            {
                printf("%d번째 학생의 이번학기 등급은 %c,전학기 등급은 %c입니다.\n", i + 1, grade_list[i], preGrade_list[i]);
                printf("\n");
            }
        }
        else if (choice == 4)
        {
            // 항목 4 선택 시 장학금 여부 계산 및 출력
            menu4(avgList, preAvgList, judge,2);
            for (int i = 0; i < 2; i++)
            { // 장학금 계산
                if (judge[i])
                {
                    printf("축하드립니다 %d번째 학생은 %d원 장학금 대상자 입니다.\n", i + 1, scholarship[0]);
                }
                else
                {
                    printf("죄송합니다,%d번째 학생은 장학금 %d원으로 미대상자 입니다.\n", i + 1,scholarship[1]);
                }
                printf("\n");
            }
        }
        else if (choice == 5)
        {
            // 항목 5 선택 시 결과 프린트
            menu5(initial_list, kor95, math95, avgList, grade_list, judge, scholarship);
        }
        else // 메뉴 이외의 것을 입력했을 경우
        {
            // 잘못된 선택 메시지 출력
            printf("잘못된 선택입니다. 다시 선택하세요.\n");
        }
    }

    return 0;
}

void menu1(int kor95[], int math95[], char initial[], double preAvgList[],int size)
{
    for (int i = 0; i < 2; i++)
    {
        printf("%d번째 학생입니다.\n", i + 1);
        // 이니셜을 아스키 코드를 이용하여 랜덤하게 생성
        initial[i] = rand() % 26 + 65;  // 아스키 코드 65(A)부터 90(Z)까지
        printf("이니셜: %c\n", initial[i]);
        // 과목점수를 50부터 100까지의 난수로 생성
        kor95[i] = rand() % 51 + 50;
        printf("국어점수: %d\n", kor95[i]);
        math95[i] = rand() % 51 + 50;
        printf("수학점수: %d\n", math95[i]);
        // 전학기 평균을 50부터 100까지의 난수로 생성
        preAvgList[i] = rand() % 51 + 50;
        printf("전학기 평균: %.2lf\n", preAvgList[i]);
        printf("\n");
    }
}

void menu2(int kor95[], int math95[], double avgList[], int size)
{
    for (int i = 0; i < 2; i++)
        avgList[i] = (kor95[i] + math95[i]) / 2.0;
}

void menu3(double avgList[], char grade_list[], int size)
{
    for (int i = 0; i < 2; i++)
    {
        if (avgList[i] >= 90)
        {
            grade_list[i] = 'A';
        }
        else if (avgList[i] >= 80)
        {
            grade_list[i] = 'B';
        }
        else if (avgList[i] >= 70)
        {
            grade_list[i] = 'C';
        }
        else if (avgList[i] >= 60)
        {
            grade_list[i] = 'D';
        }
        else
        {
            grade_list[i] = 'F';
        }
    }
}

void menu3_pre(double preAvgList[], char preGrade_list[], int size)
{
    for (int i = 0; i < 2; i++)
    {
        int preten = preAvgList[i] / 10;
        switch (preten)
        {
        case 10:
        case 9:
            preGrade_list[i] = 'A';
            break;
        case 8:
            preGrade_list[i] = 'B';
            break;
        case 7:
            preGrade_list[i] = 'C';
            break;
        case 6:
            preGrade_list[i] = 'D';
            break;
        default:
            preGrade_list[i] = 'F';
            break;
        }
    }
}

void menu4(double avgList[], double preAvgList[], int judge[], int size)
{
    for (int i = 0; i < 2; i++)
    {
        if (avgList[i] >= 90 || (avgList[i] >= 80 && avgList[i] >= preAvgList[i] + 10))
            judge[i] = 1;
        else
            judge[i] = 0;
    }
}

void menu5(char* initial, int* kor95, int* math95, double* avgList, char* grade_list, int* judge, int* scholarship)
{
    for (int i = 0; i < 2; i++)
    {
        printf("%d번째 학생의 이니셜은 %c입니다.\n", i + 1, initial[i]);
        printf("국어점수는 %d, 수학점수는 %d입니다.\n", kor95[i], math95[i]);
        printf("%d번째 학생의 평균은 %.2lf, 등급은 %c입니다.\n", i + 1, avgList[i], grade_list[i]);
        if (judge[i])
        {
            printf("축하드립니다, %d번째 학생은 %d원 장학금 대상자 입니다.\n\n", i + 1, scholarship[0]);
        }
        else
        {
            printf("죄송합니다,%d번째 학생은 장학금 %d원으로 미대상자 입니다.\n", i + 1,scholarship[1]);
        }
    }
}

