package Lessons1.products;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<Hrana> products = new ArrayList<>();
        try(BufferedReader br = new BufferedReader
            (new FileReader("C:/_/Dev/JavaExercise/exercise/vaje/Lessons1/products/podatki.txt"))) {

            String vrstica;

            while ((vrstica= br.readLine()) != null) {
                String[] tokens= vrstica.split(",");
                String kategorija = tokens[0].trim();
                String naziv = tokens[1].trim();
                double cena = Double.parseDouble(tokens[2].trim());

                switch (kategorija) {
                    case  "*A":
                        Hrana h = new Hrana(naziv, cena);
                        products.add(h);
                        break;
                    case "*B":
                        boolean kvas = tokens[3].trim().equalsIgnoreCase("da");
                        Kruh k = new Kruh(naziv, cena, kvas);
                        products.add(k);
                        break;
                    case "*C":
                        boolean brezLaktoze = tokens[4].trim().equalsIgnoreCase("da");
                        double odstotekMascob = Double.parseDouble(tokens[3].trim());
                        MlecIzdelki m= new MlecIzdelki(naziv, cena, odstotekMascob, brezLaktoze);
                        products.add(m);
                        break;
                    case "*D":
                        Sadje s = new Sadje(naziv, cena, tokens[3].trim());
                        products.add(s);
                        break;
                
                    default:
                        break;
                }
            }
            br.close();

            int st=0;
            double vsota = 0;
            for(Hrana h : products){
                System.out.println(h);
                if(h instanceof MlecIzdelki){
                    vsota += h.getCena();
                    st++;
                }
            }
            if (st>0){
                double povprecje = vsota/ st;
                 System.out.println("Povprečna cena mlečnih izdelkov: " + povprecje + " EUR");
            } else { System.out.println("Ni mlecnih izdelkov");}
           
            
        } catch (Exception e) {
            System.out.println("Ошибка " + e.getMessage());
        }
            
        }
    }
// Мой первый правильный коммит через терминал!