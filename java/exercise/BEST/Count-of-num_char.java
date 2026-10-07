package JavaProg2;
import java.util.Scanner;
public class Exercise_8 {
    public static void main(String[] args) {
        Scanner myObj = new Scanner( System.in);
        System.out.println("Your string :");
        String userString = myObj.nextLine();
        
        String text = userString.toLowerCase();
        int count =0;
        int countNum = 0;
        for (int i = 0; i < text.length(); i++) {
            char c = text.charAt(i);
            if ("aeiou".indexOf(c) != -1){
                count ++;
            }
            if ("1234567890".indexOf(c) != -1){
                countNum++;
            }}
        System.out.println(count);
        System.out.println(countNum);
        
        System.out.println("your char: ");
        String userinput = myObj.nextLine();
        char userChar = userinput.charAt(0);
        String[] words = text.split(" ");
        

        for (int i = 0; i < words.length; i++) {
            String word = words[i];
            if (word.charAt(0) == userChar) {
                System.out.println(word);
            }
            }
            myObj.close();
        }


    }

