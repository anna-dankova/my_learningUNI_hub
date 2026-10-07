package Vaje;

public class Vaja15 {

    public static void main(String[] args) {
        robKvadrata(9);
    }

    public static void robKvadrata(int n) {
        for (int i = 1; i < n; i++) {
            for (int j = 1; j < n; j++) {
                if (j > i) {
                    System.out.print(i);
                } else {
                    System.out.print(j);
                }
            }
            System.out.println();
        }
    }
}
