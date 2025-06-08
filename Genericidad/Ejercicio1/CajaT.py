from typing import Generic, TypeVar

T = TypeVar('T')

class Caja(Generic[T]):
    def __init__(self):
        self._contenido: T = None

    # a) Agrega métodos guardar() y obtener()
    def guardar(self, item: T):
        self._contenido = item

    def obtener(self) -> T:
        return self._contenido

# b) Crea dos instancias de la caja y almacena 2 datos de diferente tipo

caja_entero = Caja[int]()
caja_entero.guardar(42)

caja_texto = Caja[str]()
caja_texto.guardar("Hola Mundo")

# c) Muestra el contenido de las cajas
print("Contenido de caja_entero:", caja_entero.obtener())  
print("Contenido de caja_texto:", caja_texto.obtener())    

