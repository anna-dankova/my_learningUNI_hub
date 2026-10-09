package TechShopPet;

import java.util.HashMap;

public class StoreInventory {
    private HashMap<String, Product> productsByName = new HashMap<>();

    public void addProduct(Product product) {
        productsByName.put(product.getName(), product);
    }

    public Product getProduct(String name) {
        return productsByName.get(name);

    }

    public boolean hasProduct(String name) {
        return productsByName.containsKey(name);
        
    }

    public boolean removeProduct(String name) {
        if (productsByName.containsKey(name)) {
            productsByName.remove(name);
            return true;
        }
        return false;
    }

    public void printInventoryStatics() {

        int phoneCount = 0;
        int laptopCount = 0;
        int headphonesCount = 0;


        for (Product p : productsByName.values()) {
            if (p instanceof Phone) {
                phoneCount++;
            } else if (p instanceof Laptop) {
                laptopCount++;
            } else if (p instanceof Headphones) {
                headphonesCount++;
            }
        }
        System.out.println("--- Inventory Statistics ---");
        System.out.println("Phones: " + phoneCount);
        System.out.println("Laptops: " + laptopCount);
        System.out.println("Headphones: " + headphonesCount);
    }

    public int getProductCount() {
        return productsByName.size();
    }

    public void printAllProducts() {
        for (Product p : productsByName.values()) {
            System.out.println(p.toString());
        }

    }
}
