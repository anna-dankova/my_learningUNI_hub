package Izpiti;

import java.util.ArrayList;

public class izpit1_20junij2022 {
    // naloga 1
    /*
     * return - zakljuci celo metodo in vrne vrednost
     * break - zakljuci del kode kjer je. ce je switch pride do naslednjega case
     * continue - spusti del ki je ostal in gre k naslednjemu delu
     */

    // naloga 2
    public static int[] vsota(int[][] matrika) {
        int n = matrika.length;
        int[] rezultat = new int[n];

        for (int i = 0; i < n; i++) {
            int vsotaVrstice = 0;
            int vsotaStolpca = 0;

            for (int j = 0; j < n; j++) {
                vsotaVrstice += matrika[i][j];
                vsotaStolpca += matrika[j][i];
            }
            rezultat[i] = vsotaVrstice + vsotaStolpca;
        }
        return rezultat;
    }

    // naloga 2.1
    public static int[] razlika(int[][] matrika) {
        int n = matrika.length;
        int[] rezultat = new int[n];

        for (int i = 0; i < n; i++) {
            int razlikaVrstice = 0;
            int razlikaStolpce = 0;

            for (int j = 0; j < n; j++) {
                razlikaVrstice += matrika[i][j];
                razlikaStolpce += matrika[j][i];
            }
            rezultat[i] = razlikaVrstice - razlikaStolpce;
        }
        return rezultat;
    }

    // naloga 2.2
    public static int[] vsotaLihih(int[][] matrika) {
        int n = matrika.length;
        int[] rezultat = new int[n];

        for (int i = 0; i < n; i++) {
            int vsotaVrstice = 0;
            int vsotaStolpca = 0;
            for (int j = 0; j < n; j++) {
                if (matrika[i][j] % 2 != 0) {
                    vsotaVrstice += matrika[i][j];
                }
                if (matrika[j][i] % 2 != 0) {
                    vsotaStolpca += matrika[j][i];
                }
            }
            rezultat[i] = vsotaStolpca + vsotaVrstice;
        }
        return rezultat;
    }

    // naloga 3
    public static void diamant(int n) {
        if (n % 2 == 0 || n < 1) {
            return;
        }
        int middle = n / 2;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (Math.abs(i - middle) + Math.abs(j - middle) == middle) {
                    System.out.print("*");
                } else {
                    System.out.print(" ");
                }
            }
            System.out.println();
        }

    }
    // naloga 5

    public class Pesem {
        String songName;
        String autorName;
        int minuts;

        public Pesem(String songName, String authorName, int minutes) {
            this.songName = songName;
            this.autorName = authorName;
            this.minuts = minutes;

        }

        public String getSongName() {
            return songName;
        }

        public String getAuthorName() {
            return autorName;
        }

        public int getMinutes() {
            return minuts;
        }

        @Override
        public String toString() {
            return "Song : " + songName + " , | Author : " + autorName + " , Minutes : " + minuts;
        }
    }

    public class Zgoscenka {
        private ArrayList<Pesem> seznamPesmi;

        public Zgoscenka(ArrayList<Pesem> seznamPesmi) {
            this.seznamPesmi = seznamPesmi;
        }

        public void dodajPesem(Pesem p) {
            seznamPesmi.add(p);
            System.out.println("Song was added on CD");
        }

        public int steviloPesmi() {
            return seznamPesmi.size();
        }

        public int izpisi(int minutes) {
            for (Pesem p : seznamPesmi) {
                if (minutes > p.minuts) {
                    seznamPesmi.get(i).toString();
                }
            }
        }
    }

    public static void main(String[] args) {
        ArrayList<Pesem> zacetniSeznam = new ArrayList<>();
        Zgoscenka mojDisk = new Zgoscenka(zacetniSeznam);

        // Создаем 3 песни (название, исполнитель, минуты)
        Pesem p1 = new Pesem("Bohemian Rhapsody", "Queen", 6);
        Pesem p2 = new Pesem("Yesterday", "The Beatles", 2);
        Pesem p3 = new Pesem("Believer", "Imagine Dragons", 3);

        // Добавляем их на диск с помощью нашего метода
        mojDisk.dodajPesem(p1);
        mojDisk.dodajPesem(p2);
        mojDisk.dodajPesem(p3);

        // Проверяем сколько песен добавилось
        System.out.println("Песен на диске: " + mojDisk.steviloPesmi()); // Выведет 3

        // Тестируем фильтр: вывести песни короче 4 минут
        System.out.println("--- Песни короче 4 минут ---");
        mojDisk.izpisi(4);
    }

}
