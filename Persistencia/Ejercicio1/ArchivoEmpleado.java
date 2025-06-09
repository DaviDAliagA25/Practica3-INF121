package Persistencia.Ejercicio1;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class ArchivoEmpleado {
    public final String nomA;

    public ArchivoEmpleado(String nomA) {
        this.nomA = nomA;
        crearArchivo();
    }

    public void crearArchivo() {
        File archivo = new File(nomA);
        if (!archivo.exists()) {
            try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nomA))) {
                oos.writeObject(new ArrayList<Empleado>());
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }

    // a) Implementa el método guardarEmpleado(Empleado e) para almacenar empleados
    public void guardarEmpleado(Empleado e) {
        List<Empleado> lista = leerEmpleados();
        lista.add(e);
        try (ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(nomA))) {
            oos.writeObject(lista);
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }

    // b) Implementa buscaEmpleado(String n) a traves del nombre, para ver los datos del Empleado n
    public Empleado buscaEmpleado(String nombre) {
        List<Empleado> lista = leerEmpleados();
        for (Empleado e : lista) {
            if (e.getNombre().equals(nombre)) {
                return e;
            }
        }
        return null;
    }

    // c) Implementa mayorSalario(float sueldo), que devuelva al primer empleado con sueldo mayor al ingresado
    public Empleado mayorSalario(double sueldo) {
        List<Empleado> lista = leerEmpleados();
        for (Empleado e : lista) {
            if (e.getSalario() > sueldo) {
                return e;
            }
        }
        return null;
    }
    @SuppressWarnings("unchecked")
    private List<Empleado> leerEmpleados() {
        try (ObjectInputStream ois = new ObjectInputStream(new FileInputStream(nomA))) {
            return (List<Empleado>) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            e.printStackTrace();
            return new ArrayList<>();
        }
    }
}

