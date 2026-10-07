package JavaProg2;

public class Exercise_20 {
    public static void main(String[] args) {
        Avtosalon salon = new Avtosalon();

        salon.dodajVozilo(new Avto("BMW", 25000, 2020, 4));
        salon.dodajVozilo(new Avto("Fiat", 8000, 2015, 3));
        salon.dodajVozilo(new Kamion("Volvo", 75000, 2019, 20.5));
        salon.dodajVozilo(new Kamion("MAN", 60000, 2018, 15.0));

        System.out.println("=== Все транспортные средства ===");
        salon.izpisiVsa();

        System.out.println("\n=== Самое дорогое ===");
        System.out.println(salon.vrniNajdrazjeVozilo());
    }
}
