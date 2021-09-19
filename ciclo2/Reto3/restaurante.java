import java.util.ArrayList;
import java.util.List;
import java.util.Collections;


public class restaurante {

    public static ArrayList tipos_productos(ArrayList productos){
        ArrayList salida = new ArrayList();
        for (int n = 0; n < productos.size(); n++) {
            
            if(Collections.frequency(salida, productos.get(n))<1) {
                salida.add(productos.get(n));
            }
        }
        return salida;
    }

    public static ArrayList productosfaltantes(ArrayList<Integer> p,ArrayList<String> Lc, String productos) {
        
        ArrayList productosBuscar = new ArrayList();
        for(Integer item:p) {
            if (Lc.get(item).equals(productos)) {
                productosBuscar.add(item);
            }
        }
        return productosBuscar;
    }

    public static ArrayList novendo(ArrayList<String>productosCompetencia,ArrayList<String> products) {
        ArrayList lista = new ArrayList();
        for (String item:productosCompetencia) {
            if(products.contains(item) == false) {
                lista.add(item);
            }
        }
        return lista;
    }

    public static Integer cambio (ArrayList productosCompetencia,ArrayList products) {
        int olimpicon = 0;
        int tomePa = 0;
        for(int n = 0; n < productosCompetencia.size(); n++) {
            if(products.contains(productosCompetencia.get(n)) == false) {
                 olimpicon++;
            }
        }
        for(int m = 0; m < products.size(); m++) {
            if (productosCompetencia.contains(products.get(m)) == false) {
                tomePa++;
            }
        }
        return Math.min(tomePa, olimpicon);
    }
    
    public static void main(String[] args) {
        
        restaurante obj = new restaurante();
    }
}
