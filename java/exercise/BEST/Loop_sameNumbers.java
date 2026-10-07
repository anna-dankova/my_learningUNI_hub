package JavaProg2;

import java.util.ArrayList;
import java.util.Scanner;

public class Exercise_11 {
    public static void main(String[] args) {
        ArrayList<Integer> list1 = new ArrayList<>(); 
        ArrayList<Integer> list2 = new ArrayList<>(); 
        Scanner myObj = new Scanner(System.in);

        System.out.println("Введите 5 чисел для первого списка: ");
        for (int i = 0; i <5 ; i++) {
            list1.add(myObj.nextInt());
        }
        System.out.println("Введите 5 чисел для второго списка:");
        for (int i = 0; i < 5; i++) {
            list2.add(myObj.nextInt());  
        }  myObj.nextLine();

        ArrayList<Integer> list3 = new ArrayList<>();

        for (int i = 0; i < list1.size(); i++) {
            int temp=list1.get(i);
            for (int j = 0; j < list2.size(); j++) {
                if (temp == list2.get(j) && !list3.contains(temp) ) {
                    list3.add(temp);
                }
            }
        }
        System.out.println("--- Общие числа (до фильтрации) ---");
        for (int i = 0; i < list3.size(); i++) {
            System.out.println(list3.get(i));
        }
        list3.removeIf(num -> num % 2 ==0);

        System.out.println("--- Итоговый список (только нечетные общие числа) ---");
        for (int i = 0; i < list3.size(); i++) {
            System.out.println(list3.get(i)); }
    }  
}
