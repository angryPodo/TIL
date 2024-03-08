package operator;

import javax.management.monitor.StringMonitor;

public class Operator2 {
    public static void main(String[] args) {
        String result1 = "hello"+"world";
        System.out.println(result1);

        String s1 = "string1";
        String s2 = "stirng2";
        String s3 = s1 + s2;
        System.out.println(s3);

        String result3  = "a + b = "+ 10;
        System.out.println(result3);

        int num1 = 123123;
        String str1 = "What the fuck?";
        String result4 = str1+" "+num1;
        System.out.println(result4);

    }
}
