package Lessons1.products;

public class Hrana {
    private String naziv;
    private double cena;

    public Hrana(String naziv, double cena) {
        this.naziv = naziv;
        this.cena = cena;
    }

    public String getNaziv() {
        return naziv;
    }

    public double getCena() {
        return cena;
    }

    @Override
    public String toString() {
        return "Наименование: " + naziv + " , Цена: " + cena + " EUR ";
    }
}