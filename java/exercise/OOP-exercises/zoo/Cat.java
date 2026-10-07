package Lessons1.zoo;

public class Cat extends Animal {
    public Cat(String name, int age){
        super(name, age);
    }
    @Override
    public String makeSound(){
        return "Мяу!";
    }
    @Override
    public String move(){
        return "крадётся бесшумно";
    }
}
