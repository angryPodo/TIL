package cond.ex;

public class ScoreEx {
    public static void main(String[] args) {
        int score = 45;
        char grade;
        if (score >= 90) {
            grade = 'A';
            System.out.println(score+" "+grade);
        } else if (score >= 80 && score < 90) {
            grade = 'B';
            System.out.println(score+" "+grade);
        } else if (score >= 70 && score < 80) {
            grade = 'C';
            System.out.println(score+" "+grade);
        } else if (score >= 60 && score < 70) {
            grade = 'D';
            System.out.println(score+" "+grade);
        } else {
            grade = 'F';
            System.out.println(score+" "+grade);
        }
    }
}
