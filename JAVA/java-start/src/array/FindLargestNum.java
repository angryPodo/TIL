package array;

public class FindLargestNum {
    public static void main(String[] args) {

        int[] numList = {1, 100, 45};
        int largeNum = numList[0];

        for (int num : numList) {
            if (largeNum < num) {
                largeNum = num;
            }
        }
        System.out.println(largeNum);
    }
}
