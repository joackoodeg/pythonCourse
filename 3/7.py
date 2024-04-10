class Pais:
    def __init__(self, nombre, impuesto):
        self.nombre = nombre
        self.impuesto = impuesto

    def es_argentina(self):
        return self.nombre.lower() == 'argentina'

class Vehiculo:
    def __init__(self, marca, modelo, patente, precio_venta, kilometraje,
                 duenio=None):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.precio_venta = precio_venta
        self.kilometraje = kilometraje
        self.duenio = duenio

    def es_auto_nacional(self):
        return False

class Auto(Vehiculo):
    def __init__(self, marca, modelo, patente, precio_venta, kilometraje, pais):
        super().__init__(marca, modelo, patente, precio_venta, kilometraje)
        self.pais = pais

    def es_auto_nacional(self):
        return self.pais.es_argentina()

class Moto(Vehiculo):
    def __init__(self, marca, modelo, patente, precio_venta, kilometraje):
        super().__init__(marca, modelo, patente, precio_venta, kilometraje)

class Camioneta(Vehiculo):
    def __init__(self, marca, modelo, patente, precio_venta, kilometraje):
        super().__init__(marca, modelo, patente, precio_venta, kilometraje)


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

class Venta:
    def __init__(self, fecha, comprador):
        self.fecha = fecha
        self.comprador = comprador
        self.detalles_venta = []

    def es_venta_auto_nacional(self):
        ...

    def agregar_detalle_venta(self, detalle_venta):
        self.detalles_venta.append(detalle_venta)

    def mostrar_autos_usados_nacionales(self):
        resultado = []
        for detalle in self.detalles_venta:
            if detalle.es_usado() and detalle.vehiculo.es_auto_nacional():
                resultado.append(detalle.vehiculo)
        return resultado

class DetalleVenta:
    def __init__(self, venta, vehiculo):
        self.venta = venta
        self.vehiculo = vehiculo

    def es_usado(self):
        return self.vehiculo.duenio != None

class Concesionaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ventas = []

    def agregar_venta(self, venta: Venta) -> Venta:
        self.ventas.append(venta)

    def calc_ventas_nacionales_usados(self):
        # Implementar una función que permita calcular y mostrar el total
        # acumulado de ventas que incluyan únicamente AUTOS NACIONALES USADOS,
        # considerando solo aquellos que tengan registrado un dueño previo.
        acc = 0
        for venta in self.ventas:
            autos = venta.mostrar_autos_usados_nacionales()
            for auto in autos:
                acc += auto.precio_venta
        print(f'Total acumulado de autos nacionales usados con dueño: ${acc}')


macua = Concesionaria('Macua')
argentina = Pais('Argentina', 0)

pedro = Duenio('Pedro', 'Gomez', 3425694856)
juan = Cliente('Juan', 'Perez', 35839854)
venta_juan = Venta('20240329', juan)

corsa98 = Auto('Chevrolet', 'Corsa', 'JKK849', 3000000, 500000, argentina)
corsa98.duenio = pedro

detalle0_venta_corsa = DetalleVenta(venta_juan, corsa98)

venta_juan.agregar_detalle_venta(detalle0_venta_corsa)
macua.agregar_venta(venta_juan)

macua.calc_ventas_nacionales_usados()
