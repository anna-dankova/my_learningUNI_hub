package JavaProg2;

public class Exercise_6 {
    public static void main(String[] args) {
        int n = 7;
        for (int i = 0; i < n; i++) {
            
            for (int j = 0; j < n; j++) {
                if ((j >= i && j <= n - 1 - i) || (j >= n - 1 - i && j <= i)) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println(); 
        }
    }
}