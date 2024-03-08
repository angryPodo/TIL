package scanner.ex;

import java.util.Scanner;

public class ScannerEx2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("정수를 입력하세요:");
        int num = scanner.nextInt();

        if (num==0) {
            System.out.println("0을 입력하셨습니다.");
        }
        else if (num % 2 == 0) {
            System.out.println(num + "은 짝수입니다.");
        } else {
            System.out.println(num + "은 홀수입니다.");
        }

    }
}
