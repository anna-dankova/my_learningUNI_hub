package TechShopPet;


public class Laptop extends Product {
    protected int ram;

    public Laptop(String name, double price, int ram) {
        super(name, price);
        this.ram = ram;
    }

    public int getRam() {
        return ram;
    }

    @Override
    public String toString() {
        return super.toString() + ", | RAM : " + getRam();
    }
}
