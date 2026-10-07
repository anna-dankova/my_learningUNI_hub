package JavaProg2;

import java.util.Scanner;

public class Exercise_19 {
    public static void main(String[] args) {
        Scanner myobj = new Scanner(System.in);
        System.out.println("Введите строку : ");
        String input = myobj.nextLine();
        StringBuilder result = new StringBuilder();
        try {for (int i = 0; i < input.length(); i+=2) {
            char letter = input.charAt(i);
            char digitChar =  input.charAt(i+1);
            int count = Character.getNumericValue(digitChar);
            for (int j = 0; j < count; j++) {
                result.append(letter);}}}
        catch (IndexOutOfBoundsException e) {
            System.out.println("Ошибка: строка введена в неверном формате!");}
        System.out.println(result);
    }
}



