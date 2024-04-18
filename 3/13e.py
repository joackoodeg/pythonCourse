"""
Viola el principio de segregacion de interfaces,, dsp amplio xd 

"""

from abc import ABC, abstractmethod
class IUsuario(ABC):
    @abstractmethod
    def buscar_libro(self):
        pass

class IPrestamoLibro(ABC):
    @abstractmethod
    def solicitar_prestamo_libro(self):
        pass

class IDevolucionLibro(ABC):
    @abstractmethod
    def devolver_libro(self):
        pass

class IReservaSala(ABC):
    @abstractmethod
    def solicitar_reserva_sala_estudio(self):
        pass

class Estudiante(IUsuario, IPrestamoLibro, IDevolucionLibro):
    def solicitar_prestamo_libro(self):
        print("Estudiante solicitando préstamo de libro.")
    def devolver_libro(self):
        print("Estudiante devolviendo libro.")
    def buscar_libro(self):
        print("Estudiante buscando libro en el catálogo.")

class Profesor(IUsuario,IPrestamoLibro, IDevolucionLibro):
    def solicitar_prestamo_libro(self):
        print("Profesor solicitando préstamo de libro.")
    def devolver_libro(self):
        print("Profesor devolviendo libro.")
    def buscar_libro(self):
        print("Profesor buscando libro en el catálogo.")
    def solicitar_reserva_sala_estudio(self):
        print("Profesor solicitando reserva de sala de estudio.")

if __name__ == "__main__":
    # Ejemplo de uso
    estudiante = Estudiante()
    profesor = Profesor()
    estudiante.solicitar_prestamo_libro()
    estudiante.devolver_libro()
    estudiante.buscar_libro()
    
    profesor.solicitar_prestamo_libro()
    profesor.devolver_libro()
    profesor.buscar_libro()
    profesor.solicitar_reserva_sala_estudio()