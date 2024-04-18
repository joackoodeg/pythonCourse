from abc import ABC, abstractmethod

class MedioComunicacion(ABC):
    @abstractmethod
    def enviar_notificacion(self, destinatario: str, mensaje: str):
        pass

class CorreoElectronico(MedioComunicacion):
    def enviar_notificacion(self, destinatario: str, mensaje: str):
        # Lógica para enviar notificación por correo electrónico
        print(f"Correo electrónico enviado a {destinatario}: {mensaje}")
    
class Sms(MedioComunicacion):
    def enviar_notificacion(self, destinatario: str, mensaje: str):
        # Lógica para enviar notificación por correo electrónico
        print(f"Sms enviado a {destinatario}: {mensaje}")

class Notificador:
    def __init__(self, medio_comunicacion: MedioComunicacion):
        self.medio_comunicacion = medio_comunicacion
    
    def enviar_notificacion(self, destinatario: str, mensaje: str):
        self.medio_comunicacion.enviar_notificacion(destinatario, mensaje)

if __name__ == "__main__":
    # Uso del código actual
    correo_electronico = CorreoElectronico()
    notificador = Notificador(correo_electronico)
    notificador.enviar_notificacion("usuario@example.com", "¡Tu tarea está lista!")

    # Uso del código con OtroMedio
    sms = Sms()
    notificador_otro = Notificador(sms)
    notificador_otro.enviar_notificacion("usuario@example.com", "¡Tu tarea está lista!")