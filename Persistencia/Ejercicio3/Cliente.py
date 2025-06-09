import json
import os

class Cliente:
    def __init__(self, id: int, nombre: str, telefono: int):
        self.id = id
        self.nombre = nombre
        self.telefono = telefono

    def to_dict(self):
        return {'id': self.id, 'nombre': self.nombre, 'telefono': self.telefono}

    @staticmethod
    def from_dict(data):
        return Cliente(data['id'], data['nombre'], data['telefono'])

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Teléfono: {self.telefono}"


class ArchivoCliente:
    def __init__(self, nomA: str):
        self.nomA = nomA
        self.crearArchivo()

    def crearArchivo(self):
        if not os.path.exists(self.nomA):
            with open(self.nomA, 'w') as f:
                json.dump([], f)

    def _leerClientes(self):
        with open(self.nomA, 'r') as f:
            return json.load(f)

    def _escribirClientes(self, clientes):
        with open(self.nomA, 'w') as f:
            json.dump(clientes, f, indent=4)


    def guardaCliente(self, c: Cliente):
        clientes = self._leerClientes()
        clientes.append(c.to_dict())
        self._escribirClientes(clientes)

    # b) Implementa buscarCliente(int c) a través del id
    def buscarCliente(self, c: int) -> Cliente:
        clientes = self._leerClientes()
        for cli in clientes:
            if cli['id'] == c:
                return Cliente.from_dict(cli)
        return None

    # c) Implementa buscarCelularCliente(int c), que devuelva los datos del cliente junto al número de celular
    def buscarCelularCliente(self, c: int) -> Cliente:
        return self.buscarCliente(c)  # misma lógica, pero el __str__ muestra ambos datos

if __name__ == "__main__":
    archivo = ArchivoCliente("clientes.json")

    archivo.guardaCliente(Cliente(1, "Carlos", 71234567))
    archivo.guardaCliente(Cliente(2, "Maria", 76543210))

    cliente = archivo.buscarCliente(2)
    if cliente:
        print("Cliente encontrado:", cliente)
    else:
        print("Cliente no encontrado.")

    cliente = archivo.buscarCelularCliente(1)
    if cliente:
        print("Celular del cliente:", cliente.telefono)
    else:
        print("Cliente no encontrado.")

