import datetime

class Empresa:
    def __init__(self,nombre):
        self.nombre=nombre
        self.facturas=[]
    
    def addFactura(self,fa):
        self.facturas.append(fa)

class Factura:
    def __init__(self, nro, cliente):
        self.nro=nro
        self.cliente=cliente
        self.fecha=datetime.date.today()
        self.detalles=[]
    
    def addDetalle(self, detalle):
        self.detalles.append(detalle)

    def getTotal(self):
        total=0
        for detalle in self.detalles:
            total+=(detalle.getCantidad()*detalle.getProducto().precio)
        return total


class Cliente:
    def __init__(self,nombre,cuit):
        self.nombre=nombre
        self.cuit=cuit
    
class Producto:
    def __init__(self, nombre, precio):
        self.nombre=nombre
        self.precio=precio
    
    def getPrecio(self):
        return self.precio

class Detalle:
    def __init__(self, producto, cantidad):
        self.producto=producto
        self.cantidad=cantidad

    def getProducto(self):
        return self.producto
    
    def getCantidad(self):
        return self.cantidad

def main():
    em = Empresa("Mayorista S.A")
    fa= Factura(1,em)
    p1=Producto("Porcelanato", 100)
    p2=Producto("Griferia", 50)
    de1= Detalle(p1,2)
    de2= Detalle(p2,3)
    fa.addDetalle(de1)
    fa.addDetalle(de2)
    print(fa.getTotal())


if __name__ == "__main__":
    main()
    