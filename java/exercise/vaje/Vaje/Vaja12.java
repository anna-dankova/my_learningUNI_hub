package Vaje;

import java.util.Random;

public class Vaja12 {
    public static void main(String[] args) {
    int now = 0;
    int max = 0;
    for (int i = 0; i < 100; i++) {
        Random rand = new Random();
        int brosCoin = rand.nextInt(2); // даёт 0 или 1
       
        if (brosCoin == 1 ) {
            now++;
            if ( now > max){
                max=now;
            }
        }else {
            now =0;
        }
    }
    System.out.println("Najdaljša serija: " + max);
 } 

}
