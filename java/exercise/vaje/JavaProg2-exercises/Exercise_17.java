package JavaProg2;

import java.util.ArrayList;
import java.util.InputMismatchException;
import java.util.Scanner;

public class Exercise_17 {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        String[] arr = { "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"};
        while (true) {
            try {
                System.out.println("Введите индекс элемента:" );
                int num = myObj.nextInt();
                System.out.println(arr[num]);
                break;}

            catch (InputMismatchException e) {
                System.out.println("Пожалуйста, введите число!");
                myObj.next();
            }
            catch (ArrayIndexOutOfBoundsException e){
                System.out.println("Индекс вне границ, попробуйте еще раз!");
            }

            
        }

    }
}
