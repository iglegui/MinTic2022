import java.util.ArrayList;
import java.util.Scanner;

public class Colegio {
    public static ArrayList<Persona> personList = new ArrayList<Persona>();

    public static void main(String[] args) {
        Scanner input=new Scanner(System.in);
        while(true){
            String cadenaIngresada=input.next();
            char opcion=cadenaIngresada.charAt(0);
            switch (opcion){

                case '1':
                    agregarPersonas(cadenaIngresada);
                    break;
                case '2':
                    mostrarPersonas();
                    break;

                case '3':
                    input.close ();
                    System.exit(0);

            }
        }
    }

    public static void agregarPersonas(String entrada) {
        String datos[]=entrada.split("&");
        String nombre=datos[2];
        int documento =Integer.parseInt(datos[3]);
        char genero=datos[4].charAt(0);
        int telefono=Integer.parseInt(datos[5]);

        if (datos[1].equals("Alumno")){
            String grado=datos[6];
            int edad =Integer.parseInt(datos[7]);

            Alumno estudiante=new Alumno(nombre, documento, genero, telefono, grado, edad);

            personList.add(estudiante);
        }
        else if (datos[1].equals("Profesor")){
            String asignatura=datos[6];
            int salario=Integer.parseInt(datos[7]);
            Profesor docente=new Profesor(nombre, documento, genero, telefono,
                    asignatura, salario);
            personList.add(docente);
        }
    }

    private static void mostrarPersonas() {
        System.out.println("**Personas Colegio**\n" );
        for(Persona persona:personList){
            persona.mostrarDatos();
            System.out.println();
        }
        System.out.println();
    }
}
