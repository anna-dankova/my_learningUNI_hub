package Lessons1.library;
// 2. Библиотека простых книг
// Создай класс Book и программу, которая хранит несколько книг в ArrayList.
// Сейчас: добавить книгу, вывести все книги, найти книгу по автору.
// Потом: добавить сортировку по году и поиск по части названия.


public class book {
   
    static class Book{
        private String name ;
        private String author;
        private int date;

        Book(String name, String author, int date){
            this.name=name;
            this.author=author;
            this.date=date;

        }
    public String getName(){
        return name;
    }
    public String getAuthor(){
        return author;
    }
    public int getDate(){
        return date;
    }
    }
}