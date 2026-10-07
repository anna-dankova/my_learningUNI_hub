package JavaProg2;

public class Exercise_5 {
    public static void main(String[] args) {
        int [] numbers = {45,22,7,56,19,28};
        int[] sorted =  numbers;
        for (int i = 0; i < sorted.length-1; i++) {
            for (int j = 0; j < sorted.length - 1- i; j++) {
                if (sorted[j]>sorted[j+1]){
                    int temp =sorted[j];
                    sorted[j] = sorted[j+1];
                    sorted[j+1]= temp;
                }
            }
        }
        System.out.println("sorted:");
        for (int i = 0; i < sorted.length; i++) {
            System.out.println(sorted[i] + " ");
        }
        
    }
}