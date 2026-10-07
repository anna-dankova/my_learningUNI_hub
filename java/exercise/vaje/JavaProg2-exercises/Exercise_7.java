package JavaProg2;

public class Exercise_7 {
    public static void main(String[] args) {
        int num1 = Integer.parseInt(args[0]);
        String operation = args[1];
        int num2 = Integer.parseInt(args[2]);

        int result = 0;
        
        switch (operation) {
            case "+":
                result = num1 + num2;
                break;
            case "-":
                result = num1 - num2;
                break;
            case "/":
                if (num2!=0) {
                result = num1 / num2;}
                else { System.out.println("Ошибка: деление на ноль!");}
                break;
            case "*":
                result = num1 * num2;
                break;
            default:
                System.out.println("Неизвестная операция: " + operation);
                break;
        }
        System.out.println("Результат: " + num1 + " " + operation + " " + num2 + " = " + result );
    }
}
