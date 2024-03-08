package cond;

public class If5 {
    public static void main(String[] args) {
        int itemPrice = 10000;
        int age = 15;
        int discount = 0;

        if (itemPrice >= 10000) {
            discount += 1000;
            System.out.println(discount);
        }
        if (age <= 10) {
            discount += 1000;
            System.out.println(discount);
        }
        discount = 0;

    }
}
