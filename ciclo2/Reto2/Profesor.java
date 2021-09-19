public class Profesor extends Persona {
    public String subject;
    public int salary;

    public Profesor (String name, int id, char gender, int phone,
                     String subject, int salary) {
        super(name, id, gender, phone);
        this.subject=subject;
        this.salary=salary;
    }

    public void mostrarDatos(){
        System.out.println("Persona Profesor-");
        super.mostrarDatos();
        System.out.println("\nasignatura: " +subject);
        System.out.println("\nsalario: " +salary);
    }

}
