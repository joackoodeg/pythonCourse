"""
class Dispositivo:
    def __init__(self, marca: str, modelo: str):
        self.marca = marca
        self.modelo = modelo

class Celular(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool):
        super().__init__(marca, modelo)
        self.pantalla = pantalla

class Tablet(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool, lapiz: bool):
        super().__init__(marca, modelo)
        self.pantalla = pantalla
        self.lapiz = lapiz
class Smartwatch(Dispositivo):
    def __init__(self, marca: str, modelo: str, pantalla: bool, gps: bool):
        super().__init__(marca, modelo)
        self.pantalla = pantalla
        self.gps = gps

def contar_piezas_reparacion(dispositivos: list):
    for dispositivo in dispositivos:
        if isinstance(dispositivo, Celular):
            print(contar_piezas_celular(dispositivo))
        elif isinstance(dispositivo, Tablet):
            print(contar_piezas_tablet(dispositivo))
        elif isinstance(dispositivo, Smartwatch):
            print(contar_piezas_smartwatch(dispositivo))
            
# Funciones para contar piezas de repuesto específicas para cada tipo de dispositivo
def contar_piezas_celular(celular: Celular):
    return "Piezas requeridas para reparar el celular"
def contar_piezas_tablet(tablet: Tablet):
    return "Piezas requeridas para reparar la tablet"
def contar_piezas_smartwatch(smartwatch: Smartwatch):
    return "Piezas requeridas para reparar el smartwatch"
# Ejemplo de uso
dispositivos = [
Celular("Samsung", "Galaxy S20", True),
Tablet("Apple", "iPad Pro", True, True),
Smartwatch("Apple", "Watch Series 6", True, True)
]
contar_piezas_reparacion(dispositivos)

"""

"""
ERRORES:
    Principio de Abierto/Cerrado (OCP): La violación de este principio se da en la función contar_piezas_reparacion y 
    las funciones auxiliares contar_piezas_celular, contar_piezas_tablet y contar_piezas_smartwatch. 
    Cada vez que se añade un nuevo tipo de dispositivo, se debe modificar estas funciones para agregar soporte para el nuevo tipo. 
    Esto significa que el código no está cerrado para la modificación, ya que cada vez que se añade un nuevo tipo de dispositivo, 
    es necesario modificar estas funciones existentes.

    Principio de Sustitución de Liskov (LSP): Este principio establece que los objetos de un programa deben ser sustituibles por 
    instancias de sus subtipos sin alterar la corrección del programa. En el código proporcionado, aunque Celular, Tablet y Smartwatch son subclases de Dispositivo, 
    el método contar_piezas_reparacion realiza una verificación explícita del tipo de dispositivo y llama a funciones específicas para cada tipo. 
    Esto indica que las subclases no son completamente sustituibles por la clase base, lo que viola el principio de Liskov.
"""

"""
SOLUCION:
podríamos reestructurar el código para que cumpla con el Principio de Abierto/Cerrado (OCP) y el Principio de Sustitución de Liskov (LSP), 
lo cual implica no depender de la identificación de tipos con isinstance y permitir que cada clase maneje sus propios cálculos de piezas de repuesto.

"""

from abc import ABC, abstractmethod
from typing import List

class Reparacion:
    def __init__(self, dispositivos: List['Dispositivo']):
        self.dispositivos=dispositivos

    def contar_piezas_reparacion_total(self):
        total=0
        for dispositivo in self.dispositivos:
            total+=dispositivo.contar_piezas_reparacion()
        return total

class Dispositivo:
    def __init__(self, marca: str, modelo: str, pantalla: bool):
        self.marca = marca
        self.modelo = modelo

    @abstractmethod
    def contar_piezas_reparacion(self):
        pass

class Celular(Dispositivo):
    def __init__(self, marca: str, modelo: str):
        super().__init__(marca, modelo, pantalla=True)
    
    def contar_piezas_reparacion(self) -> int:
        return 10


class Tablet(Dispositivo):
    def __init__(self, marca: str, modelo: str, lapiz: bool):
        super().__init__(marca, modelo, pantalla=True)
        self.lapiz = lapiz
    
    def contar_piezas_reparacion(self)-> int:
        return 25

class Smartwatch(Dispositivo):
    def __init__(self, marca: str, modelo: str, gps: bool):
        super().__init__(marca, modelo, pantalla=True)
        self.gps = gps
    
    def contar_piezas_reparacion(self) -> int: 
        return 5       

if __name__ == '__main__':
    # Ejemplo de uso
    dispositivos = [
    Celular("Samsung", "Galaxy S20"),
    Tablet("Apple", "iPad Pro", True),
    Smartwatch("Apple", "Watch Series 6", True)
    ]
    rep = Reparacion(dispositivos)
    print(rep.contar_piezas_reparacion_total())