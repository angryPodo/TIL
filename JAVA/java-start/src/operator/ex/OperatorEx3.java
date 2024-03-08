package operator.ex;

public class OperatorEx3 {
    public static void main(String[] args) {
        int score = 50;
        boolean judge;
        if (score >= 80 && score <= 100) {
            judge = true;
            System.out.println(judge);
        }
        else {
            judge = false;
            System.out.println(judge);
        }
    }
}
