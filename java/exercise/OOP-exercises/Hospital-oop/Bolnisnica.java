package JavaProg2.Hospital;

import java.util.ArrayList;

public class Bolnisnica {
    ArrayList<Oseba> seznam = new ArrayList<>();

    public void dodajOsebo(Oseba o){
        seznam.add(o);
    }
    public void izpisiVse(){
        for(Oseba o : seznam){
            System.out.println(o);}}

    public  Oseba vrniNajstarejsega(){
        if ( seznam.isEmpty()){
            return null;
        }

        Oseba najstarejsi = seznam.get(0);
        for(Oseba o : seznam){
            if (o.starost > najstarejsi.starost){
                najstarejsi= o;
            }
        }
        return najstarejsi; 

    
}
}