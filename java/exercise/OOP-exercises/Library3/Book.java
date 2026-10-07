package Lessons2.Library;

public class Book extends Publication {
    int countPages;

    public Book(String name, String avtor, int year, int countPages) {
        super(name, avtor, year);
        this.countPages = countPages;
    }

    public int getCountPages() {
        return this.countPages;
    }

    @Override
    public String toString() {
        return super.toString() + " | Количество стр : " + countPages;
    }
}
