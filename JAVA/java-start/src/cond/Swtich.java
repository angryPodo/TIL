package cond;

public class Swtich {
    public static void main(String[] args) {
        int grade = 1;
        int coupon;

        switch (grade) {
            case 1:
                coupon = 1;
            case 2:
                coupon = 2;
                break;
            case 3:
                coupon = 3;
                break;
            default:
                coupon = 0;
        }
        System.out.println(coupon);
    }
}
