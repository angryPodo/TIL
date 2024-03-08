package scanner.ex;

import java.util.Scanner;

public class ScannerEx1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("이름을 입력하세요: ");
        String name = scanner.nextLine();
        System.out.print("나이을 입력하세요: ");
        String age = scanner.nextLine();

        System.out.println("당신의 이름은 :"+name+" 나이는 :"+age);



    }
}
