package Lessons2.TechShop;

public class Main {
    public static void main(String[] args) {
        StoreInventory inventory = new StoreInventory();
        inventory.addProduct(new Phone("iPhone 15", 1000.0, 2));
        inventory.addProduct(new Laptop("Lenovo IdeaPad", 1200.0, 16));
        inventory.addProduct(new Headphones("Sony WH-1000", 300.0, true));

        inventory.addProduct(new Phone("Samsung Galaxy S24", 900.0, 2));
        inventory.addProduct(new Phone("Google Pixel 8", 700.0, 2));
        inventory.addProduct(new Phone("Xiaomi 14 Pro", 600.0, 1));
        inventory.addProduct(new Phone("OnePlus 12", 800.0, 2));
        inventory.addProduct(new Phone("iPhone 15 Pro", 1200.0, 3));
        inventory.addProduct(new Phone("Asus ROG Phone 8", 1100.0, 2));
        inventory.addProduct(new Phone("Huawei Pura 70", 850.0, 2));
        inventory.addProduct(new Phone("Nothing Phone 2", 550.0, 1));
        inventory.addProduct(new Phone("Sony Xperia 1 VI", 1300.0, 2));

        inventory.addProduct(new Laptop("MacBook Air M3", 1400.0, 16));
        inventory.addProduct(new Laptop("ASUS Zenbook 14", 1100.0, 16));
        inventory.addProduct(new Laptop("HP Spectre x360", 1500.0, 32));
        inventory.addProduct(new Laptop("Dell XPS 13", 1600.0, 16));
        inventory.addProduct(new Laptop("Acer Swift Go", 800.0, 8));
        inventory.addProduct(new Laptop("Lenovo Legion 5", 1300.0, 32));
        inventory.addProduct(new Laptop("MSI Katana 15", 1000.0, 16));
        inventory.addProduct(new Laptop("Huawei MateBook X", 1700.0, 16));
        inventory.addProduct(new Laptop("Gigabyte Aero 16", 2000.0, 32));

        inventory.addProduct(new Headphones("Apple AirPods Max", 550.0, true));
        inventory.addProduct(new Headphones("Bose QuietComfort Ultra", 400.0, true));
        inventory.addProduct(new Headphones("Sennheiser Momentum 4", 350.0, true));
        inventory.addProduct(new Headphones("JBL Tune 720BT", 80.0, false));
        inventory.addProduct(new Headphones("Marshall Monitor II", 300.0, true));
        inventory.addProduct(new Headphones("Anker Soundcore Q45", 150.0, true));
        inventory.addProduct(new Headphones("Sony WF-1000XM5", 250.0, true));
        inventory.addProduct(new Headphones("Beats Studio Pro", 350.0, true));
        inventory.addProduct(new Headphones("Audio-Technica M50xBT2", 200.0, false));

        Cart cart = new Cart();
        Product chosenLaptop = inventory.getProduct("Lenovo IdeaPad");
        cart.addProduct(chosenLaptop);

        Product chosenHeadphones = inventory.getProduct("JBL Tune 720BT");
        cart.addProduct(chosenHeadphones);
        chosenHeadphones = inventory.getProduct("Marshall Monitor II");
        cart.addProduct(chosenHeadphones);

        Product chosenPhone = inventory.getProduct("Asus ROG Phone 8");

        cart.addProduct(chosenPhone);
        System.out.println(cart);

        System.out.println("Total cart value: " + cart.calculateTotal());
        System.out.println(cart.findMostExpensiveProduct());
        cart.printWirelessHeadphonesOnly();
        //cart.printAllCart();
    }
}