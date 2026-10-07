package Vaje;

public class Vaja17 {
    public static void main(String[] args) {
        piramida(5);
    }

    public static void piramida(int n) {
        for (int i = n; i >= 1; i--) {
            for (int j = 1; j <= (i - 1); j++) {
                System.out.print(" ");
            }
            if (i % 2 == 0) {
                for (int j = 1; j <= (2 * (n - i) + 1); j++) {
                    System.out.print("*");
                }
            } else {
                for (int j = 1; j <= (2 * (n - i) + 1); j++) {
                    System.out.print(i);
                }
            }
            for (int j = 1; j <= (i - 1); j++) {
                System.out.print(" ");
            }
            System.out.println();

        }
    }
}
