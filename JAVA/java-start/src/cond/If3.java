package cond;

public class If3 {
    public static void main(String[] args) {
        int age = 13;
        if (age >= 5 && age < 6) {
            System.out.println("1");
        } else if (age >= 6 && age <= 12) {
            System.out.println("2");
        } else if (age >= 13 && age <= 15) {
            System.out.println("Goal");

        }
    }
}
