package Lessons1.zoo;

import java.util.ArrayList;

public class Zoo {
    private ArrayList <Animal> animals = new ArrayList<>();

    public void  addAnimal(Animal a){
        animals.add(a);
    }
    public void printAll(){
        for (Animal a : animals){
            System.out.println(a.describe());
        }
    }
   public ArrayList<Animal> getDogs(){
        ArrayList <Animal> dog = new ArrayList<>();

        for (Animal a : animals){
        if(a instanceof Dog){
            dog.add(a);
            System.out.println(a.describe());
        }
        }
        return dog;
    }
    public void countByType() {
    int countDog = 0;
    int countCat = 0;
    int countBird = 0;

    for (Animal a : animals) {
        if (a instanceof Dog) {
            countDog++;
        } else if (a instanceof Cat) {
            countCat++;
        } else {
            countBird++;
        }
    }

    System.out.println("число собак: " + countDog);
    System.out.println("число котов: " + countCat);
    System.out.println("число птиц: " + countBird);}
    }

