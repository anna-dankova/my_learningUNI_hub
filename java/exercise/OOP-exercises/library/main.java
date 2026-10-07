package Lessons1.library;

import java.util.ArrayList;
import java.util.Comparator;
import java.util.Scanner;

import Lessons1.library.book.Book;

public class main {
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in);
        ArrayList<Book> library = new ArrayList<>();
        library.add(new Book("Мастер и маргарита", "Михаил Булгаков", 1940));
        library.add(new Book("Преступление и наказание", "Федор Достоевский", 1866));
        library.add(new Book("Собачье сердце", "Михаил Булгаков", 1925));
        library.add(new Book("Капитанская дочка", "Александр Пушкин", 1836));
        library.add(new Book("Герой нашего времени", "Михаил Лермонтов", 1840));
        library.add(new Book("Мертвые души", "Николай Гоголь", 1842));
        library.add(new Book("Война и мир", "Лев Толстой", 1867));
        library.add(new Book("Отцы и дети", "Иван Тургенев", 1862));
        library.add(new Book("Белая гвардия", "Михаил Булгаков", 1925));
        library.add(new Book("Руслан и Людмила", "Александр Пушкин", 1820));

        library.sort(Comparator.comparingInt(Book::getDate));

        while (true) {
            System.out.println("1.Показать все книги");
            System.out.println("2.Найти книгу");
            System.out.println("3.Добавить книгу");
            System.out.println("4.Выход");

            System.out.println("Выбор:");
            int choise = myObj.nextInt();
            myObj.nextLine();

            switch (choise) {
                case 1:
                    System.out.println("--Books--");
                    for (Book b : library) {
                        System.out.println(b.getName() + "---" + b.getAuthor() + "  (" + b.getDate() + "г.)");
                    }
                    break;
                case 2:
                    System.out.println("Введите автора:");
                    String searchAuthor = myObj.nextLine();
                    for (Book b : library) {
                        if (b.getAuthor().toLowerCase().contains(searchAuthor.toLowerCase())) {
                            System.out.println(b.getName() + "---" + b.getAuthor() + "  (" + b.getDate() + "г.)");
                        }
                    }
                    break;
                case 3:
                    System.out.println("Введите название:");
                    String inName = myObj.nextLine();
                    System.out.println("Введите автора:");
                    String inAuthor = myObj.nextLine();
                    System.out.println("Введите год:");
                    int inDate = myObj.nextInt();
                    myObj.nextLine();
                    library.add(new Book(inName, inAuthor, inDate));
                    System.out.println("Книга добавлена !");
                    break;

                case 4:
                    break;
                default:
                    System.out.println("Введите число от 1 до 4:");
                    break;
            }

        }

    }

}
