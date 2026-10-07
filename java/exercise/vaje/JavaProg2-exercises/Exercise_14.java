package JavaProg2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.PrintWriter;
import java.util.HashMap;
import java.util.Map;

public class Exercise_14 {
    public static void main(String[] args) {
        countWords("C:\\_\\Dev\\JavaExercise\\exercise\\JavaProg2\\notes.txt", "C:\\_\\Dev\\JavaExercise\\exercise\\JavaProg2\\result.txt");}

        public static void countWords(String inputPath, String outputPath) {
        try {
            BufferedReader reader= new BufferedReader(new FileReader(inputPath));
            Map<String, Integer> words = new HashMap<>();
            String line;

            while ((line = reader.readLine()) != null) {
                String[] arr = line.split(" ");
                for (String word :arr){
                    if (words.containsKey(word)){
                        words.put(word, words.get(word)+1);
                    } else {words.put(word, 1);}
            }} 


            PrintWriter writer = new PrintWriter(outputPath);
            for( String word : words.keySet()) {
                int count = words.get(word);
                writer.println( word + " встретилось " + count + " раз");
            }
            writer.close();
            reader.close();
        } catch (Exception e) {
            System.out.println(e.getMessage());
        }
    }
}
