package JavaProg2;

public class Exercise_2 {
    public static void main(String[] args) {
        int totalCandies = 23;
        int children = 5;
        int CandiesPerPerson= totalCandies / children;
        int outCandies = totalCandies%children;
        int a = totalCandies % CandiesPerPerson;

        System.out.println(CandiesPerPerson);
        System.out.println(outCandies);

        if (a==0) {
            System.out.println("Все конфеты разделены поровну!");}
            
        System.out.println("Остались лишние конфеты-" + outCandies);
    }
}
