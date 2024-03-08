package scanner;

import java.util.Scanner;

public class ScannerWhile3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int sum = 0;
        while (true) {
            System.out.print("정수를 입력하세요(0을 입력하면 종료됩니다.): ");
            int num1 = scanner.nextInt();

            if (num1 == 0) {
                break;
            }
            sum += num1;

        }
        System.out.println("정수의 총합은: "+sum);

    }
}
