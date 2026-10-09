package TechShopPET;

public class Phone extends Product {
    protected int cameraCount;

    public Phone(String name, double price, int cameraCount) {
        super(name, price);
        this.cameraCount = cameraCount;
    }

    public int getCameraCount() {
        return cameraCount;
    }

    @Override
    public String toString() {
        return super.toString() + ", | Count of cameras : " + getCameraCount();
    }
}
