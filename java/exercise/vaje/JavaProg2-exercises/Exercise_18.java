package JavaProg2;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

public class Exercise_18 {
    public static void main(String[] args) {
        Map<String, Integer> map = new HashMap<>();
        map.put("Яблоки", 100);
        map.put("Бананы", 150);
        map.put("Апельсины", 200);
        ArrayList<Integer> list = new ArrayList<>(map.values()) ;
        System.out.println("Итоговая сумма: " + sumRecursive(list, 0));
    }
    public static int  sumRecursive(ArrayList<Integer> list, int i){
        if (i == list.size()) {
        return 0;}
        return list.get(i) + sumRecursive(list, i+1) ;
    }
}
