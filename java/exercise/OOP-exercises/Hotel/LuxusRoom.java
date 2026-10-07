package Lessons2.Hotel;

public class LuxusRoom extends Room {
    boolean hasJacuzzi;

    public LuxusRoom(int number, int priceForNight, boolean free, boolean hasJacuzzi) {
        super(number, priceForNight, free);
        this.hasJacuzzi = hasJacuzzi;
    }

    public boolean hasJacuzzi() {
        return this.hasJacuzzi;
    }

}
