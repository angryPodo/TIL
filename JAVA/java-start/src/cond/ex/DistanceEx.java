package cond.ex;

public class DistanceEx {
    public static void main(String[] args) {
        int distance = 2123;

        if (distance <= 1) {
            System.out.println("walk");
        } else if (distance <= 10) {
            System.out.println("cycle");
        } else if (distance <= 100) {
            System.out.println("car");
        } else {
            System.out.println("plane");
        }

    }
}
