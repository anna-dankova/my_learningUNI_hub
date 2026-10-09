package TechShopPET;

public class Product {
    private String name;
    private double price;

    public Product(String name, double price) {
        this.name = name;
        this.price = price;
    }

    public String getName() {
        return this.name;
    }

    public double getPrice() {
        return this.price;
    }

    public void applyDiscount(double percentage) {
        double discountAmount = price * percentage / 100;
        price -= discountAmount;
    }

    @Override
    public String toString() {
        return "Product : " + getName() + ", | Price : " + getPrice();
    }
}