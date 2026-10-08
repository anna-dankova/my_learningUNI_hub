package Lessons2.TechShop;

import java.util.ArrayList;

public class Cart {
    private ArrayList<Product> items = new ArrayList<>();

    public void addProduct(Product p) {
        items.add(p);
    }

    public double calculateTotal() {
         double total = 0;
        for (Product p : items) {
            total += p.getPrice();
        }
        return total;
    }

    public String findMostExpensiveProduct() {
        double maxPrice = 0;
        String expensiveName = "";
        if (items.isEmpty()) {
            return null;
        }
        for (Product p : items) {
            if (p.getPrice() > maxPrice) {
                maxPrice = p.getPrice();
                expensiveName = p.getName();
            }
        }
        
        return maxPrice + ", " + expensiveName;
    }

    public String getWirelessHeadphonesOnly() {
        List<Headphones> wirelessHeadphones = new ArrayList<>();

        for (Product p : items) {
            if (p instanceof Headphones) {
                Headphones h = (Headphones) p;
                if (h.isWireless()) {
                    wirelessHeadphones.add(h);
                }
            }else {
                return null;
            }
            return wirelessHeadphones.toString();
    }
    }
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder("Products in the list:\n");
        for (Product p : items) {
            sb.append(p.toString()).append("\n");
        }
        return sb.toString();
    }
}
