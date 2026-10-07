package Vaje;

import java.util.Scanner;

public class Vaja4 {
    public static void main (String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Введите число :");
        Integer userinput = scanner.nextInt();
        if (userinput % 2 ==0) {
            System.out.printf(" Число четное ");
        }else {
            System.out.printf("Число не четное ");
        }
    }
}
