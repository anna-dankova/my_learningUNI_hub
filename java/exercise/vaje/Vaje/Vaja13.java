package Vaje;

public class Vaja13 {
    public static void main(String[] args) {
        char[] znaki = {'a', 'b', 'a', 'c', 'b', 'd'};
        int[] count = new int[znaki.length]; // счётчик для каждого знака
        for (int i = 0; i < znaki.length; i++) {
            for (int j = 0; j < znaki.length; j++) {
                if (znaki[i] == znaki[j]){
                    count[i]++;
                }
            }
        }
        for (int i = 0; i < znaki.length; i++) {
            if ( count[i] == 1){
                System.out.println(znaki[i]);
            }
        }
    }
}
