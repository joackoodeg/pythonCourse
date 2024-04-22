from abc import ABC, abstractmethod
from datetime import datetime

class RolUsuarioDTO:
    def __init__(self,usuario):
        self.usuario=usuario

    @abstractmethod
    def es_comensal(self):
        pass

    @abstractmethod
    def getFacultad(self):
        return None
    
    @abstractmethod
    def getSaldo(self):
        return None

class RolAdminDto(RolUsuarioDTO):
    def __init__(self,usuario,clave):
        super().__init__(usuario)
        self.clave=clave
    
    def es_comensal(self):
        return False
    
    def getFacultad(self):
        return None
    
    def getSaldo(self):
        return None

class RolComensalDTO(RolUsuarioDTO):
    def __init__(self, usuario,ultimoAcceso, tokenSesion, facultad):
        super().__init__(usuario)
        self.ultimoAcceso=ultimoAcceso
        self.tokenSesion=tokenSesion
        self.facultad=facultad
        self.cupones=[]

    def es_comensal(self):
        return True

    def getFacultad(self):
        return self.facultad.getNombre()
    
    def addCupon(self,cupon):
        self.cupones.append(cupon)

    def getSaldo(self):
        saldo=0
        for cupon in self.cupones:
            if not cupon.es_entregado():
               saldo+=1
        return saldo

class RolVentanillaDTO(RolUsuarioDTO):
    def __init__(self,usuario, clave, comedor):
        super().__init__(usuario)
        self.clave=clave
        self.comedor=comedor

    def es_comensal(self):
        return False
    
    def getFacultad(self):
        return None
    
    def getSaldo(self):
        return None
    
class UsuarioDTO:
    def __init__(self, apellido, nombre, correo):
        self.apellido=apellido
        self.nombre=nombre
        self.correo=correo
        self.roles=[]

    def getNombre(self):
        return self.nombre
    
    def getCorreo(self):
        return self.correo

    def addRol(self, rol: RolUsuarioDTO):
        self.roles.append(rol)

    def mas_de_un_rol(self):
        if len(self.roles)>1:
            return True
        else:
            return False

    def es_comensal(self):
            for rol in self.roles:
                if rol.es_comensal():
                    return True 
            return False
    
    def getFacultad(self):
        for rol in self.roles:
            if rol.es_comensal():
                return rol.getFacultad()
        return None
    
    def getSaldo(self):
        for rol in self.roles:
            if rol.es_comensal():
                return rol.getSaldo()
        return None

    
class ComedorDTO:
    def __init__ (self, descripcion, domicilio):
        self.descripcion=descripcion
        self.domicilio=domicilio
        self.entregas=[]

    def addEntrega(self,entrega):
        self.entregas.append(entrega)

class Entrega:
    def __init__(self,fecha, comedor, cupon, ventanilla):
        self.fecha=fecha
        self.comedor=comedor
        self.cupon=cupon
        self.ventanilla=ventanilla

class Cupon:
    def __init__(self,id, fecha):
        self.id=id
        self.fecha=fecha
        self.entregas=[]

    def addEntrega(self,entrega):
        self.entregas.append(entrega)

    def es_entregado(self):
        if len(self.entregas)>=1:
            return True
        else: return False

class Facultad:
    def __init__(self,sigla):
        self.sigla=sigla

    def getNombre(self):
        return self.sigla

class Universidad:
    def __init__(self,nombre):
        self.nombre=nombre
        self.facultades=[]
        self.comedorDtos=[]
        self.usuarioDtos=[]

    def addFacultad(self,facultad):
        self.facultades.append(facultad)
    
    def addComedorDto(self,comedorDto):
        self.comedorDtos.append(comedorDto)

    def adddUsuarioDto(self,usuarioDto):
        self.usuarioDtos.append(usuarioDto)

    def listar_usuarios_rol_comensal(self):
        """"
        Listar los usuarios que tengan más de un ROL y a su vez sean COMENSALES. De estos COMENSALES mostrar la siguiente información por
        consola:
        Apellido y Nombre + Facultad + Saldo
        El saldo son la sumatoria de cupones sin consumir (que no estén entregados)
        """
        for usuario in self.usuarioDtos:
            if usuario.mas_de_un_rol() and usuario.es_comensal():
                print(usuario.getNombre(), usuario.getCorreo(), usuario.getFacultad(), usuario.getSaldo())

