package JavaProg2;

import java.util.Scanner;
import java.util.HashMap;
import java.util.Map;

public class Exercise_12 {
    public static void main(String[] args) {

        Scanner myObj =new Scanner(System.in);
        Map<String, Integer> votes = new HashMap<>();
        
        System.out.println("Вводи имена (stop чтобы закончить):");

        while (true) {
            String name = myObj.nextLine();
            if (name.equals("stop")){
                break;
            } if (votes.containsKey(name)){
                votes.put(name, votes.get(name)+1);
            } else {votes.put(name, 1);}

        }
        System.out.println("Результаты : ");
        System.out.println(votes);

        myObj.close();

    }
}
