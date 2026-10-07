package JavaProg2;

public class Exercise_4 {
    public static void main(String[] args) {
        int originalNumber= 12322;
        int temp = originalNumber;
        int reversed =0;
        while (originalNumber != 0) {
            int digit = originalNumber % 10;
            reversed = reversed * 10 +  digit;
            originalNumber = originalNumber / 10;
        }

        if (temp == reversed) { System.out.println("its polindrom number:" + reversed);}
        else {System.out.println("no: " + reversed);}
    }
}