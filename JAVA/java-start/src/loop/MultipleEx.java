package loop;

public class MultipleEx {
    public static void main(String[] args) {
        int rows = 3;
        for (int i = 0; i < rows; i++) {
            // 공백 출력
            for (int j = 0; j < rows - i - 1; j++) {
                System.out.print(" ");
            }
            // 별 출력
            for (int k = 0; k < 2 * i + 1; k++) {
                System.out.print("*");
            }
            // 줄 바꿈
            System.out.println();
        }
    }
}
