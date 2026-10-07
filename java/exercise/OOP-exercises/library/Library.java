package Lessons2.Library;

import java.util.ArrayList;

public class Library {
    ArrayList<Publication> list = new ArrayList<>();

    public void addBook(Book b) {
        list.add(b);
    }

    public void addMagazine(Magazine m) {
        list.add(m);
    }

    public void readAll() {
        for (Publication p : list) {
            System.out.println(p);
        }
    }

    public Publication oldestPub() {
        Publication oldest = list.get(0);
        if (list.isEmpty()) {
            System.out.println("Список пуст");
        }
        for (Publication p : list) {
            if (p.getYear() < oldest.getYear()) {
                oldest = p;
            }
        }
        return oldest;
    }

    public void readAllBooks() {
        for (Publication p : list) {
            if (p instanceof Book) {
                System.out.println(p.toString() + "\n");
            }
        }
    }

    public int avgPages() {
        int avg = 0;
        int pages = 0;
        int count = 0;
        for (Publication p : list) {
            if (p instanceof Book) {
                count++;
                pages += ((Book) p).getCountPages();
            }
        }
        avg = pages / count;
        return avg;
    }
}