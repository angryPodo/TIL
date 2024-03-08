package scanner.ex;

import java.util.Scanner;

public class ChangeVarEx1 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("첫번쨰 값을 입력하세요 = ");
        int a = input.nextInt();
        System.out.print("두번쨰 값을 입력하세요 = ");
        int b = input.nextInt();
        int temp = a;
        a = b;
        b = temp;
        System.out.println(a+" "+b);

    }
}
