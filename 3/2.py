import datetime

class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = None
    
    def calcular_edad(self):
        hoy = datetime.date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        return edad

    def mostrar(self):
        self.edad = self.calcular_edad()
        print(f"{self.apellido}, {self.nombre}: {self.edad} años.")


class Principal:
    def __init__(self):
        pass
    
    def ejecutar(self):
        fecha_nacimiento_persona1 = datetime.date(1990, 5, 15)
        persona1 = Persona("Juan", "Perez", fecha_nacimiento_persona1)
        persona1.mostrar()

        fecha_nacimiento_persona2 = datetime.date(1992, 10, 25)
        persona2 = Persona("Carols", "Sanchez", fecha_nacimiento_persona1)
        persona2.mostrar()

        print('ident p1: ', id(persona1))
        print('ident p2: ', id(persona2))

        if persona1 is persona2:
            print('son iguales')
        else:
            print('no son iguales')

if __name__ == "__main__":
    principal = Principal()
    principal.ejecutar()