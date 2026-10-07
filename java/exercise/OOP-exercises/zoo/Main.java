package Lessons1.zoo;

public class Main {
    public static void main(String[] args) {
        Zoo zoo = new Zoo();

        zoo.addAnimal(new Dog("Рекс", 3));
        zoo.addAnimal(new Cat("Мурка", 2));
        zoo.addAnimal(new Bird("Кеша", 1, true));

        zoo.printAll();

        zoo.getDogs();
    }
}
