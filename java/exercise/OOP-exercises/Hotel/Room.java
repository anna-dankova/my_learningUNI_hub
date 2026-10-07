package Lessons2.Hotel;

public class Room {
    int number;
    int priceForNight;
    boolean free;

    public Room(int number, int priceForNight, boolean free) {
        this.number = number;
        this.priceForNight = priceForNight;
        this.free = free;
    }

    public void roomBooked() {
        this.free = false;
    }

    public boolean isBooked() {
        return this.free;
    }

    public int RoomNumber() {
        return this.number;
    }

}
