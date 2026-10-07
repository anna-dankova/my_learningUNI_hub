package Lessons2.Hotel;

public class Visitor {
    String name;
    int countOfDays;
    int room = 0;

    public Visitor(String name, int countOfDays, int room) {
        this.name = name;
        this.countOfDays = countOfDays;
        this.room = room;
    }

    public String getName() {
        return this.name;
    }

    public int getRoom() {
        return this.room;
    }

    public void VisitorRoom(Visitor v) {
        if (v.getRoom() == 0) {
            System.out.println("Visitor has no room");
        } else {
            System.out.println("Room : " + v.getRoom());
        }
    }

}
