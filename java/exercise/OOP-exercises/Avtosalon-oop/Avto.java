package JavaProg2;

public class Avto extends Vozilo {
    int steviloVrat;

    public Avto(String znamka, double cena, int letoIzdelave, int steviloVrat){
        super(znamka, cena, letoIzdelave);
        this.steviloVrat= steviloVrat;
    }
    @Override
    public String toString(){
        return "Avto: " + znamka + ", цена: " + cena + ", год: " + letoIzdelave + ", дверей: " + steviloVrat;
    }

}
