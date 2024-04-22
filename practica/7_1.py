from abc import ABC, abstractmethod

class Pais:
    def __init__(self, nombre, impuesto):
        self.nombre=nombre
        self.impuesto=impuesto

    def getNombre(self):
        return self.nombre
    
    def getImpuesto(self):
        return self.impuesto
    
    def es_argentina(self):
        return self.nombre.lower() == 'argentina'

class Vehiculo:
    def __init__(self, marca, modelo, patente, precioVenta, kilometraje, duenio=None):
        self.marca=marca
        self.modelo=modelo
        self.patente=patente
        self.precioVenta=precioVenta
        self.kilometraje=kilometraje
        self.duenio=duenio

    def getPrecio(self):
        return self.precioVenta

    def getDuenio(self):
        return self.duenio

    @abstractmethod
    def es_nacional(self):
        pass
    

class Auto(Vehiculo):
    def __init__(self, marca, modelo, patente, precioVenta, kilometraje, origen, duenio=None):
        super().__init__(marca, modelo, patente, precioVenta, kilometraje, duenio)
        self.origen=origen

    def es_nacional(self):
       return self.origen.es_argentina()
    
class Moto(Vehiculo):
    def __init__(self, marca, modelo, patente, precioVenta, kilometraje):
        super().__init__(marca, modelo, patente, precioVenta, kilometraje)

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, patente, precioVenta, kilometraje):
        super().__init__(marca, modelo, patente, precioVenta, kilometraje)

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido)
        self.dni = dni

class Duenio(Persona):
    def __init__(self, nombre, apellido, telefono):
        super().__init__(nombre, apellido)
        self.telefono = telefono

class DetalleVenta:
    def __init__(self, nro, vehiculo: Vehiculo):
        self.nro=nro
        self.vehiculo=vehiculo

    def getVehiculo(self):
        return self.vehiculo
    
    def es_usado(self):
        return self.vehiculo.getDuenio() == None
    
    def es_nacional(self):
        return self.vehiculo.es_nacional()

class Venta:
    def __init__(self, fecha, comprador: Cliente):
        self.fecha=fecha
        self.comprador=comprador
        self.detalles_venta=[]

    def agregar_detalle_venta(self, detalleVenta):
        self.detalles_venta.append(detalleVenta)

    def autos_nacionales_usados(self):
        resultado=[]
        for detalle in self.detalles_venta:
            print(detalle.es_usado())
            if detalle.es_usado() and detalle.es_nacional():
                resultado.append(detalle.getVehiculo())
        return resultado
        
class Concesionaria:
    def __init__(self, nombre):
        self.nombre=nombre
        self.ventas=[]

    def addVenta(self, venta: Venta) -> Venta:
        self.ventas.append(venta)

    def total_autos_nacionales_usados(self):
        total=0
        for venta in self.ventas:
            autos=venta.autos_nacionales_usados()
            for auto in autos:
                total+=auto.getPrecio()
        return total
    

if __name__ == "__main__":
    macua = Concesionaria('Macua')
    argentina = Pais('argentina', 0)

    pedro = Duenio('Pedro', 'Gomez', 3425694856)
    juan = Cliente('Juan', 'Perez', 35839854)
    venta_juan = Venta('20240329', juan)

    corsa98 = Auto('Chevrolet', 'Corsa', 'JKK849', 3000000, 500000, argentina)

    detalle0_venta_corsa = DetalleVenta(venta_juan, corsa98)

    venta_juan.agregar_detalle_venta(detalle0_venta_corsa)
    macua.addVenta(venta_juan)

    total = macua.total_autos_nacionales_usados()
    print(total)
    