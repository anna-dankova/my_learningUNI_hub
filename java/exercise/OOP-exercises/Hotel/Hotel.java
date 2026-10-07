package Lessons2.Hotel;

import java.util.ArrayList;

public class Hotel {
    ArrayList<Room> rooms = new ArrayList<>();
    ArrayList<Visitor> visitors = new ArrayList<>();

    public void addVisitor(Visitor v) {
        visitors.add(v);
    }

    public void addRoom(Room r) {
        rooms.add(r);
    }

    public void addLuxusRoom(LuxusRoom lr) {
        rooms.add(lr);
    }

    public String addToRoom(Visitor v) {
        for (Room r : rooms) {
            if (r.isBooked() == true) {
                r.roomBooked();
                v.room = r.RoomNumber();
                visitors.add(v);
            }
        }
        return " Visitor " + v.getName() + " is living in room num. " + v.getRoom();
    }

    public void getFreeRooms() {
        for (Room r : rooms) {
            if (r.isBooked() == true) {
                System.out.println("Free room : " + r.RoomNumber() + " Price: " + r.priceForNight);
            }
        }
    }

    public void getFreeLuxRooms() {
        for (Room r : rooms) {
            if (r instanceof LuxusRoom) {
                LuxusRoom lr = (LuxusRoom) r;
                System.out.println("Free Luxroom : " + lr.RoomNumber() + " Price: " + lr.priceForNight + ", jacuzzi : "
                        + lr.hasJacuzzi());
            }
        }
    }

    public void countPriceAll() {
        int totalCost = 0;

        for (Visitor v : visitors) {
            if (v.getRoom() == 0) {
                continue;
            }
            int visitorRoom = v.getRoom();

            int nightPrice = 0;
            int priceForVisiter = 0;
            int nights = 0;

            for (Room r : rooms) {
                if (r.RoomNumber() == visitorRoom) {

                    nightPrice = r.priceForNight;
                    nights = v.countOfDays;
                    priceForVisiter = nightPrice * nights;
                    break;
                }
            }
            totalCost += priceForVisiter;
        }
        System.out.println("Total expected income for hotel: " + totalCost);
    }

}
