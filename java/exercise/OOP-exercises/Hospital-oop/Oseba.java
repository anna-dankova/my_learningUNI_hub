package JavaProg2.Hospital;

public class Oseba {
String name;
String priimek;
int starost;
    public  Oseba(String name, String priimek, int starost){
        this.name = name;
        this.priimek= priimek ;
        this.starost= starost;}

        @Override
        public String toString(){
            return " Ime :" + name + "Priimek : " + priimek + "Starost : " + starost;
        }
}
