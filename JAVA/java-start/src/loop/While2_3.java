package loop;

public class While2_3 {
    public static void main(String[] args) {
        int sum = 0;
        for (int i = 1; sum < 10; i++) {
            sum += i;
            System.out.println(sum);
        }
    }
}
