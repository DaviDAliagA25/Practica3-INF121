package Ejercicio5;

public class Main {
    public static void main(String[] args) {
        Pila<Integer> pilaEnteros = new Pila<>();
        pilaEnteros.apilar(10);
        pilaEnteros.apilar(20);
        pilaEnteros.apilar(30);
        pilaEnteros.mostrar();
        System.out.println("Desapilado: " + pilaEnteros.desapilar());
        pilaEnteros.mostrar();
        System.out.println();

        Pila<String> pilaCadenas = new Pila<>();
        pilaCadenas.apilar("Hola");
        pilaCadenas.apilar("Mundo");
        pilaCadenas.mostrar();
        System.out.println("Desapilado: " + pilaCadenas.desapilar());
        pilaCadenas.mostrar();
        System.out.println();

        Pila<Boolean> pilaBooleanos = new Pila<>();
        pilaBooleanos.apilar(true);
        pilaBooleanos.apilar(false);
        pilaBooleanos.mostrar();
        System.out.println("Desapilado: " + pilaBooleanos.desapilar());
        pilaBooleanos.mostrar();
    }
}


