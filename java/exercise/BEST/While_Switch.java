package JavaProg2;

import java.util.ArrayList;
import java.util.Scanner;

public class Exercise_9 {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        Scanner myObj = new Scanner(System.in);

        while (true) {
            System.out.println("1 - Добавить товар\n" + 
                        "2 - Удалить товар\n"  + 
                        "3 - Показать список\n" + 
                        "4 - Проверить, есть ли товар в списке\n" + 
                        "0 - Выход");
            
            int choise = myObj.nextInt();
            myObj.nextLine();
            switch (choise) {
                case 1 :
                    System.out.println("Что добавить в список? :");
                    String product = myObj.nextLine();
                    list.add(product);
                    System.out.println("Товар добавлен!");
                    break;

                case 2 :
                    System.out.println("Предмет который хотите удалить(имя или индекс) : ");
                    int del = myObj.nextInt();
                    list.remove(del);
                    System.out.println("Товар удален!");
                    break;

                case 3 :
                    for (int i = 0; i < list.size(); i++) {
                        System.out.println(list.get(i));}
                    break;

                case 4 :
                    System.out.println("Товар котрый хотите проверить : ");
                    String tovar = myObj.nextLine();
                    if (list.contains(tovar)) {
                        System.out.println("Товар" + tovar +  "есть в списке");}
                    System.out.println("Товара нет в списке");
                    break;
               case 0:
                    System.out.println("Выход из программы.");
                    return; // Завершает работу метода main
                
                default:
                    System.out.println("Неверная команда. Попробуйте снова.");


            
                
            }
        }
    }
}
