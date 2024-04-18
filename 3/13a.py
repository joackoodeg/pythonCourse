"""
class Empleado:
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora
    def generar_reporte_desempenio(self):
    # Código para generar el reporte de desempeño
        pass
        
    -Viola el principio de responsabilidad unica, ya que el reporte
    no deberia ser tarea del empeado (?)
"""
from typing import List

class Empleado:
    def __init__(self, nombre, horas_trabajadas, tarifa_por_hora):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_por_hora = tarifa_por_hora
    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_por_hora

class Trabajo:
    def __init__(self, empleados: list['Empleado']) -> None:
        self.empleados=empleados

    def generar_reporte_desempenio(self,empleados):
        pass