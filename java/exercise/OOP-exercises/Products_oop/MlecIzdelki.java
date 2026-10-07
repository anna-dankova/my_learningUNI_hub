package Lessons1.products;

public class MlecIzdelki extends Hrana{
    private double odstotekMascob;
    private boolean brezLaktoze;
    public MlecIzdelki(String naziv, double cena, double odstotekMascob, boolean brezLaktoze){
        super(naziv,cena);
        this.odstotekMascob=odstotekMascob;
        this.brezLaktoze=brezLaktoze;
        }
        @Override
        public String toString(){
            return super.toString() + ", Жира : " + odstotekMascob + "%" + ", Без лактозы : " + (brezLaktoze ? "да" : "нет"); 
        }
    }