if __name__=="__main__":
    """
    
    UNL = Universidad("Universidad Nacional del Litoral")
    FICH = Facultad ("Ingeniería y ciencias hídricas")
    U1 = UsuarioDTO("Pepa", "Torrez", "pepa@gmail.com")
    U2 = UsuarioDTO("Pepe", "Gimenez", "pepe@gmail.com")
    U3 = UsuarioDTO("Carlos", "Gomez", "pepi@gmail.com")
    com = ComedorDTO("Comedor UNL", "predio UNL-ATE")
    rolA = RolAdminDto(U1, 123)
    rolV = RolVentanillaDTO(U2, 234, com)
    rolC = RolComensalDTO(U3, datetime(2023,12,25), "aaa111", FICH)
    C1 = Cupon("abc123", datetime(2023,3,3))
    C2 = Cupon("abc234", datetime(2023,4,4))
    E = Entrega(datetime(2024,3,3), C1, com, rolV)

    UNL.addFacultad(FICH)
    UNL.adddUsuarioDto(U1)
    UNL.adddUsuarioDto(U2)
    UNL.adddUsuarioDto(U3)
    UNL.addComedorDto(com)

    #Usuario con 2 roles con comensal
    U1.addRol(rolA)
    U1.addRol(rolC)
    #Usuario comensal pero con solo 1 rol
    U2.addRol(rolC)
    #Usuario con 2 roles sin comensal
    U3.addRol(rolV)

    rolC.addCupon(C1)
    rolC.addCupon(C2)

    C1.addEntrega(E)

    com.addEntrega(E)

    UNL.listar_usuarios_rol_comensal()

    """

    """
    EJ DE USO POR CHATGPT:
    """
    # Crear la Universidad
    universidad = Universidad("Universidad Nacional")

    # Crear algunas Facultades
    facultad_ciencias = Facultad("Ciencias")
    facultad_ingenieria = Facultad("Ingeniería")

    universidad.addFacultad(facultad_ciencias)
    universidad.addFacultad(facultad_ingenieria)

    # Crear algunos usuarios
    usuario1 = UsuarioDTO("Gomez", "Juan", "juan.gomez@example.com")
    usuario2 = UsuarioDTO("Lopez", "Ana", "ana.lopez@example.com")

    # Crear algunos roles
    rol_comensal_juan = RolComensalDTO(usuario1, datetime.now(), "token1", facultad_ciencias)
    rol_admin_juan = RolAdminDto(usuario1, "clave123")

    rol_comensal_ana = RolComensalDTO(usuario2, datetime.now(), "token2", facultad_ingenieria)
    rol_ventanilla_ana = RolVentanillaDTO(usuario2, "clave456", "Comedor Central")

    # Agregar roles a los usuarios
    usuario1.addRol(rol_comensal_juan)
    usuario1.addRol(rol_admin_juan)

    usuario2.addRol(rol_comensal_ana)
    usuario2.addRol(rol_ventanilla_ana)

    # Agregar cupones al rol comensal de Juan
    cupon1 = Cupon("cupon001", datetime.now())
    cupon2 = Cupon("cupon002", datetime.now())
    cupon3 = Cupon("cupon003", datetime.now())
    cupon4 = Cupon("cupon004", datetime.now())

    rol_comensal_juan.addCupon(cupon1)
    rol_comensal_juan.addCupon(cupon2)
    rol_comensal_juan.addCupon(cupon3)
    rol_comensal_juan.addCupon(cupon4)

    # Entrega algunos cupones para cambiar su estado a entregado
    entrega1 = Entrega(datetime.now(), "Comedor Central", cupon1, "Ventanilla 1")
    cupon1.addEntrega(entrega1)

    # Agregar usuarios a la universidad
    universidad.adddUsuarioDto(usuario1)
    universidad.adddUsuarioDto(usuario2)

    # Listar los usuarios 
    universidad.listar_usuarios_rol_comensal()

