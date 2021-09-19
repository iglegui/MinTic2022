import java.util.Scanner;

public class Main {
    public static void catapulta(int tiro_uno){
        int tiro_dos = (tiro_uno * 2) + 4;
        int tiro_tres = (tiro_uno + tiro_dos) / 5;
        System.out.println(tiro_uno + " " + tiro_dos + " " + tiro_tres);

        if (tiro_tres >= 0 && tiro_tres <= 20 ) {
            System.out.println("Uno");
        } else if (21 <= tiro_tres && tiro_tres <= 30) {
            System.out.println("Dos");
        } else if (31 <= tiro_tres && tiro_tres <= 50) {
            System.out.println("Tres");
        } else {
            System.out.println("Cuatro");
        }


    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Ingrese distancia en metros: ");
        int distancia = Integer.parseInt(sc.nextLine());
        catapulta(distancia);
    }
}
