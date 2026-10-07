package JavaProg2;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.concurrent.ThreadLocalRandom;


public class Exercise_13PET {
    public static void main(String[] args) {
        ArrayList<String> words = new ArrayList<>();
        words.addAll(List.of("кот", "собака" , "окно", "паровоз", "инопланетяне", "чай" ,"стул" , "опера" , "каракал" , "лебедь"  )) ;
        int x = ThreadLocalRandom.current().nextInt(0, words.size());
        String secretWord= words.get(x); 
        int lives =6;
        Scanner myObj = new Scanner(System.in);

        int len = secretWord.length();
        char[] mask = new char[len];
        for (int i = 0; i < mask.length; i++) {
            mask[i] = '_';}
        

        while (lives> 0) {
        for (int i = 0; i < mask.length; i++) {
            System.out.print(mask[i]+ " ");}
        System.out.println("(" + len + " букв" +")");

        System.out.println("Введите букву:");
        char input = myObj.next().charAt(0);

        boolean hit = false;
        for (int i = 0; i < len; i++) {
            if (input == secretWord.charAt(i)){
                mask[i]= input; 
                hit = true; } }
        if (hit == false) {
            lives -= 1;
        }
        System.out.println("Осталось жизней " + lives);
        if (String.valueOf(mask).equals(secretWord)){
            System.out.println("Поздравляю! Вы угадали слово!");
            for (int i = 0; i < secretWord.length(); i++) {
            System.out.print(secretWord.charAt(i) + " ");}
            break;
        } }
        if (lives==0){
            System.out.println("Игра окончена! Вы проиграли. Загаданное слово было:" + secretWord);
        }
        
    }
}
