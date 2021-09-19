public class Alumno extends Persona {
    public String grade;
    public int age;

    public Alumno (String name, int id, char gender, int phone,
                   String grade, int age) {
        super(name, id, gender, phone);
        this.grade=grade;
        this.age=age;
    }
    public void mostrarDatos(){
        System.out.println("Persona Alumno-");
        super.mostrarDatos();
        System.out.println("\tgrado: " +grade);
        System.out.println("\tedad: " +age);
    }
}
