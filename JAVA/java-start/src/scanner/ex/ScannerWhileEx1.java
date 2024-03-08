package scanner.ex;

import java.util.Scanner;

public class ScannerWhileEx1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.print("이름을 입력하세요(종료입력시 종료): ");
            String name = scanner.nextLine();
            if(name.equals("종료")){
                System.out.println("종료합니다.");
                break;
            }
            System.out.print("나이을 입력하세요: ");
            String age = scanner.nextLine();

            System.out.println("당신의 이름은 :" + name + " 나이는 :" + age);

        }


    }
}
