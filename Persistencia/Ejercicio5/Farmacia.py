import json

class Medicamento:
    def __init__(self, nombre='', codMedicamento=0, tipo='', precio=0.0):
        self.nombre = nombre
        self.codMedicamento = codMedicamento
        self.tipo = tipo
        self.precio = precio

    def mostrar(self):
        print(f"Nombre: {self.nombre}, Codigo: {self.codMedicamento}, Tipo: {self.tipo}, Precio: {self.precio}")

    def getTipo(self):
        return self.tipo

    def getPrecio(self):
        return self.precio

    def to_dict(self):
        return self.__dict__

    @staticmethod
    def from_dict(data):
        return Medicamento(**data)


class Farmacia:
    def __init__(self, nombreFarmacia='', sucursal=0, direccion=''):
        self.nombreFarmacia = nombreFarmacia
        self.sucursal = sucursal
        self.direccion = direccion
        self.medicamentos = []

    def mostrar(self):
        print(f"Farmacia: {self.nombreFarmacia}, Sucursal: {self.sucursal}, Direccion: {self.direccion}")
        for med in self.medicamentos:
            med.mostrar()

    def getDireccion(self):
        return self.direccion

    def getSucursal(self):
        return self.sucursal

    def mostrarMedicamentos(self, tipo):
        for med in self.medicamentos:
            if med.getTipo().lower() == tipo.lower():
                med.mostrar()

    def buscaMedicamento(self, nombre):
        for med in self.medicamentos:
            if med.nombre.lower() == nombre.lower():
                return True
        return False

    def to_dict(self):
        return {
            'nombreFarmacia': self.nombreFarmacia,
            'sucursal': self.sucursal,
            'direccion': self.direccion,
            'medicamentos': [med.to_dict() for med in self.medicamentos]
        }

    @staticmethod
    def from_dict(data):
        f = Farmacia(data['nombreFarmacia'], data['sucursal'], data['direccion'])
        f.medicamentos = [Medicamento.from_dict(m) for m in data['medicamentos']]
        return f


class ArchFarmacia:
    def __init__(self, filename):
        self.filename = filename
        self.farmacias = []

    def guardar(self):
        with open(self.filename, 'w') as f:
            json.dump([farmacia.to_dict() for farmacia in self.farmacias], f, indent=4)

    def cargar(self):
        with open(self.filename, 'r') as f:
            self.farmacias = [Farmacia.from_dict(d) for d in json.load(f)]

    def listar(self):
        for f in self.farmacias:
            f.mostrar()

    def mostrarMedicamentosTos(self, sucursal):
        for f in self.farmacias:
            if f.getSucursal() == sucursal:
                print(f"\nMedicamentos para la tos en sucursal {sucursal}:")
                f.mostrarMedicamentos("tos")

    def sucursalConMedicamento(self, nombreMedicamento):
        for f in self.farmacias:
            if f.buscaMedicamento(nombreMedicamento):
                print(f"\nSucursal que tiene '{nombreMedicamento}':")
                print(f"Sucursal: {f.getSucursal()}, Direccion: {f.getDireccion()}")
                return
        print(f"\nNo se encontró el medicamento '{nombreMedicamento}'.")


archivo = ArchFarmacia("farmacias.json")

f1 = Farmacia("Farmacia Central", 1, "Calle A #123")
f1.medicamentos = [
    Medicamento("Golpex", 101, "tos", 12.5),
    Medicamento("Paracetamol", 102, "resfrio", 5.0)
]

f2 = Farmacia("Farmacia Norte", 2, "Av. B #456")
f2.medicamentos = [
    Medicamento("Broncolin", 201, "tos", 8.0),
    Medicamento("Ibuprofeno", 202, "resfrio", 6.0)
]

archivo.farmacias = [f1, f2]
archivo.guardar()

print("\nArchivo de farmacias cargado:")
archivo.cargar()
archivo.listar()

print("\nMedicamentos para la tos en la sucursal 2:")
archivo.mostrarMedicamentosTos(2)

print("\nBuscar el medicamento 'Golpex':")
archivo.sucursalConMedicamento("Golpex")


