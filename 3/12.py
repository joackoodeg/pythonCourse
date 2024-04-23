from datetime import datetime
from typing import List

class Transaccion:
    def __init__(self, tipo, fecha, monto, moneda):
        self.tipo = tipo
        self.fecha = fecha
        self.monto = monto
        self.moneda = moneda

    def obtenerFecha(self):
        return self.fecha

    def obtenerMonto(self):
        return self.convertir_a_moneda('peso',tasa_de_cambio)

    def convertir_a_moneda(self, moneda_objetivo, tasa_de_cambio):
        if self.moneda == moneda_objetivo:
            return self.monto
        elif self.moneda == "peso" and moneda_objetivo == "dolar":
            return self.monto / tasa_de_cambio["peso_a_dolar"]
        elif self.moneda == "dolar" and moneda_objetivo == "peso":
            return self.monto * tasa_de_cambio["peso_a_dolar"]
        elif self.moneda == "peso" and moneda_objetivo == "real":
            return self.monto / tasa_de_cambio["peso_a_real"]
        elif self.moneda == "real" and moneda_objetivo == "peso":
            return self.monto * tasa_de_cambio["peso_a_real"]
        elif self.moneda == "dolar" and moneda_objetivo == "real":
            return self.monto * tasa_de_cambio["dolar_a_real"]
        elif self.moneda == "real" and moneda_objetivo == "dolar":
            return self.monto / tasa_de_cambio["dolar_a_real"]
        else:
            raise ValueError("Moneda no válida")

class Titular:
    def __init__(self,apellido,nombre,cuil):
        self.apellido=apellido
        self.nombre=nombre
        self.cuil=cuil

class Cuenta:
    def __init__(self, titular: Titular, nro, saldo=0):
        self._titular=titular
        self._transacciones=[]
        self._saldo=saldo #el saldo que se guarda es en dolares
        self.nro=nro

    def consultarNro(self):
        return self.nro

    def consultarSaldo(self):
        return  self._saldo
    
    def consultarTransacciones(self, fechaInicio, fechaFin):
        transacciones_entre_fechas = []
        for transaccion in self._transacciones:
            fecha_transaccion = datetime.strptime(transaccion.obtenerFecha(), "%Y-%m-%d")
            if fechaInicio <= fecha_transaccion <= fechaFin:
                transacciones_entre_fechas.append(transaccion)
        return transacciones_entre_fechas
        
    
    def consultarTitular(self):
        return self._titular

    def depositarSaldo(self, transaccion: Transaccion):
        self._transacciones.append(transaccion)
        self._saldo+=transaccion.convertir_a_moneda('dolar',tasa_de_cambio)

    def retirarSaldo(self, transaccion: Transaccion):
        self._transacciones.append(transaccion)
        self._saldo+=transaccion.convertir_a_moneda('dolar',tasa_de_cambio) #se deberia ingresar un numero negativo
    
class Banco:
    def __init__(self,nombre, cuentas: List['Cuenta']):
        self.nombre=nombre
        self.cuentas=cuentas

    def agregarCuenta(self,cuenta:Cuenta):
        self.cuentas.append(cuenta)
    
    def generarComision(self, cuenta: Cuenta, fechaInicio,FechaFin):
        transacciones_entre_fechas=cuenta.consultarTransacciones(fechaInicio,FechaFin)
        a = len(transacciones_entre_fechas)
        b=0
        for transaccion in transacciones_entre_fechas:
            b+= transaccion.obtenerMonto()
        return (30-((b/a)*0.005))

    def listarComisiones(self, fechaInicio, fechaFin):
        resultado = []
        for cuenta in self.cuentas:
            comision_data = {
                'nro': cuenta.consultarNro(),
                'comision': self.generarComision(cuenta, fechaInicio, fechaFin)
            }
        resultado.append(comision_data)  # Añadimos a la lista
        return resultado

if __name__ == '__main__':
    tasa_de_cambio = {"peso_a_dolar": 0.015, "dolar_a_real": 5.4, "peso_a_real": 0.003}

    # Crear titular
    titular = Titular("Pérez", "Juan", "123456789")

    # Crear cuenta
    cuenta = Cuenta(titular, "1234", saldo=1000)

    # Agregar transacciones a la cuenta
    transaccion1 = Transaccion("deposito", "2024-04-17", 500, "dolar")
    transaccion2 = Transaccion("extraccion", "2024-04-18", 200, "dolar")
    cuenta.depositarSaldo(transaccion1)
    cuenta.retirarSaldo(transaccion2)

    # Crear banco y agregar cuenta
    banco = Banco("Mi Banco", [])
    banco.agregarCuenta(cuenta)

    # Listar comisiones entre dos fechas
    fecha_inicio = datetime.strptime("2024-04-17", "%Y-%m-%d")
    fecha_fin = datetime.strptime("2024-04-18", "%Y-%m-%d")
    comis = banco.listarComisiones(fecha_inicio, fecha_fin)
    for c in comis:
        print(f"Número de cuenta: {c['nro']}, Comisión: {c['comision']}")