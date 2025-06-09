import json
import os

class Empleado:
    def __init__(self, nombre: str, edad: int, salario: float):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}'

    def to_dict(self):
        return {'nombre': self.nombre, 'edad': self.edad, 'salario': self.salario}

    @staticmethod
    def from_dict(data):
        return Empleado(data['nombre'], data['edad'], data['salario'])


class ArchivoEmpleado:
    def __init__(self, nomA: str):
        self.nomA = nomA
        self.crearArchivo()

    def crearArchivo(self):
        if not os.path.exists(self.nomA):
            with open(self.nomA, 'w') as f:
                json.dump([], f)  # Lista vacía

    # a) Implementa el método guardarEmpleado(Empleado e) para almacenar empleados
    def guardarEmpleado(self, e: Empleado):
        empleados = self._leerEmpleados()
        empleados.append(e.to_dict())
        with open(self.nomA, 'w') as f:
            json.dump(empleados, f, indent=4)

    # b) Implementa buscaEmpleado(String n) a traves del nombre, para ver los datos del Empleado n
    def buscaEmpleado(self, n: str) -> Empleado:
        empleados = self._leerEmpleados()
        for emp_data in empleados:
            if emp_data['nombre'] == n:
                return Empleado.from_dict(emp_data)
        return None

    # c) Implementa mayorSalario(float sueldo), que devuelva al primer empleado con sueldo mayor al ingresado
    def mayorSalario(self, sueldo: float) -> Empleado:
        empleados = self._leerEmpleados()
        for emp_data in empleados:
            if emp_data['salario'] > sueldo:
                return Empleado.from_dict(emp_data)
        return None

    def _leerEmpleados(self):
        with open(self.nomA, 'r') as f:
            return json.load(f)

if __name__ == "__main__":
    archivo = ArchivoEmpleado('empleados.json')

    # a) Guardar empleados
    archivo.guardarEmpleado(Empleado('Juan', 30, 3500.0))
    archivo.guardarEmpleado(Empleado('Ana', 25, 4200.0))
    archivo.guardarEmpleado(Empleado('Luis', 40, 2800.0))

    # b) Buscar empleado por nombre
    emp = archivo.buscaEmpleado('Ana')
    if emp:
        print("Empleado encontrado:", emp)
    else:
        print("Empleado no encontrado.")

    # c) Buscar salario mayor
    emp = archivo.mayorSalario(3000.0)
    if emp:
        print("Empleado con salario mayor:", emp)
    else:
        print("No hay empleado con salario mayor al ingresado.")

