package JavaProg2.Hospital;

public class Main {
    public static void main(String[] args) {
        Bolnisnica hospital = new Bolnisnica();

        hospital.dodajOsebo(new Zdravnik("Tomaz","Kril" , 45, "surgeon"));
         hospital.dodajOsebo(new Zdravnik("Ana", "Novak", 38, "кардиолог"));
        hospital.dodajOsebo(new Zdravnik("Marko", "Horvat", 52, "невролог"));
        hospital.dodajOsebo(new Zdravnik("Elena", "Kovač", 61, "педиатр"));

    // Медсёстры
        hospital.dodajOsebo(new MedSestra("Sara", "Zupan", 29, "реанимация"));
        hospital.dodajOsebo(new MedSestra("Maja", "Bernik", 34, "хирургия"));
        hospital.dodajOsebo(new MedSestra("Tina", "Oblak", 47, "терапия"));
        hospital.dodajOsebo(new MedSestra("Nina", "Krajnc", 25, "педиатрия"));

        hospital.izpisiVse();
        System.out.println("---------------------");
        System.out.println(hospital.vrniNajstarejsega());
        
    }
}
