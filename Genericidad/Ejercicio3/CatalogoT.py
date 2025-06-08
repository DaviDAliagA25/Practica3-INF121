from typing import Generic, TypeVar, List

T = TypeVar('T')

class Catalogo(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    # a) Agrega métodos para agregar y buscar elemento
    def agregar(self, elemento: T):
        self.elementos.append(elemento)

    def buscar(self, elemento: T) -> bool:
        return elemento in self.elementos

    def mostrar(self):
        for elem in self.elementos:
            print(elem)

class Libro:
    def __init__(self, titulo: str, autor: str):
        self.titulo = titulo
        self.autor = autor

    def __eq__(self, other):
        return isinstance(other, Libro) and self.titulo == other.titulo and self.autor == other.autor

    def __str__(self):
        return f"Libro: {self.titulo} de {self.autor}"

class Producto:
    def __init__(self, nombre: str, precio: float):
        self.nombre = nombre
        self.precio = precio

    def __eq__(self, other):
        return isinstance(other, Producto) and self.nombre == other.nombre and self.precio == other.precio

    def __str__(self):
        return f"Producto: {self.nombre} - ${self.precio:.2f}"


# b) Prueba el catálogo con libros
catalogo_libros = Catalogo[Libro]()
catalogo_libros.agregar(Libro("Cien Años de Soledad", "Gabriel García Márquez"))
catalogo_libros.agregar(Libro("Don Quijote", "Miguel de Cervantes"))
catalogo_libros.mostrar()
print("¿Está 'Don Quijote'?:", catalogo_libros.buscar(Libro("Don Quijote", "Miguel de Cervantes")))

# c) Prueba el catálogo con productos
catalogo_productos = Catalogo[Producto]()
catalogo_productos.agregar(Producto("Laptop", 1200.0))
catalogo_productos.agregar(Producto("Mouse", 25.5))
catalogo_productos.mostrar()
print("¿Está el producto 'Mouse'?:", catalogo_productos.buscar(Producto("Mouse", 25.5)))
