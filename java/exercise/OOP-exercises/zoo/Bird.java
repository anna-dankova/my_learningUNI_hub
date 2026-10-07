package Lessons1.zoo;

public class Bird extends Animal{
    private boolean canFly;
    public Bird(String name, int age, boolean canFly){
        super(name, age);
        this.canFly=canFly;
    }
    @Override
    public String makeSound(){
        return "Чирик!";
    }
    @Override
    public String move(){
        return canFly ? "летит по воздуху" : "прыгает по земле";
    }
}
