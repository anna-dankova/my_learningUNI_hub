package JavaProg2;

public class Exercise_3 {
    public static void main(String[] args) {

        int computerChoice = (int)(Math.random() * 3) + 1;
        int userChoice = (int)(Math.random() * 3) + 1;;
        
        switch (computerChoice) {
            case 1:
                System.out.println("Комьютер :"+"Камень");
                break;
            case 2:
                System.out.println("Комьютер :"+"Ножницы");
                break;
            case 3:
                System.out.println("Комьютер :"+"Бумага");
                break;
        }
        
        switch (userChoice) {
            case 1:
                System.out.println("Вы :"+"Камень");
                break;
            case 2:
                System.out.println("Вы :"+"Ножницы");
                break;
            case 3:
                System.out.println("Вы :"+"Бумага");
                break;
        }
        
        if (userChoice == computerChoice) {
            System.out.println("Ничья");
        }
        else if ((userChoice == 1 && computerChoice == 2) || 
                 (userChoice == 2 && computerChoice == 3) || 
                 (userChoice == 3 && computerChoice == 1)) {
            System.out.println("Вы победили!");
        }
        else {
            System.out.println("Компьютер победил!");
        }
    }
}