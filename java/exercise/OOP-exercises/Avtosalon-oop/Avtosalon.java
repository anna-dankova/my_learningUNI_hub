package JavaProg2;

import java.util.ArrayList;

public class Avtosalon {

    ArrayList<Vozilo>  seznam = new ArrayList<>();

    public void dodajVozilo(Vozilo v){
        seznam.add(v);
    }
    public void izpisiVsa(){
        for (Vozilo v : seznam){
            System.out.println(v);
        }
    }
    public Vozilo vrniNajdrazjeVozilo() {
        if (seznam.isEmpty()) return null;

        Vozilo najdrazje = seznam.get(0); 

        for (Vozilo v : seznam) {
            if (v.cena > najdrazje.cena) {
                najdrazje = v;
        }
    }
        return najdrazje;
        }
        }
    
