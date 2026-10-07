package Izpiti;

import java.util.ArrayList;
import java.util.Arrays;

import Lessons1.library.book;

public class Izpit2_19junij2023 {

    // // naloga 1
    // /*
    // Nadrazred - razred starsa , ostali razredi lahko dedujejo lastnosti
    // Podrazred - novi razred ki extends polja razreda starsa in lahko se ima svoja
    // polja
    // */
    // class Zivali {
    // String ime;

    // public Zivali(String ime) {
    // this.ime = ime;
    // }
    // }

    // class Pes extends Zivali {
    // public Pes(String name) {
    // super(name);
    // }
    // }

    // class Macka extends Zivali {
    // public Macka(String ime) {
    // super(ime);
    // }
    // }

    // naloga 2
    // a=5;b=15;x=1;

    // naloga 3
    // int n = 3;
    // 6 7 11
    // 8 9 11
    // 10 11 11
    // 12 13 11
    // 14 15 11
    // 16

    // naloga 3
    // public static void okno(int n) {
    // int sirina = 2 * n + 3;

    // for (int i = 0; i < sirina; i++) {
    // System.out.print("*");
    // }
    // System.out.println();

    // for (int i = 0; i < n; i++) {
    // System.out.print("*");

    // for (int j = 0; j < n; j++) {
    // System.out.print(" ");
    // }
    // System.out.print("*");

    // for (int j = 0; j < n; j++) {
    // System.out.print(" ");
    // }
    // System.out.print("*");
    // System.out.println();
    // }
    // for (int i = 0; i < sirina; i++) {
    // System.out.print("*");
    // }
    // System.out.println();
    // }

    // naloga 4
    public class Predstava {
        String imePredstave;
        int dozinaMinut;
        int stNastopajocih;
        boolean zaOtroke;

        public Predstava(String imePredstave, int dozinaMinut, int stNastopajocih, boolean zaOtroke) {
            this.imePredstave = imePredstave;
            this.dozinaMinut = dozinaMinut;
            this.stNastopajocih = stNastopajocih;
            this.zaOtroke = zaOtroke;
        }

        public int getMinutes() {
            return dozinaMinut;
        }

        public String getImePredstave() {
            return imePredstave;
        }

        public int getStNastopajocih() {
            return stNastopajocih;
        }

        public boolean jeZaOtroke() {
            return zaOtroke;
        }

        @Override
        public String toString() {
            return "ime predstave :" + imePredstave + " Dolzina predstave : " + dozinaMinut + " Stevilo nastopajocih : "
                    + stNastopajocih + " ali je za otroke :" + (zaOtroke ? "Da" : "ne");
        }
    }

    public class Gledalisce {
        private ArrayList<Predstava> seznam;

        public Gledalisce(ArrayList<Predstava> seznam) {
            this.seznam = seznam;
        }

        public void dodajPredstavo(Predstava p) {
            seznam.add(p);
        }

        public int dolzinaVsehPredstav() {
            int skupnoMin = 0;
            for (Predstava p : seznam) {
                skupnoMin += p.getMinutes();
            }
            return skupnoMin;
        }

        public void izpisi(int nastopajoce) {
            for (Predstava p : seznam) {
                if (p.getStNastopajocih() == nastopajoce) {
                    System.out.println(p.toString());
                }
            }
        }
    }

    public static void main(String[] args) {
        ArrayList<Predstava> zacetnaPredstava = new ArrayList<>();
        Gledalisce gledalisce = new Gledalisce(zacetnaPredstava);

        gledalisce.dodajPredstavo(new Predstava("Snegulcica", 120, 5, true));
        gledalisce.dodajPredstavo(new Predstava("hamlet", 70, 7, false));
        gledalisce.dodajPredstavo(new Predstava("Pika Nogavicka", 45, 11, true));
        gledalisce.dodajPredstavo(new Predstava("Kekec", 45, 15, true));

        System.out.println("Skupna dolzina :" + gledalisce.dolzinaVsehPredstav());
        System.out.println("Otroške predstave z vsaj 10 nastopajočimi:");
        gledalisce.izpisi(10);
    }


    //naloga 5

    public static int neVsebuje(int[] tabela) {
        Arrays.sort(tabela);
        return preveri(tabela, 1);
    }

    private static int preveri(int[] tabela, int st) {
        if (st > 100) {
            return 0;
        }
        boolean neVsebuje = Arrays.binarySearch(tabela, st) < 0;
        System.out.print(neVsebuje ? st + "\n" : " ");
        int vsota = neVsebuje ? st : 0;
        return vsota + preveri(tabela, st + 1);
    }
    }

