package JavaProg2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Exercise_16 {
    public static void main(String[] args) {
        
    
    Scanner myObj = new Scanner(System.in);

    System.out.print("Введите имя файла для чтения (например, input.txt): ");
    String inputFile = myObj.nextLine();

    System.out.print("Введите имя файла для записи (например, output.txt): ");
    String outputFile = myObj.nextLine();

    try (BufferedReader reader = new BufferedReader(new FileReader(inputFile));
    PrintWriter writer = new PrintWriter(new FileWriter(outputFile));) {
        String line ;
        while ((line = reader.readLine()) != null) {
            String word = line.trim();
            if (jePalindrom(word)){
                writer.println(word);
            }
        }
        System.out.println("Фильтрация завершена! Проверь файл: " + outputFile);
    } catch (IOException e) {
        System.out.println("Ошибка при работе с файлами: " + e.getMessage());}
    }
    public static boolean jePalindrom(String s){
        int len = s.length();
        if (len <=1) { return true;}
        char firstChar = Character.toLowerCase(s.charAt(0));
        char lastChar = Character.toLowerCase(s.charAt(s.length() - 1));
        if (firstChar != lastChar) {return false;}
        String middle = s.substring(1, len -1);
        return jePalindrom(middle);

    
        }
    }