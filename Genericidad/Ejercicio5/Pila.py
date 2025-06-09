from typing import Generic, TypeVar, List, Optional
    
T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    # a) Método para apilar (push)
    def apilar(self, elemento: T) -> None:
        """Agrega un elemento al tope de la pila."""
        self.elementos.append(elemento)

    # b) Método para desapilar (pop)
    def desapilar(self) -> Optional[T]:
        """Elimina y retorna el último elemento de la pila. Retorna None si la pila está vacía."""
        if self.esta_vacia():
            print("La pila está vacía. No se puede desapilar.")
            return None
        return self.elementos.pop()

    def esta_vacia(self) -> bool:
        return len(self.elementos) == 0

    # d) Método para mostrar los datos de la pila
    def mostrar(self) -> None:
        """Muestra los elementos de la pila desde la base hasta la cima."""
        print("Contenido de la pila (base -> cima):", self.elementos)

# c) Pruebas de la pila con diferentes tipos de datos

pila_enteros = Pila[int]()
pila_enteros.apilar(10)
pila_enteros.apilar(20)
pila_enteros.apilar(30)
pila_enteros.mostrar()
print("Desapilado:", pila_enteros.desapilar())
pila_enteros.mostrar()
print()

pila_cadenas = Pila[str]()
pila_cadenas.apilar("Hola")
pila_cadenas.apilar("Mundo")
pila_cadenas.mostrar()
print("Desapilado:", pila_cadenas.desapilar())
pila_cadenas.mostrar()
print()

pila_booleanos = Pila[bool]()
pila_booleanos.apilar(True)
pila_booleanos.apilar(False)
pila_booleanos.mostrar()
print("Desapilado:", pila_booleanos.desapilar())
pila_booleanos.mostrar()
