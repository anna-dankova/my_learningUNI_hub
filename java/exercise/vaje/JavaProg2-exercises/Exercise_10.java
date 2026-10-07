package JavaProg2;

import java.util.Scanner;

public class Exercise_10 {
    public static void main(String[] args) {
        Scanner myObj=  new Scanner(System.in);
        System.out.println("Введите предложение и потом число ");
        String str = myObj.nextLine();
        int shift = myObj.nextInt();
        myObj.nextLine();
        String result = "" ;

    for (int i = 0; i < str.length(); i++) {
        char currentChar = str.charAt(i);
    
    if (currentChar >= 'a' && currentChar <= 'z') {
        // Если это маленькая буква — шифруем её
        char encryptedChar = (char) ('a' + (currentChar - 'a' + shift) % 26);
        result += encryptedChar;
    } else {
        // Если это пробел, знак препинания или большая буква — оставляем как было
        result += currentChar; 
     } }
      System.out.println(result);
    
    
} 
}