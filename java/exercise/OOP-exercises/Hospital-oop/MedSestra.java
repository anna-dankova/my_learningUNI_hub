package JavaProg2.Hospital;

public class MedSestra extends Oseba {
    String oddelek;
    public MedSestra(String name , String priimek, int starost, String oddelek){
        super(name, priimek, starost);
        this.oddelek = oddelek;}

        @Override
        public String toString(){
            return " Ime :" + name + " Priimek : " + priimek + " Starost : " + starost + " Oddelek : " + oddelek;
        }
}
