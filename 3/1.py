class Persona:
    def __init__(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad
    
class Principal:
    def __init__(self):
        pass
    
    def ejecutar(self):
        p1= Persona('p1',25)
        p2= Persona('p2',50)

        print('ident p1: ', id(p1))
        print('ident p2: ', id(p2))

        if p1 is p2:
            print('son iguales')
        else:
            print('no son iguales')

if __name__ == "__main__":
    principal = Principal()
    principal.ejecutar()