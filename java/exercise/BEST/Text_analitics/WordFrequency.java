package Lessons1.Analitics;

public class WordFrequency {
    private String word;
    private int count;

    public WordFrequency(String word, int count){
        this.word=word;
        this.count=count;
    }

    public String getWord(){
        return this.word;
}
    public void incrementCount(){
        this.count++;
}
    public int getCount(){
        return this.count;
}
    
}