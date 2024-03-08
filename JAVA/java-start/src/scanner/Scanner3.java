package scanner;

import java.util.Scanner;

public class Scanner3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("첫번째 정수를 입력하세요: ");
        int value1 = scanner.nextInt();

        System.out.print("두번째 정수를 입력하세요: ");
        int value2 = scanner.nextInt();

        if (value1 > value2) {
            System.out.println("큰수는: " + value1);
        } else {
            System.out.println("큰수는: " + value2);
        }


    }
}
