package JavaProg2;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Exercise_15 {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        Map<String, Integer> inputs = new HashMap<>(); 

        while (true) {
            System.out.println("Введите имя (или 'stop' для выхода): ");
            String name = myObj.nextLine();
            
            if (name.equalsIgnoreCase("stop")) {
                break;
            }

            int age = 0;
            boolean validAge = false;

            while (!validAge) {
                System.out.println("Введите возраст : ");
                try { 
                    if (!myObj.hasNextInt()) {
                        System.out.println("Ошибка: Введите число!");
                        myObj.nextLine(); 
                        continue; 
                    }

                    age = myObj.nextInt();
                    myObj.nextLine(); 

                    if (age < 0) { 
                        throw new IllegalArgumentException("Возраст не может быть отрицательным");
                    }
                    validAge = true; 

                } catch (IllegalArgumentException e) {
                    System.out.println(e.getMessage()); 
                }
            }

    
            inputs.put(name, age);
            System.out.println("Успешно добавлено: " + name + " — " + age);
            System.out.println("Текущая база данных: " + inputs);
            System.out.println("-----------------------------------");
        }
        
        System.out.println("Программа завершена. Итоговый результат: " + inputs);
        myObj.close(); 
    }
}