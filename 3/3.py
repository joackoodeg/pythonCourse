import datetime

class Facultad:
    def __init__(self,nombre):
        self.nombre=nombre
        self.carreras=[]
    
    def mostrarCarreraYAlumnos(self):
        print(self.nombre)
        print("\n")
        for carrera in self.carreras:
            print(carrera.nombre)
            carrera.mostrarAlumnos()

    def addCarrera(self, carrera):
        self.carreras.append(carrera)

class Carrera:
    def __init__(self,nombre):
        self.nombre=nombre
        self.alumnos=[]
        self.inscripcion=[]
    
    def mostrarAlumnos(self):
        for inscripcion in self.inscripcion:
            print(f" -- {inscripcion.alumno.nombre}, {inscripcion.fecha}")

    def addAlumno(self, alumno):
        self.alumnos.append(alumno)

    def addInscripcion(self, inscripcion):
        self.inscripcion.append(inscripcion)

class Alumno:
    def __init__(self,nombre,dni,fecha):
        self.nombre=nombre
        self.dni=dni
        self.fecha=fecha
        self.edad=self.calcular_edad()
        self.carrera=[]
        self.inscripcion=None
    
    def calcular_edad(self):
        hoy = datetime.date.today()
        edad = hoy.year - self.fecha.year
        return edad
    
    def addCarrera(self,carrera):
        self.carrera.append(carrera)
    

    
class Inscripcion:
    def __init__(self, fecha, alumno, carrera):
        self.alumno = alumno
        self.carrera = carrera
        self.carrera.addAlumno(alumno)
        self.alumno.addCarrera(carrera)
        self.fecha=fecha


def main():
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
    
    

if __name__ == "__main__":
    main()



