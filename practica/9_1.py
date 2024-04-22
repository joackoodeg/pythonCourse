from typing import List
from datetime import datetime

class Carrera:
    def __init__(self):
        self.c_alumnos: List[Alumno] = []

    def contar_egresados(self) -> int:
        contador=0
        for alumno in self.c_alumnos:
            if alumno.fecha_egreso is not None:
                contador+=1
        return contador

    def calcular_promedios(self) -> dict:
        promedios={}
        for alumno in self.c_alumnos:
            if alumno.getFechaEgreso() is not None:
                prom=alumno.getPromedioExamAprobados()
                promedios[alumno.getNombre()] = prom
        return promedios    


class Examen:
    def __init__(self, nota: float):
        self.nota = nota

    def getNota(self):
        return self.nota
        

class Alumno:
    def __init__(self, nombre: str, examenes: List['Examen'], fecha_egreso: datetime = None):
        self.nombre = nombre
        self.fecha_egreso = fecha_egreso
        self.examenes = examenes

    def getNombre(self):
        return self.nombre

    def getFechaEgreso(self):
        return self.fecha_egreso

    def getExamenes(self):
        return self.examenes
    
    def getExamenesAprobados(self):
        resultado=[]
        for examen in self.examenes:
            if(examen.getNota()>=6):
                resultado.append(examen)
        return resultado
    
    def totalNotasAprobadas(self):
        examAprob=self.getExamenesAprobados()
        total=0
        for exam in examAprob:
            total+=exam.getNota()
        return total
    
    def getPromedioExamAprobados(self):
        return self.totalNotasAprobadas()/len(self.getExamenesAprobados())



# Ejemplo de uso
if __name__ == "__main__":
    dia=datetime.now()
    alumno1 = Alumno("Juan", [Examen(7), Examen(8), Examen(5)], dia)
    alumno2 = Alumno("María", [Examen(6), Examen(7), Examen(6)])
    carrera = Carrera()
    carrera.c_alumnos = [alumno1, alumno2]
    proms=carrera.calcular_promedios()
    for clave, valor in proms.items():
        print(f"{clave}: {valor}")