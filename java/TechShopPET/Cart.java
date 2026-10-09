package TechShopPet;
import java.util.List;
import java.util.ArrayList;

public class Cart {
    private final List<Product> items = new ArrayList<>();

    public void addProduct(Product p) {
        if (p == null) {
            throw new IllegalArgumentException("Product cannot be null");
        }
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
            throw new IllegalStateException("Cart is empty");
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
            if (p instanceof Headphones h) {
                if (h.isWireless()) {
                    wirelessHeadphones.add(h);
                }
            }
        }
            return wirelessHeadphones.toString();
    }
    


     public List<Product> getProducts(){
        return new ArrayList<>(this.items);
     }
    //  public void printProducts() {
    //     StringBuilder sb = new StringBuilder("Products in the list:\n");
    //     for (Product p : items) {
    //         sb.append(p).append("\n");
    // }
    //     System.out.println(sb.toString());
    // }
}



