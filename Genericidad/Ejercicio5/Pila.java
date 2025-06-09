package Ejercicio5;
import java.util.ArrayList;
import java.util.List;

public class Pila<T> {
    public List<T> elementos;

    public Pila() {
        elementos = new ArrayList<>();
    }

    // a) Método para apilar (push)
    public void apilar(T elemento) {
        elementos.add(elemento);
    }

    // b) Método para desapilar (pop)
    public T desapilar() {
        if (estaVacia()) {
            System.out.println("La pila está vacía. No se puede desapilar.");
            return null;
        }
        return elementos.remove(elementos.size() - 1);
    }

    public boolean estaVacia() {
        return elementos.isEmpty();
    }

    // d) Método para mostrar los datos de la pila
    public void mostrar() {
        System.out.println("Contenido de la pila (base -> cima): " + elementos);
    }
}