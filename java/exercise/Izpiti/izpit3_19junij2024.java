package Izpiti;

import java.util.ArrayList;

public class izpit3_19junij2024 {
    // naloga 1
    // if- preveri ali velja pogoj . lahko dodamo neskoncno st else if in na koncu
    // else brez pogoja
    // int starost;
    // if ( starost <18){
    // System.out.println("se ni polnoleten");
    // }
    // else if(starost==18)
    // {
    // System.out.println("ze polnoleten");
    // }else{
    // System.out.println("starejsi od 18");
    // }

    // for- lahko gremo po seznamu en po enem
    // for(int st : seznam){
    // System.out.println(st);
    // }

    /// while - velja dokler velja pogoj. ce ze v prvem ciklu ni true , cikl
    /// se zakljuci
    // while(a ==true){
    // return true};

    // do-while - cikl se izpolni vsaj enkrat in lahko se potem zakljuci. prvo gre
    // do po tem while
    // do{System.out.print(seznam[i])i++;
    // }while(i>seznam.length);

    // naloga 2

    // public static int vsotaKvadratovSodih(ArrayList<Integer> seznam) {
    // seznam.removeIf(st -> st % 2 != 0);

    // int kvadrate = 0;
    // for (int st : seznam) {
    // kvadrate += st * st;
    // }
    // return kvadrate;
    // }

    // naloga 3
    public static class Predstava {
        String naslovPredstave;
        String avtor;
        int uraPrecetka;
        double casTrajanja;

        public Predstava(String naslovPredstave, String avtor, int uraPrecetka, double casTrajanja) {
            this.naslovPredstave = naslovPredstave;
            this.avtor = avtor;
            this.uraPrecetka = uraPrecetka;
            this.casTrajanja = casTrajanja;
        }

        public String getNaslovPredstave() {
            return naslovPredstave;
        }

        public int getUroPrecetka() {
            return uraPrecetka;
        }

        public double getCasTrajanja() {
            return casTrajanja;
        }

        @Override
        public String toString() {
            return "Naslov predstave : " + naslovPredstave + "Ura precetka : " + uraPrecetka + "cas trajanja"
                    + casTrajanja;
        }
    }

    public static class Gledalisce {
        String imeGledalisca;
        ArrayList<Predstava> predstave;

        public Gledalisce(String imeGledalisca) {
            this.imeGledalisca = imeGledalisca;
            this.predstave = new ArrayList<>();
        }

        public void dodajPredstavo(Predstava p) {
            predstave.add(p);
        }

        public void izpisi(int ura) {
            System.out.println("Predstave v gledališču \"" + imeGledalisca + "\", ki se končajo pred " + ura + ":00:");

            for (Predstava p : predstave) {
                double casKonca = p.getUroPrecetka() + p.getCasTrajanja();
                if (casKonca < ura) {
                    p.toString();
                }

            }
        }
    }

    public static void main(String[] args) {
        Gledalisce gledalisce = new Gledalisce("Slovensko narodno gledališče");
        gledalisce.dodajPredstavo(new Predstava("romeo in julija", "william Shakespeare", 17, 1.5));
        gledalisce.dodajPredstavo(new Predstava("Kralj Ubu", "Alfred Jarry", 19, 1.5));
        gledalisce.dodajPredstavo(new Predstava("Hlači", "Ivan Cankar", 16, 2.0));

        gledalisce.izpisi(20);
    }

    // naloga5

}