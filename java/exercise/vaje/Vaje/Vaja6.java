package Vaje;

public class Vaja6 {
    public static void main(String[] args) {
        // все четные числа из массива
        int [] numbers = {50,8,5,7,1,65};
        for (int i = 0; i < numbers.length; i++) {
            if (numbers[i] % 2 ==0) {
                System.out.println("четные числа :" + numbers[i]);
            }
        }for (int number : numbers ) {
            if (number % 2 == 0){
                System.out.println("Четное число :" + number);
            }
        }
        }
}
