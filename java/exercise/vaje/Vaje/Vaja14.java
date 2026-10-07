package Vaje;

public class Vaja14 {
    public static void main(String[]args){
        int num = 1293343;
        int reversed = 0;
        int original = num;
        while (num>0){
            int digit= num % 10;
            reversed = reversed * 10 + digit;
            num /=10;
        }
        if (reversed == original) {
            System.out.println("Its armstrong number");
        } else {System.out.println("It is not an armstrong number");}
    }
}