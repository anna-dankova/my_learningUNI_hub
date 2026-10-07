package Lessons1.Analitics;

import java.util.ArrayList;

public class AdvancedTextAnalyzer extends TextMetrics {
    ArrayList<WordFrequency> list = new ArrayList<>();

    public void analyze(String text) {
        list.clear();

        countSim = text.length();
        countLine = text.split("\\R").length;
        countWord = text.split("\\s+").length;

        String cleanText = text.toLowerCase().replaceAll("[\\p{N}+ \\p{L}+ ]", "");
        String[] words = cleanText.split(" ");

        for (String w : words) {
            if (w.length() < 3) {
                continue;
            }
            boolean found = false;
            for (WordFrequency wf : list) {
                if (wf.getWord().equals(w)) {
                    wf.incrementCount();
                    found = true;
                    break;
                }
            }
            if (!found) {
                WordFrequency newCard = new WordFrequency(w, 1);
                list.add(newCard);
            }
        }
    }

    public void printTopWords() {
        if (list.isEmpty()) {
            System.out.println("Список слов пуст. Сначала запустите analyze().");
            return;
        }
        int topN = 3;
        System.out.println("\n--- ТОП " + topN + " САМЫХ ЧАСТЫХ СЛОВ ---");

        list.sort((w1, w2) -> Integer.compare(w2.getCount(), w1.getCount()));
        int limit = Math.min(topN, list.size());
        for (int i = 0; i < topN; i++) {
            WordFrequency wf = list.get(i);
            System.out.println((i + 1) + ". " + wf.getWord() + " ->" + wf.getCount() + "раз(а)");
        }
    }

}