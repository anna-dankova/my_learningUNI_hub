package Lessons2.TechShop;

public class Headphones extends Product {
    protected boolean isWireless;

    public Headphones(String name, double price, boolean isWireless) {
        super(name, price);
        this.isWireless = isWireless;
    }

    public boolean isWireless() {
        return isWireless;
    }

    @Override
    public String toString() {
        return super.toString() + ", | Wireless : " + isWireless();
    }
}
