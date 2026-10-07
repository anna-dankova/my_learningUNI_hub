package Vaje;


public class Vaja5 {
     public static void main(String[] args) {
         boolean isWorkEngine = true;
         boolean isWorkTransmission = true;
         boolean[] wheels = {true, true, true, true};
         int workingWheels = 0;
         for (boolean wheel : wheels) {
             if (wheel) {
                 workingWheels++;
             }
         }
         if (isWorkEngine && isWorkTransmission && workingWheels >= 3) {
             System.out.println(" у машины работают 3 колеса, коробка передач и двигатель");
         }
     }
 }