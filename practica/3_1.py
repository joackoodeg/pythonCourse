import datetime

class Facultad:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__carreras=[]
    
    def mostrarCarreraYAlumnos(self):
        print(self.__nombre)
        print("\n")
        for carrera in self.__carreras:
            print(carrera.getNombre())
            carrera.mostrarAlumnos()

    def addCarrera(self, carrera):
        self.__carreras.append(carrera)

class Carrera:
    def __init__(self,nombre):
        self.__nombre=nombre
        self.__inscripciones=[]
    
    def getNombre(self):
        return self.__nombre

    def mostrarAlumnos(self):
        for inscripcion in self.__inscripciones:
            print(f" -- {inscripcion.getAlumno().getNombre()}, {inscripcion.getFecha()}")

    def addInscripcion(self, inscripcion):
        self.__inscripciones.append(inscripcion)

class Alumno:
    def __init__(self,nombre,dni,fecha):
        self.__nombre=nombre
        self.__dni=dni
        self.__fecha=fecha
        self.__edad=self.__calcular_edad()
    
    def __calcular_edad(self):
        hoy = datetime.date.today()
        if(hoy.month < self.__fecha.month):
            edad = (hoy.year - self.__fecha.year)-1
        else:
            edad = (hoy.year - self.__fecha.year)
        return edad
    
    def getNombre(self):
        return self.__nombre
    
    def getDNI(self):
        return self.__dni
    
    def getEdad(self):
        return self.__edad
    
    
class Inscripcion:
    def __init__(self, fecha, alumno, carrera):
        self.__alumno = alumno
        self.__carrera = carrera
        self.__fecha=fecha
    
    def getAlumno(self):
        return self.__alumno
    
    def getCarrera(self):
        return self.__carrera
    
    def getFecha(self):
        return self.__fecha

if __name__ == "__main__":
    fa = Facultad("FICH")
    ca1= Carrera("Ingenieria Informatica")
    ca2 = Carrera("Ingenieria en RH")

    fa.addCarrera(ca1)
    fa.addCarrera(ca2)

    fn1= datetime.date(1992, 10, 25)
    al1=Alumno("Carlos", 11111, fn1)
    fi1= datetime.date(2020, 10, 25)
    ins1=Inscripcion(fi1,al1,ca1)
    ca1.addInscripcion(ins1)

    fn2= datetime.date(1995, 11, 5)
    al2=Alumno("Hernan", 2222, fn2)
    fi2= datetime.date(2021, 11, 20)
    ins2=Inscripcion(fi2,al2,ca1)
    ca1.addInscripcion(ins2)

    fa.mostrarCarreraYAlumnos()



