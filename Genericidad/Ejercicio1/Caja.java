package Ejercicio1;

public class Caja<T> {
    public T contenido;

    public void guardar(T item) {
        this.contenido = item;
    }

    public T obtener() {
        return this.contenido;
    }

    public static void main(String[] args) {
        // b) Crear dos instancias de Caja con diferentes tipos
        Caja<Integer> cajaEntero = new Caja<>();
        cajaEntero.guardar(42);

        Caja<String> cajaTexto = new Caja<>();
        cajaTexto.guardar("Hola Mundo");

        // c) Mostrar el contenido de las cajas
        System.out.println("Contenido de cajaEntero: " + cajaEntero.obtener());
        System.out.println("Contenido de cajaTexto: " + cajaTexto.obtener());
    }
}
