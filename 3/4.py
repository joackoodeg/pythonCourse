import datetime
import hashlib

class Persona:
    def __init__(self, nombre, apellido, fecha_nacimiento,passw):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.edad = None
        self.password = self.hashPass(passw)
        
    def hashPass(self, password):
        password_bytes = password.encode('utf-8')
        hash_object = hashlib.sha256(password_bytes)
        password_hash = hash_object.hexdigest()
        return password_hash

    def calcular_edad(self):
        hoy = datetime.date.today()
        edad = hoy.year - self.fecha_nacimiento.year
        return edad

    def mostrar(self):
        self.edad = self.calcular_edad()
        print(f"{self.apellido}, {self.nombre}: {self.edad} años.")

    def validar_password(self,password):
        if self.password == self.hashPass(password):
            return True
        else:
            return False
        
def main():
    juan = Persona("Juan", "Perez", "1990-11-11", "password")
    print(juan.validar_password("password"))

main()