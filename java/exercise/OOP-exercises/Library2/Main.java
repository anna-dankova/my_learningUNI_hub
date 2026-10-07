package Lessons2.Library2;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

import Lessons1.library.book;

class Knjiga {
    private String naziv;
    private String avtor;
    private double cena;

    public Knjiga(String naziv, String avtor, double cena) {
        this.naziv = naziv;
        this.avtor = avtor;
        this.cena = cena;
    }

    @Override
    public String toString() {
        return "Naziv : " + naziv + "| Avtor : " + avtor + "| Cena : " + cena;
    }

    public double getCena() {
        return this.cena;
    }
}

class TiskanaKnjiga extends Knjiga {
    private int steviloStrani;

    public TiskanaKnjiga(String naziv, String avtor, double cena, int steviloStrani) {
        super(naziv, avtor, cena);
        this.steviloStrani = steviloStrani;
    }

    @Override
    public String toString() {
        return super.toString() + "| Stevilo strani : " + steviloStrani;
    }

    public int getSteviloStrani() {
        return this.steviloStrani;
    }
}

class Eknjiga extends Knjiga {
    private double velikostMB;

    public Eknjiga(String naziv, String avtor, double cena, double velikostMB) {
        super(naziv, avtor, cena);
        this.velikostMB = velikostMB;
    }

    @Override
    public String toString() {
        return super.toString() + "| Velikost v mb : " + velikostMB;
    }

    public double getVelikostMB() {
        return this.velikostMB;
    }
}

class Comics extends Knjiga {
    private String ilustrator;
    private boolean BWcolor;

    public Comics(String naziv, String avtor, double cena, String ilustrator, boolean BWcolor) {
        super(naziv, avtor, cena);
        this.ilustrator = ilustrator;
        this.BWcolor = BWcolor;
    }

    @Override
    public String toString() {
        return super.toString() + "| ilustrator : " + ilustrator + "| Color : " + (BWcolor ? "Color" : "BlackWhite");
    }

    public String getColor() {
        return (BWcolor ? "Color" : "BlackWhite");
    }
}

public class Main {
    public static void main(String[] args) {
        ArrayList<Knjiga> seznam = new ArrayList<>();

        try {
            BufferedReader br = new BufferedReader(new FileReader("library.txt"));
            String line;

            while ((line = br.readLine()) != null) {
                if (line.startsWith("#") || line.trim().isEmpty()) {
                    continue;
                }
                String[] deli = line.split(",");
                for (int i = 0; i < deli.length; i++) {
                    deli[i] = deli[i].trim();
                }
                String tip = deli[0];
                String naziv = deli[1];
                String avtor = deli[2];
                double cena = Double.parseDouble(deli[3]);

                switch (tip) {
                    case "*A":
                        seznam.add(new Knjiga(naziv, avtor, cena));
                        break;
                    case "*B":
                        int steviloStrani = Integer.parseInt(deli[4]);
                        seznam.add(new TiskanaKnjiga(naziv, avtor, cena, steviloStrani));
                        break;
                    case "*C":
                        double velikostMB = Double.parseDouble(deli[4]);
                        seznam.add(new Eknjiga(naziv, avtor, cena, velikostMB));
                        break;
                    case "*D":
                        String ilustrator = deli[4];
                        boolean barva = Boolean.parseBoolean(deli[5]);
                        seznam.add(new Comics(naziv, avtor, cena, ilustrator, barva));
                        break;

                    default:
                        break;
                }
            }
            br.close();
        } catch (IOException e) {
            System.out.println("Napaka pri branju");
        }
        System.out.println("-------vse knjige:-------");
        for (int i = 0; i < seznam.size(); i++) {
            System.out.println(seznam.get(i));
        }
        double vsota = 0;
        int st = 0;

        for (int i = 0; i < seznam.size(); i++) {
            if (seznam.get(i) instanceof Eknjiga) {
                vsota += seznam.get(i).getCena();
                st += 1;
            }
        }
        int sum = 0;
        for (int i = 0; i < seznam.size(); i++) {
            if (seznam.get(i) instanceof TiskanaKnjiga) {
                TiskanaKnjiga knjiga = (TiskanaKnjiga) seznam.get(i);
                sum += knjiga.getSteviloStrani();
            }

        }
        System.out.println("srednja cena vseh el. knjig: " + (vsota / st));
        System.out.println("sum str vseh tisk. knjig: " + (sum));

    }
}
