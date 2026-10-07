

package JavaProg2;

public class Kamion extends Vozilo {
    double nosilnost;

    public Kamion(String znamka, double cena, int letoIzdelave, double nosilnost) {
        super(znamka, cena, letoIzdelave);
        this.nosilnost = nosilnost;
    }

    @Override
    public String toString() {
        return "Kamion: " + znamka + ", цена: " + cena + ", год: " + letoIzdelave + ", грузоподъёмность: " + nosilnost + "т";
    }
}
