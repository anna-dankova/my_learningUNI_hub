package Lessons1.products;

public class Sadje extends Hrana {
   private String barva;
   public Sadje(String naziv, double cena, String barva){
    super(naziv, cena);
    this.barva=barva;
   }
   @Override
   public String toString(){
    return super.toString() + ", Цвет : " + barva;
   }
    }

