package Vaje;

public class Vaja18 {
    public static void main(String[] args) {
        diamant(9);
    }

    public static void diamant(int n) {
        if (n % 2 == 0 || n < 1) {
            return;
        }
        int sredina = n / 2;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (Math.abs(i - sredina) + Math.abs(j - sredina) == sredina) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }

    }
}
