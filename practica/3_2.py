from datetime import datetime

class Inscripcion:
    def __init__(self, fecha: datetime, carrera, alumno):
        self.fecha=fecha
        self.carrera=carrera
        self.alummno=alumno

    def getFecha(self):
        return self.fecha
    
    def getAlumno(self):
        return self.alummno
    
    def getCarrera(self):
        return self.carrera

class Alumno:
    def __init__(self,nombre,dni,fechaNac):
        self.nombre=nombre
        self.dni=dni
        self.fechaNac=fechaNac
        self.edad=self.calcular_edad()
        self.inscripciones=[]
        
    def calcular_edad(self):
        hoy = datetime.date.today()
        if(hoy.month < self.fecha.month):
            edad = (hoy.year - self.fecha.year)-1
        else:
            edad = (hoy.year - self.fecha.year)
        return edad
    
    def addInscripcion(self, inscripcion: Inscripcion):
        self.inscripciones.append(inscripcion)

    def getCarreras(self):
        carreras=[]
        for inscripcion in self.inscripciones:
            carreras.append(inscripcion.getCarrera())
        return carreras
    
    def getFechaInscripcion(self,carrera):
        for inscripcion in self.inscripciones:
            if(inscripcion.getCarrera()==carrera):
                return inscripcion.getFecha()
            else: return -1 

    def getEdad(self):
        return self.edad
    
    def getNombre(self):
        return self.nombre
    
    def getDNI(self):
        return self.dni
    
    def getFechaNacimiento(self):
        return self.fechaNac

class Carrera:
    def __init__(self, nombre):
        self.nombre=nombre
        self.inscripciones=[]

    def addInscripcion(self, inscripcion: Inscripcion):
        self.inscripciones.append(inscripcion)

    def getNombre(self):
        return self.nombre
    
    def getAlumnos(self):
        alumnos=[]
        for inscripcion in self.inscripciones:
            alumnos.append(inscripcion.getAlumno())
        return alumnos
        
class Facultad:
    def __init__(self, nombre):
        self.nombre=nombre
        self.carreras=[]
    
    def addCarrera(self, carrera: Carrera):
        self.carreras.append(carrera)

    def mostrarCarrerasyAlumnos(self):
        print("Nombre de facultad")
        for carrera in self.carreras:
            print(f"Nombre de la carrera {carrera.getNombre()}")
            for alumno in carrera.getAlumnos():
                print(f"nombre del alumno {alumno.getNombre()}")
                print(f"inscripto el {alumno.getFechaInscripcion()}")