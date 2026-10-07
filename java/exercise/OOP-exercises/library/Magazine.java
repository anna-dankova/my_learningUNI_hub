package Lessons2.Library;

public class Magazine extends Publication {
    int idMagazine;

    public Magazine(String name, String avtor, int year, int idMagazine) {
        super(name, avtor, year);
    }

    public int getIdMagazine() {
        return this.idMagazine;
    }

    @Override
    public String toString() {
        return super.toString() + "|Стриниц : " + idMagazine;
    }
}
