package scanner.ex;

import java.util.Scanner;

public class ScannerEx4 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("구구단의 단을 입력하세요: ");
        int mul = input.nextInt();

        if (mul > 0 && mul < 10) {
            for (int i = 1; i <= 9; i++) {
                System.out.println(mul + "*" + i + "=" + mul * i);
            }
        } else {
            System.out.println("1~9를 입력해주세요");
        }
    }
}
