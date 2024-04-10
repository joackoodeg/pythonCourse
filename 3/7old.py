class Vehiculo:
    def __init__(self, marca, modelo, patente, precio, kilometraje, estado, dueño_previo=None):
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self.precio = precio
        self.kilometraje = kilometraje
        self.estado = estado
        self.dueño_previo = dueño_previo

class Auto(Vehiculo): 
    def __init__(self, marca, modelo, patente, precio, kilometraje, estado, dueño_previo=None, nacional=True, pais_origen=None, impuesto_importacion=0):
        super().__init__(marca, modelo, patente, precio, kilometraje, estado, dueño_previo)
        self.nacional = nacional
        self.pais_origen = pais_origen
        self.impuesto_importacion = impuesto_importacion

class Venta:
    def __init__(self, monto, vehiculo, fecha, comprador):
        self.monto = monto
        self.vehiculo = vehiculo
        self.fecha = fecha
        self.comprador = comprador

ventas = []

def agregar_venta(monto, vehiculo, fecha, comprador):
    venta = Venta(monto, vehiculo, fecha, comprador)
    ventas.append(venta)

def calcular_total_ventas_autos_usados_con_dueño_previo():
    total_ventas = 0
    for venta in ventas:
        vehiculo = venta.vehiculo
        if isinstance(vehiculo, Auto) and vehiculo.estado == "usado" and vehiculo.dueño_previo is not None:
            total_ventas += venta.monto
    return total_ventas

# Ejemplo de uso
auto1 = Auto("Toyota", "Corolla", "ABC123", 20000, 50000, "usado", dueño_previo="Pérez Juan 12345678")
auto2 = Auto("Ford", "Fiesta", "DEF456", 15000, 40000, "usado", dueño_previo="Gómez María 87654321")
auto3 = Auto("Chevrolet", "Cruze", "GHI789", 18000, 60000, "nuevo")
65
agregar_venta(21000, auto1, "2024-04-01", "Martínez Luis 98765432")
agregar_venta(16000, auto2, "2024-04-02", "Rodríguez Ana 45678901")
agregar_venta(19000, auto3, "2024-04-03", "González Pablo 34567890")

total_ventas_autos_usados_con_dueño_previo = calcular_total_ventas_autos_usados_con_dueño_previo()
print("Total acumulado de ventas de autos usados con dueño previo:", total_ventas_autos_usados_con_dueño_previo)