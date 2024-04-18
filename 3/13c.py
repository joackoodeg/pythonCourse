"""
class Producto:
    def __init__(self, nombre: str, categoria: str):
        self.nombre = nombre
        self.categoria = categoria
class Carrito:
    def __init__(self, productos: list):
        self.productos = productos
    def calcular_descuento(productos: list):
        for producto in productos:
            if producto.categoria == 'alimentos':
                print(f"Descuento del 10% en {producto.nombre}")
            elif producto.categoria == 'limpieza':
                print(f"Descuento del 5% en {producto.nombre}")

# Añadir más condiciones para nuevos tipos de productos y descuentos
    productos = [
    Producto('manzanas', 'alimentos'),
    Producto('jabón', 'limpieza')
    ]
    carrito = Carrito(productos)
    carrito.calcular_descuento(carrito.productos)
"""


"""
RTA:
    Principio de Responsabilidad Única (SRP):
    La clase Carrito tiene la responsabilidad de mantener una lista de productos (productos) 
    y también la responsabilidad de calcular descuentos (calcular_descuento). 
    Esto viola el principio de que una clase debe tener una única razón para cambiar. 
    Separar estas responsabilidades en clases distintas mejorararía la cohesión del código y facilitaría su mantenimiento.

    SOLUCION: 
    Separar la lógica de descuentos en clases separadas por cada tipo de producto, 
    adheriéndose al Principio de Responsabilidad Única (SRP).

    Principio de Abierto/Cerrado (OCP):
    El método calcular_descuento tiene una implementación que no está cerrada a la modificación. 
    Cada vez que se añada un nuevo tipo de producto o se modifique un descuento existente, 
    es necesario modificar directamente el método calcular_descuento. 
    Esto viola el principio de que una clase debe estar abierta para su extensión pero cerrada para su modificación. 
    Una forma de resolver esto sería aplicar polimorfismo y crear clases separadas para cada tipo de producto, 
    evitando la necesidad de modificar el código existente cuando se agreguen nuevos tipos de productos o descuentos.

    SOLUCION:
    Utilizar el polimorfismo para calcular descuentos, 
    evitando la necesidad de modificar el código existente cuando se agreguen nuevos tipos de productos o descuentos, 
    adhiriéndose al Principio de Abierto/Cerrado (OCP).

"""
from typing import List

class Producto:
    def __init__(self, nombre: str, categoria: str):
        self.nombre = nombre
        self.categoria = categoria

class Alimentos(Producto):
    def __init__(self, nombre: str):
        super().__init__(nombre, 'alimentos')

    def calcular_descuento(self):
        return 0.1  # Descuento del 10% para alimentos

class Limpieza(Producto):
    def __init__(self, nombre: str):
        super().__init__(nombre, 'limpieza')

    def calcular_descuento(self):
        return 0.05  # Descuento del 5% para productos de limpieza

class Carrito:
    def __init__(self, productos: list['Producto']):
        self.productos = productos
    def calcular_descuento_total(self):
        descuento_total=0
        for producto in self.productos:
            descuento_total+=producto.calcular_descuento()
        return descuento_total


if __name__ == "__main__":     
    productos = [
        Alimentos('manzanas'),
        Limpieza('jabón')
    ]
    carrito = Carrito(productos)
    descuento_total = carrito.calcular_descuento_total()
    print(f"Descuento total: {descuento_total}")