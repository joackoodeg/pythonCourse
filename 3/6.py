class Empleado:
    def __init__(self, nombre,apellido,direccion,dni):
        self.nombre=nombre
        self.apellido=apellido
        self.direccion=direccion
        self.dni=dni
        self.jefe=None

    def asignar_jefe(self,jefe):
        self.jefe=jefe
        
class Mensualizado(Empleado):
    def __init__(self, nombre, apellido, direccion, dni, categoria, salario_mensual):
        super().__init__(nombre, apellido, direccion, dni)
        self.categoria = categoria
        self.salario_mensual = salario_mensual

    def calcular_remuneracion(self):
        return self.salario_mensual



class Jornalizado(Empleado):
    def __init__(self, nombre, apellido, direccion, dni, precio_hora_fijo, precio_hora_extra):
        super().__init__(nombre, apellido, direccion, dni)
        self.precio_hora_fijo = precio_hora_fijo
        self.precio_hora_extra = precio_hora_extra
        self.horas_trabajadas = 0

    def registrar_horas_trabajadas(self, horas):
        self.horas_trabajadas += horas

    def calcular_remuneracion(self):
        if self.horas_trabajadas <= 40:
            return self.horas_trabajadas * self.precio_hora_fijo
        else:
            horas_extra = self.horas_trabajadas - 40
            return (40 * self.precio_hora_fijo) + (horas_extra * self.precio_hora_extra)


class Jefe(Empleado):
    def __init__(self, nombre, apellido, direccion, dni, salario_fijo):
        super().__init__(nombre, apellido, direccion, dni)
        self.salario_fijo = salario_fijo

    def calcular_remuneracion(self):
        return self.salario_fijo

def main():
    # Ejemplo de uso dado por GPT
    jefe_principal = Jefe("Juan", "Pérez", "Av. Principal 123", "12345678", salario_fijo=5000)
    empleado1 = Mensualizado("Ana", "Gómez", "Calle Secundaria 456", "98765432", "Categoria A", salario_mensual=3000)
    empleado2 = Jornalizado("Carlos", "López", "Av. Libertad 789", "56789012", precio_hora_fijo=10, precio_hora_extra=15)

    # Asignar jefe a los empleados
    empleado1.asignar_jefe(jefe_principal)
    empleado2.asignar_jefe(jefe_principal)

    # Calcular remuneración de los empleados
    print("Remuneración de", empleado1.nombre, empleado1.apellido, ":", empleado1.calcular_remuneracion())
    empleado2.registrar_horas_trabajadas(100)
    print("Remuneración de", empleado2.nombre, empleado2.apellido, ":", empleado2.calcular_remuneracion())

    

if __name__ == "__main__":
    main()


    
    