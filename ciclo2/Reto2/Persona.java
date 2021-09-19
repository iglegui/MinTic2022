public class Persona {
    public String name;
    public int id;
    public char gender;
    public int phone;

    public Persona(String name, int id, char gender, int phone) {
        this.name=name;
        this.id=id;
        this.gender=gender;
        this.phone=phone;
    }
    public void mostrarDatos(){
        String []nombreSeparado=name.split("(?=\\p{Upper})");
        System.out.println("nombre: " + nombreSeparado[0]+" "+nombreSeparado[1]);
        System.out.println("\tdocumento: " +id);
        System.out.println("\tgenero: " +gender);
        System.out.println("\ttelefono: " +phone);
    }
}
