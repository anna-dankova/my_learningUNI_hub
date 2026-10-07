package Lessons1.Analitics;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class Main {

    public static String readFile(String path) {
        StringBuilder sb = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader(path))) {
            String line;
            while ((line = br.readLine()) != null) {
                sb.append(line);
            }
        } catch (IOException e) {
            System.out.println("Ошибка при чтении файла: " + e.getMessage());
            return "";
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        String testText = readFile("./input.txt");

        AdvancedTextAnalyzer analyzer = new AdvancedTextAnalyzer();
        analyzer.analyze(testText);

        System.out.println("Символов посчитано: " + analyzer.getcountSim());
        System.out.println("Строк посчитано: " + analyzer.getcountLine());

        analyzer.printTopWords();

    }

}
