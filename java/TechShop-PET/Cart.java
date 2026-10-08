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
            return "Cart is empty!";
        }
        for (Product p : items) {

            if (p.getPrice() > maxPrice) {
                maxPrice = p.getPrice();
                expensiveName = p.getName();
            }
        }
        
        return "Most expensive product: " + expensiveName + ", with price: " + maxPrice;
    }

    public void printWirelessHeadphonesOnly() {
        boolean found = false;

        for (Product p : items) {
            if (p instanceof Headphones) {
                Headphones h = (Headphones) p;

                if (h.isWireless()) {
              //      System.out.println("Wireless headphones: " + h.getName() + " " + h.getPrice() + "\n");
                    found = true;
                }
            }
        }
        if (!found) {
            //System.out.println("No wireless headphones in the cart.");
            return;
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
