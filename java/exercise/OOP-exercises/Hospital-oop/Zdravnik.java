package JavaProg2.Hospital;

public class Zdravnik  extends Oseba{
    String specialist; 

    public Zdravnik(String name, String priimek, int starost, String specialist){
    super(name, priimek, starost);
        this.specialist= specialist;}

    @Override
    public String toString(){
        return " Ime :" + name + " Priimek : " + priimek + " Starost : " + starost + " Specialnost : " + specialist;
    }
}