package Lessons2.Library;

public class Publication {
    String name;
    String avtor;
    int year;

    public Publication(String name, String avtor, int year) {
        this.name = name;
        this.avtor = avtor;
        this.year = year;
    }

    public String getName() {
        return this.name;
    }

    public String getAvtor() {
        return this.avtor;
    }

    public int getYear() {
        return this.year;
    }

    @Override
    public String toString() {
        return "Название : " + name + "|  Автор : " + avtor + "|  Год выхода:" + year;
    }
}
