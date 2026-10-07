
// 1. Консольный калькулятор фигур
// Сделай программу, которая считает площадь и периметр для круга, прямоугольника и треугольника.
// Сейчас: Shape, Circle, Rectangle, Triangle, общий метод area() и perimeter().
// Потом: добавь ввод с клавиатуры и меню через switch.

package Lessons1;

import java.util.Scanner;

public class kalkulator {
    public static void main(String[] args) {
        while (true) {
            System.out.println("1. Circle " + "\n" + "2. Rectangle " + "\n" + "3.Triangle");
            Scanner myObj = new Scanner(System.in);
            int choise = myObj.nextInt();

            switch (choise) {
                case 1:
                    System.out.println("Введите радиус:");
                    double r = myObj.nextDouble();
                    Shape circle = new Circle(r);
                    System.out.println("Площадь круга: " + circle.area());
                    ;
                    System.out.println("Периметр круга:" + circle.perimeter());
                    break;

                case 2:
                    System.out.println("Введите высоту: ");
                    double h = myObj.nextDouble();
                    System.out.println("Введите длинну: ");
                    double w = myObj.nextDouble();
                    Shape rectangle = new Rectangle(w, h);
                    System.out.println("Площадь прямоугольника: " + rectangle.area());
                    ;
                    System.out.println("Периметр прямоугольника:" + rectangle.perimeter());
                    break;
                case 3:
                    System.out.println("Введите сторону а:");
                    double a = myObj.nextDouble();
                    System.out.println("Введите сторону b:");
                    double b = myObj.nextDouble();
                    System.out.println("Введите сторону c:");
                    double c = myObj.nextDouble();
                    Shape triangle = new Triangle(a, b, c);
                    System.out.println("Площадь треугольника: " + triangle.area());
                    ;
                    System.out.println("Периметр треугольника:" + triangle.perimeter());
                    break;
                default:
                    System.out.println("Введено не то число:");
                    break;
            }
        }
    }
}

abstract class Shape {
    public abstract double area();

    public abstract double perimeter();
}

class Circle extends Shape {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI * radius * radius;
    }

    @Override
    public double perimeter() {
        return 2 * Math.PI * radius;
    }
}

class Rectangle extends Shape {
    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.height = height;
        this.width = width;
    }

    @Override
    public double area() {
        return width * height;
    }

    @Override
    public double perimeter() {
        return 2 * (width + height);
    }
}

class Triangle extends Shape {
    private double a;
    private double b;
    private double c;

    public Triangle(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    @Override
    public double perimeter() {
        return a + b + c;
    }

    @Override
    public double area() {
        double p = perimeter() / 2;
        return Math.sqrt(p * (p - a) * (p - b) * (p - c));
    }
}
