package Persistencia.Ejercicio1;

public class Main {
    public static void main(String[] args) {
        ArchivoEmpleado archivo = new ArchivoEmpleado("empleados.dat");

        // a) Guardar empleados
        archivo.guardarEmpleado(new Empleado("Juan", 30, 3500.0));
        archivo.guardarEmpleado(new Empleado("Ana", 25, 4200.0));
        archivo.guardarEmpleado(new Empleado("Luis", 40, 2800.0));

        // b) Buscar por nombre
        Empleado emp = archivo.buscaEmpleado("Ana");
        if (emp != null) {
            System.out.println("Empleado encontrado: " + emp);
        } else {
            System.out.println("Empleado no encontrado.");
        }

        // c) Buscar por salario mayor a 3000.0
        emp = archivo.mayorSalario(3000.0);
        if (emp != null) {
            System.out.println("Empleado con salario mayor: " + emp);
        } else {
            System.out.println("No hay empleado con salario mayor al ingresado.");
        }
    }
}

