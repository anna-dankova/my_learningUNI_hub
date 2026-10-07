package Lessons1;

import java.util.ArrayList;
import java.util.Scanner;

public class Students {

    static class Student {
        String name;
        int age;
        double gpa;

        Student(String name, int age, double gpa) {
            this.name = name;
            this.age = age;
            this.gpa = gpa;
        }
    }

    public static String getStatus(double gpa) {
        if (gpa >= 4.2)
            return "A";
        else if (gpa >= 3.2)
            return "B";
        else if (gpa >= 2.2)
            return "C";
        else
            return "D";
    }

    public static Student createStudent() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter name: ");
        String inName = scanner.nextLine();

        System.out.print("Enter age: ");
        int inAge = scanner.nextInt();

        System.out.print("Enter GPA: ");
        double inGpa = scanner.nextDouble();

        return new Student(inName, inAge, inGpa);
    }

    public static void main(String[] args) {
        ArrayList<Student> students = new ArrayList<>();

        students.add(new Student("Kim", 22, 3.7));
        students.add(new Student("Yao", 17, 2.0));
        students.add(new Student("Kira", 20, 4.5));
        students.add(new Student("Shoto", 18, 3.0));
        students.add(new Student("Vita", 19, 3.6));

        System.out.println("--- Add new student ---");
        Student newStudent = createStudent();
        students.add(newStudent);

        System.out.println("\n--- Student List ---");
        for (Student s : students) {
            System.out.println("Name: " + s.name
                    + " | Age: " + s.age
                    + " | GPA: " + s.gpa
                    + " | Status: " + getStatus(s.gpa));

        }
    }
}