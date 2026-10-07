package Lessons2.Hotel;

public class Main {
    public static void main(String[] args) {
        Hotel hotel = new Hotel();
        hotel.addRoom(new Room(101, 50, true));
        hotel.addRoom(new Room(102, 60, false));
        hotel.addRoom(new Room(103, 60, false));
        hotel.addRoom(new Room(104, 55, true));
        hotel.addRoom(new Room(105, 70, true));
        hotel.addRoom(new Room(106, 45, false));

        hotel.addLuxusRoom(new LuxusRoom(201, 120, false, true));
        hotel.addLuxusRoom(new LuxusRoom(202, 150, true, true));
        hotel.addLuxusRoom(new LuxusRoom(203, 170, true, true));
        hotel.addLuxusRoom(new LuxusRoom(204, 130, true, false));
        hotel.addLuxusRoom(new LuxusRoom(205, 200, true, true));
        hotel.addLuxusRoom(new LuxusRoom(206, 160, false, true));

        // Создаем гостей (Visitor)
        hotel.addVisitor(new Visitor("Luka", 3, 102));
        hotel.addVisitor(new Visitor("Ana", 5, 201));
        hotel.addVisitor(new Visitor("Jan", 2, 206));
        hotel.addVisitor(new Visitor("Maja", 7, 103));
        hotel.addVisitor(new Visitor("Denis", 4, 106));

        System.out.println("======= СТАТУС ОТЕЛЯ: НАЧАЛО ДНЯ =======");
        System.out.println("Выводим все свободные комнаты:");
        hotel.getFreeRooms();
        System.out.println("----------------------------------------");

        System.out.println("\n======= ПРОЦЕСС ЗАСЕЛЕНИЯГОСТЕЙ =======");

        System.out.println("\n======= СТАТУС ОТЕЛЯ: ПОСЛЕ ЗАСЕЛЕНИЯ =======");
        System.out.println("Оставшиеся свободные люкс-номера:");
        hotel.getFreeLuxRooms();
        System.out.println("----------------------------------------");

        System.out.println("\n======= ФИНАНСОВЫЙ ОТЧЕТ =======");
        // Вызываем твой итоговый подсчет цены
        hotel.countPriceAll();
        System.out.println("========================================");
    }
}