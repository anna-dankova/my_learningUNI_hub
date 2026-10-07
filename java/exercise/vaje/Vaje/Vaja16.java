package Vaje;

public class Vaja16 {
    public static void main(String[] args) {
        dolzina(5);
    }

    public static void dolzina(int n) {
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < (i - 1); j++) {
                System.out.print("*");
            }
            System.out.print(i);

            for (int j = 0; j <= (((n - i) * 2) - 2); j++) {
                System.out.print(" ");
            }
            if (i != n) {
                System.out.print(i);
            }
            for (int j = 0; j < (i - 1); j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
