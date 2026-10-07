package Lessons1.zoo;
public abstract class Animal{
    protected String name;
    protected int age;

    public Animal(String name , int age){
        this.name=name;
        this.age=age;

    }
    public abstract String makeSound();
    public abstract String move();

    public String describe(){
        return String.format("%s (%d лет): звук — %s, движение — %s",
                name, age, makeSound(), move());

    }
    public String getName(){ 
        return name;
    }
}