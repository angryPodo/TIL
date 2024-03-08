package array;

public class Array1 {
    public static void main(String[] args) {
        int[] students = new int[10];
        for (int i = 0; i < 10; i++) {
            students[i] = (i%2);
            System.out.println(students[i]);
        }

    }
}
