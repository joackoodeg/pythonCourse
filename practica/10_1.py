from typing import List
from datetime import datetime

class Persona:
    def __init__(self, nombre, dni):
        self.nombre=nombre
        self.dni=dni
    
    def getNombre(self):
        return self.nombre
    
    def getDni(self):
        return self.dni

class Docente(Persona):
    def __init__(self,nombre,dni,matricula):
        super().__init__(nombre,dni)
        self.matricula=matricula

class Comision:
    def __init__(self, id, docente: Docente, fecha, alumnos: List['Alumno']) -> None:
        self.id=id
        self.docenteAcargo=docente
        self.fecha=fecha
        self.alumnos=alumnos

    def getDocente(self):
        return self.docente

    def addAlumno(self, alumno):
        self.alumnos.append(alumno)

    def getAlumnos(self):
        return self.alumnos
    


class Catedra:
    def __init__(self, nombre, nro, comisiones:list['Comision']=None):
        self.nombre=nombre
        self.nro=nro
        self.comisiones=comisiones

    def addComision(self, comision: Comision):
        self.comisiones.append(comision)

    def getComisiones(self):
        return self.comisiones


class Carrera:
    def __init__(self, nombre, catedras:List['Comision']=None):
        self.nombre=nombre
        self.catedras=catedras

    def addCatedra(self, catedra:Catedra):
        self.catedras.append(catedra)

    def getCatedras(self):
        return self.catedras

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
        

class Alumno(Persona):
    def __init__(self, nombre: str, dni ,carreras: list['Carrera'], fecha_egreso: datetime = None):
        super().__init__(nombre,dni)
        self.fecha_egreso = fecha_egreso
        self.carreras=carreras
        self.examenes = []
        self.catedras=[]

    def addCatedra(self, catedra: Catedra):
        self.catedras.append(catedra)
    
    def getCatedras(self):
        return self.catedras

    def addExamen(self, examen:Examen):
        self.examenes.append(examen)

    def addCarrera(self, carrera: Carrera):
        self.carreras.append(carrera)

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

class Universidad:
    def __init__(self,nombre):
        self.nombre=nombre
        self.carreras=[]

    def addCarrera(self, carrera: Carrera):
        self.carreras.append(carrera)

    def listar_alumnos(self, catedra: Catedra):
        resultado=[]
        for comision in catedra.getComisiones():
            for alumno in comision.getAlumnos():
                resultado.append(alumno)
        return resultado

# Ejemplo de uso
if __name__ == "__main__":
    universidad = Universidad("Universidad Nacional")

    # Crear un docente
    docente = Docente("Profesor López", "12345678", "MAT123")

    # Crear algunas comisiones
    comision1 = Comision(1, docente, datetime.now(), [])
    comision2 = Comision(2, docente, datetime.now(), [])

    # Crear una cátedra con estas comisiones
    catedra = Catedra("Programación", 101, [comision1, comision2])

    # Crear la carrera y agregar la cátedra
    carrera = Carrera("Ingeniería", [catedra])
  
    # Agregar la carrera a la universidad
    universidad.addCarrera(carrera)
   
    # Crear algunos alumnos
    alumno1 = Alumno("Juan Pérez", "87654321", [carrera])
    alumno2 = Alumno("Ana García", "87654322", [carrera])
    
    # Asignar a la cátedra
    alumno1.addCatedra(catedra)
    alumno2.addCatedra(catedra)

    # Agregar a las comisiones
    comision1.addAlumno(alumno1)
    comision2.addAlumno(alumno2)

    # Crear exámenes y asignar al alumno
    examen1 = Examen(8.5)
    examen2 = Examen(6.0)

    alumno1.addExamen(examen1)
    alumno1.addExamen(examen2)
    
    # Calcular el promedio de notas aprobadas
    promedio = alumno1.getPromedioExamAprobados()
    print(f"Promedio de notas aprobadas para {alumno1.getNombre()}: {promedio}")

    alumnos_en_catedra = universidad.listar_alumnos(catedra)

    print("Alumnos inscritos en la cátedra de Programación:")
    for alumno in alumnos_en_catedra:
        print(f"- {alumno.getNombre()}")

    #CONSIGNA:
    alums=universidad.listar_alumnos(catedra)
    for al in alums:
        print(al.getNombre())
