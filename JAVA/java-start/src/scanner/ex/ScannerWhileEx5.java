package scanner.ex;

import java.util.Scanner;

public class ScannerWhileEx5 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int sum = 0;

        while (true) {
            System.out.print("1:상품입력 2:결제 3:종료 ");
            int option = input.nextInt();
            input.nextLine();

            if (option==1) {

                System.out.print("상품명을 입력하세요: ");
                String name = input.nextLine();

                System.out.print("상품의 가격을 입력하세요: ");
                int price = input.nextInt();

                System.out.print("구메 수량을 입력하세요: ");
                int quantity = input.nextInt();

                sum += price * quantity;

                System.out.println("상품명:"+name+" 가격:"+price+" 수량:"+quantity+" 합계:"+sum);

            } else if (option == 2) {
                System.out.println("총 비용:"+sum);
                sum = 0;
            } else if (option == 3) {
                System.out.println("프로그램을 종료합니다.");
                break;
            } else {
                System.out.println("올바른 입력이 아닙니다.r");
            }


        }
    }
}
