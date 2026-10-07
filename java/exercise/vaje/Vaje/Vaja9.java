package Vaje;

public class Vaja9 {
   public static void main(String[] args) {
       String text = "my name is Givanni Georgio";
       String lower = text.toLowerCase().substring(11);
       System.out.println(lower);
       String splitted[] = text.split(" ");
        for (String i : splitted){
            System.out.println("Слово " + i + " имеет " + i.length()+ " букв");
        }
   }
}
