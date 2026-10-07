package JavaProg2;

public class Vozilo {
    String znamka;
    double cena;
    int letoIzdelave;

    public Vozilo(String znamka, double cena, int letoIzdelave) {
        this.znamka = znamka;
        this.cena = cena;
        this.letoIzdelave = letoIzdelave;
    }

    @Override
    public String toString() {
        return "Vozilo: " + znamka + ", цена: " + cena + ", год: " + letoIzdelave;
    }
}