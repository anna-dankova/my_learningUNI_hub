package Lessons2.Library;

public class Main {
    public static void main(String[] args) {
        Library myLibrary = new Library();
        myLibrary.addBook(new Book("Harry Potter", "J.K.Rowling", 1997, 320));

        myLibrary.addBook(new Book("The Hobbit", "J.R.R. Tolkien", 1937, 310));
        myLibrary.addBook(new Book("1984", "George Orwell", 1949, 328));
        myLibrary.addBook(new Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 180));
        myLibrary.addBook(new Book("To Kill a Mockingbird", "Harper Lee", 1960, 281));
        myLibrary.addBook(new Book("The Catcher in the Rye", "J.D. Salinger", 1951, 234));
        myLibrary.addBook(new Book("Crime and Punishment", "Fyodor Dostoevsky", 1866, 671));
        myLibrary.addBook(new Book("The Alchemist", "Paulo Coelho", 1988, 163));
        myLibrary.addBook(new Book("Dune", "Frank Herbert", 1965, 607));
        myLibrary.addBook(new Book("The Da Vinci Code", "Dan Brown", 2003, 454));
        myLibrary.addBook(new Book("The Little Prince", "Antoine de Saint-Exupery", 1943, 96));

        myLibrary.addMagazine(new Magazine("Time", "Time USA", 2024, 1025));
        myLibrary.addMagazine(new Magazine("The Economist", "Economist Group", 2023, 4421));
        myLibrary.addMagazine(new Magazine("Forbes", "Whale Media", 2024, 882));
        myLibrary.addMagazine(new Magazine("Vogue", "Conde Nast", 2023, 112));
        myLibrary.addMagazine(new Magazine("New Scientist", "Daily Mail Group", 2024, 1501));
        myLibrary.addMagazine(new Magazine("National Geographic", "Slo press", 2023, 14));

        System.out.println("Все книги :   ");
        myLibrary.readAll();

        System.out.println("Среднее количество страниц по книгам:   " + myLibrary.avgPages());
        System.out.println("Самая старая публикация :  " + myLibrary.oldestPub());
        System.out.println("Все книги :  ");
        myLibrary.readAllBooks();
    }
}
