package Lessons1.zoo;

public class Dog extends Animal{
    public Dog(String name, int age ){
        super(name, age);
    }
    @Override
    public String makeSound(){
        return "Гав!";
    }
    @Override
    public String move() {
        return "бежит на четырёх лапах";
    }

}
