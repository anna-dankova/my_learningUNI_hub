package BEST.Napitki;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

class Napitek {
    private String naziv;
    private double cena;

    public Napitek(String naziv, double cena) {
        this.naziv = naziv;
        this.cena = cena;
    }

    @Override
    public String toString() {
        return "Naziv: " + naziv + ", | Cena: " + cena;
    }

    public double getCena() {
        return cena;
    }
}

class Sok extends Napitek {
    private boolean brez_sladkorja;

    public Sok(String naziv, double cena, boolean brez_sladkorja) {
        super(naziv, cena);
        this.brez_sladkorja = brez_sladkorja;
    }

    @Override
    public String toString() {
        return super.toString() + ", | brez_sladkorja : " + (brez_sladkorja ? "da" : "ne");
    }
}

class GaziranaPijaca extends Napitek {
    private double volumen;
    private boolean brez_gasov;

    public GaziranaPijaca(String naziv, double cena, double volumen, boolean brez_gasov) {
        super(naziv, cena);
        this.volumen = volumen;
        this.brez_gasov = brez_gasov;
    }

    @Override
    public String toString() {
        return super.toString() + ", | volumen : " + volumen + ", | brez gasov : " + (brez_gasov ? "da" : "ne");
    }
}

class Sirup extends Napitek {
    private String barva;

    public Sirup(String naziv, double cena, String barva) {
        super(naziv, cena);
        this.barva = barva;
    }

    @Override
    public String toString() {
        return super.toString() + ", | barva : " + barva;
    }
}

public class Main {

    public static void main(String[] args) {
        ArrayList<Napitek> seznam = new ArrayList<>();
        String filename = "napitki.txt";

        try {
            BufferedReader br = new BufferedReader(new FileReader(filename));
            String line;

            while ((line = br.readLine()) != null) {
                if (line.startsWith("#") || line.trim().isEmpty()) {

                    continue;
                }

                String[] deli = line.split(",");
                for (int i = 0; i <= deli.length; i++) { // ==============
                    deli[i] = deli[i].trim();
                }
                String tip = deli[0];
                String naziv = deli[1];
                double cena = Double.parseDouble(deli[2]);

                switch (tip) {
                    case "*A":
                        seznam.add(new Napitek(naziv, cena));
                        break;

                    case "*B":
                        boolean brez_sladkorja = deli[3].equalsIgnoreCase("da");
                        seznam.add(new Sok(naziv, cena, brez_sladkorja));
                        break;

                    case "*C":
                        double volumen = Double.parseDouble(deli[3]);
                        boolean brez_gasov = deli[4].equalsIgnoreCase("da");
                        seznam.add(new GaziranaPijaca(naziv, cena, volumen, brez_gasov));
                        break;

                    case "*D":
                        String barva = deli[3];
                        seznam.add(new Sirup(naziv, cena, barva));
                        break;
                }
            }
            br.close();
        } catch (IOException e) {
            System.out.println("Napaka pri branju");
        }
        System.out.println("Vsi inapitki: ");
        for (int i = 0; i < seznam.size(); i++) {
            System.out.println(seznam.get(i));
        }
        double vsota = 0;
        int st = 0;
        System.out.println("Povprecna cena gaziranih pijac");

        for (int i = 0; i < seznam.size(); i++) {
            if (seznam.get(i) instanceof GaziranaPijaca) {
                vsota += seznam.get(i).getCena();
                st += 1;
            }
        }
        if (st > 0) {
            System.out.println(vsota / st);
        }
    }
}