package Lessons1.products;

public class Kruh extends Hrana{
    private boolean brezKvasa;
    public Kruh(String naziv, double cena, boolean brezKvasa){
        super(naziv, cena);
        this.brezKvasa=brezKvasa;
    }
    @Override
    public String toString(){
        return super.toString() + ",Без дрожжей: " + (brezKvasa ? "да" : "нет");
    }
}
