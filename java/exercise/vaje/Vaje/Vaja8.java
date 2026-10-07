package Vaje;

public class Vaja8 {
    static void main(String[] args) {
        // Deklarirajte tri celoˇstevilske spremenljivke s poljubno vrednostjo.
        //Nato z uporabo if stavka na zaslon izpiˇsite najveˇcje ˇstevilo med
        //njimi
        int[] num = {1, 33, 77};
        int max = 0;
        for (int i : num) {
            if (i > max) {
                max = i;
            }
        }
        System.out.println("Самое большое число :" + max);
    }
}