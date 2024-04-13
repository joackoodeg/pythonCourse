from typing import List
from datetime import datetime
from decimal import Decimal

class Carrera:
    def __init__(self, alumnos: List['Alumno']):
        self.c_alumnos = alumnos

    def contar_egresados(self)-> int:
        if self.c_alumnos:
            return sum(1 for alumno in self.c_alumnos if alumno.fecha_egreso is not None)
        else:
            return 0
        
    def calcular_promedios(self) -> dict:
        promedios = {}
        for alumno in self.c_alumnos:
            if alumno.fecha_egreso is not None:
                notas_aprobadas=[examen.nota for examen in alumno.examenes if examen.nota>=6]
                if notas_aprobadas:
                    promedio=sum(notas_aprobadas)/len(notas_aprobadas)
                    promedios[alumno.nombre]= Decimal(promedio).quantize(Decimal('0.00'))
        return promedios

class Examen:
    def __init__(self, nota: float):
        self.nota = nota

class Alumno:
    def __init__(self, nombre: str, fecha_egreso: datetime, examenes: List['Examen']):
        self.nombre = nombre
        self.fecha_egreso = fecha_egreso
        self.examenes = examenes
# Ejemplo de uso

if __name__ == "__main__":
    # Crear algunos exámenes
    examenes_alumno1 = [Examen(7), Examen(8), Examen(5)]
    examenes_alumno2 = [Examen(6), Examen(7), Examen(6)]

    # Crear alumnos con fechas de egreso y exámenes
    alumno1 = Alumno("Juan", datetime(2023, 6, 30), examenes_alumno1)
    alumno2 = Alumno("María", datetime(2023, 6, 30), examenes_alumno2)

    # Agregar los alumnos a una lista
    alumnos = [alumno1, alumno2]

    # Crear una carrera con los alumnos
    carrera = Carrera(alumnos)

    # Mostrar la cantidad de egresados y sus promedios
    print("Cantidad de egresados:", carrera.contar_egresados())
    promedios = carrera.calcular_promedios()
    for alumno, promedio in promedios.items():
        print(f"Egresado {alumno} - Promedio: {promedio}")