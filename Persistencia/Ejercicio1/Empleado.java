package Persistencia.Ejercicio1;

import java.io.Serializable;

public class Empleado implements Serializable {
    public String nombre;
    public int edad;
    public double salario;

    public Empleado(String nombre, int edad, double salario) {
        this.nombre = nombre;
        this.edad = edad;
        this.salario = salario;
    }

    public String getNombre() {
        return nombre;
    }

    public int getEdad() {
        return edad;
    }

    public double getSalario() {
        return salario;
    }

    @Override
    public String toString() {
        return String.format("Nombre: %s, Edad: %d, Salario: %.2f", nombre, edad, salario);
    }
}

