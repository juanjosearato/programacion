# Una empresa privada que se dedica a la venta de cursos de oficios, desea desarrollar un
#sistema web para poder publicar su oferta académica. Dicho sistema debe mostrar una serie
#de cursos disponibles.
# Modelar las clases (entidad) necesarias (Cursos, Categoría, Clase)
# crear: Deficinicion, Atributos, Contructor, Métodos (ejemplo: imprimir datos), getters y setters

#    def imprimir_dato(self):
#        print(f"Nombre de Escuela: {self.get_nombreEscuela}")
#        print(f"Dirección: {self.get_direccion}")

class Cursos:
    fechacomienzo=""
    titulo=""
    descripcion=""
    objetivos=""
    programa=""
    costo=""
    duracionEnMeses=""
    foto=""
    estado=""

# estado (disponible o no disponible, en base a su estado deberán verse o no en el sitio).

    def __init__(self, FechaComienzo, Titulo, Descripcion, Objetivos, Programa, Costo, DuracionEnMeses, Foto, Estado):
        self.fechacomienzo=FechaComienzo
        self.titulo=Titulo
        self.descripcion=Descripcion
        self.objetivos=Objetivos
        self.programa=Programa
        self.costo=Costo
        self.duracionEnMeses=DuracionEnMeses
        self.foto=Foto
        self.estado=Estado

    def getFechaComienzo(self):
        return self.fechacomienzo
    def getTitulo(self):
        return self.titulo
    def getDescripcion(self):
        return self.descripcion
    def getObjetivos(self):
        return self.objetivos
    def getPrograma(self):
        return self.programa
    def getCosto(self):
        return self.costo
    def getDuracionEnMeses(self):
        return self.duracionEnMeses
    def getFoto(self):
        return self.foto
    def getEstado(self):
        return self.estado


    def setfechacomienzo(self,FechaComienzo):
        self.fechaComienzo=FechaComienzo
    def settitulo(self,Titulo):
        self.titulo=Titulo
    def setdescripcion(self,Descripcion):
        self.descripcion=Descripcion
    def setobjetivos(self,Objetivos):
        self.objetivos=Objetivos
    def setprograma(self,Programa):
        self.programa=Programa
    def setcosto(self,Costo):
        self.costo=Costo
    def setduracionEnMeses(self,DuracionEnMeses):
        self.duracionEnMeses=DuracionEnMeses
    def setfoto(self,Foto):
        self.foto=Foto
    def setestado(self,Estado):
        self.estado=Estado


class Categorias:
    inicial=""
    intermendio=""
    avanzado=""

    def __init__(self, Inicial, Intermedio, Avanzado):
        self.inicial=Inicial
        self.intermedio=Intermedio
        self.avanzado=Avanzado

    def getInicial(self):
        return self.inicial
    def getIntermedio(self):
        return self.intermendio
    def getAvanzado(self):
        return self.avanzado
    

    def setinicial(self,Inicial):
        self.inicial=Inicial
    def setintermendio(self,Intermedio):
        self.intermedio=Intermedio
    def setavanzado(self,Avanzado):
        self.avanzado=Avanzado


class Clase:
    fecha=""
    titulo=""
    contenido=""
    URLDrive=""

    def __init__(self, Fecha, Titulo, Contenido, URLDRIVE):
        self.fecha=Fecha
        self.titulo=Titulo
        self.contenido=Contenido
        self.URLDrive=URLDRIVE

    def getfecha(self):
        return self.fecha
    def gettitulo(self):
        return self.titulo
    def getcontenido(self):
        return self.contenido
    def getURLDrive(self):
        return self.URLDrive
    

    def setfecha(self,Fecha):
        self.fecha=Fecha
    def settitulo(self,Titulo):
        self.titulo=Titulo
    def setcontenido(self,Contenido):
        self.contenido=Contenido
    def setURLDrive(self,URLDRIVE):
        self.URLDrive=URLDRIVE


class Docentes:
    apellido=""
    nombre=""
    dni=int
    fechaNacimiento=int
    dirección=""
    localidad=""
    codigoPostal=int
    provincia=""
    telefonoCelular=int
    email=""

    def __init__(self, Apellido, Nombre, DNI, FechaNacimiento, Direccion, Localidad, CodigoPostal, Provincia, TelefonoCelular, Email):
        self.apellido=Apellido
        self.nombre=Nombre
        self.dni=DNI
        self.fechaNacimiento=FechaNacimiento
        self.direccion=Direccion
        self.localidad=Localidad
        self.codigoPostal=CodigoPostal
        self.provincia=Provincia
        self.telefonoCelular=TelefonoCelular
        self.email=Email

    def getapellido(self):
        return self.apellido
    def getnombre(self):
        return self.nombre
    def getdni(self):
        return self.dni
    def getfechaNacimiento(self):
        return self.fechaNacimiento
    def getdireccion(self):
        return self.direccion
    def getlocalidad(self):
        return self.localidad
    def getcodigoPostal(self):
        return self.codigoPostal
    def getprovincia(self):
        return self.provincia
    def gettelefonoCelular(self):
        return self.telefonoCelular
    def getemail(self):
        return self.email


    def setapellido(self,apellido):
        self.apellido=apellido
    def setnombre(self,nombre):
        self.nombre=nombre
    def setdni(self,dni):
        self.dni=dni
    def setfechaNacimiento(self,fechaNacimiento):
        self.fechaNacimiento=fechaNacimiento
    def setdireccion(self,direccion):
        self.direccion=direccion
    def setlocalidad(self,localidad):
        self.localidad=localidad
    def setcodigoPostal(self,codigoPostal):
        self.codigoPostal=codigoPostal
    def setprovincia(self,provincia):
        self.provincia=provincia
    def settelefonoCelular(self,telefonoCelular):
        self.telefonoCelular=telefonoCelular
    def setemail(self,email):
        self.email=email


class Usuarios:
    nombre=""
    apellido=""
    dni_II=int
    direccion=""
    fechaNacimiento=""
    localidad=""
    codigoPostal=""
    provincia=""
    telefonoCelular=""
    email=""
    clave=""
    reconfirmarClave=""
    estado=""

    def __init__(self, Nombre, Apellido, Dni_II, Direccion, FechaNacimiento, Localidad, CodigoPostal,
                 Provincia, TelefonoCelular, Email, Clave, ReconfirmarCalve, Estado):
        self.nombre=Nombre
        self.apellido=Apellido
        self.dni_II=Dni_II
        self.direccion=Direccion
        self.fechaNacimiento=FechaNacimiento
        self.localidad=Localidad
        self.codigoPostal=CodigoPostal
        self.provincia=Provincia
        self.telefonoCelular=TelefonoCelular
        self.email=Email
        self.clave=Clave
        self.reconfirmarClave=ReconfirmarCalve
        self.estado=Estado
        

    def getnombre(self):
        return self.nombre
    def getapellido(self):
        return self.apellido
    def getdni_II(self):
        return self.dni_II
    def getdireccion(self):
        return self.direccion
    def getfechaNacimiento(self):
        return self.fechaNacimiento
    def getlocalidad(self):
        return self.localidad
    def getcodigoPostal(self):
        return self.codigoPostal
    def getprovincia(self):
        return self.provincia
    def gettelefonoCelular(self):
        return self.telefonoCelular
    def getemail(self):
        return self.email
    def getclave(self):
        return self.clave
    def getreconfirmarClave(self):
        return self.reconfirmarClave
    def getestado(self):
        return self.estado
    
   
    def setnombre(self,nombre):
        self.nombre=nombre
    def setapellido(self,apellido):
        self.apellido=apellido
    def setdni_II(self,dni_II):
        self.dni_II=dni_II
    def setdireccion(self,direccion):
        self.direccion=direccion
    def setfechaNacimiento(self,fechaNacimiento):
        self.fechaNacimiento=fechaNacimiento
    def setdireccion(self,direccion):
        self.direccion=direccion
    def setlocalidad(self,localidad):
        self.localidad=localidad
    def setcodigoPostal(self,codigoPostal):
        self.codigoPostal=codigoPostal
    def setprovincia(self,provincia):
        self.provincia=provincia
    def settelefonoCelular(self,telefonoCelular):
        self.telefonoCelular=telefonoCelular
    def setemail(self,email):
        self.email=email
    def setclave(self,clave):
        self.clave=clave
    def setreconfirmarClave(self,reconfirmarClave):
        self.reconfirmarClave
    def setestado(self,estado):
        self.estado
    


class Carrito_Compra:
    foto=""
    titulo_del_curso=""
    duracion=""
    costo=""

    def __init__(self, Foto, Titulo_del_curso, Duracion, Costo):
        self.foto=Foto
        self.titulo_del_curo=Titulo_del_curso
        self.duracion=Duracion
        self.costo=Costo

    def getfoto(self):
        return self.foto
    def gettitulo_del_curso(self):
        return self.titulo_del_curso
    def getduracion(self):
        return self.duracion
    def getcosto(self):
        return self.costo
    

    def setfoto(self,Foto):
        self.foto=Foto
    def settitulo_del_curso(self,Titulo_del_curso):
        self.titulo_del_curso=Titulo_del_curso
    def setduracion(self,Duracion):
        self.duracion=Duracion
    def setcosto(self,Costo):
        self.costo=Costo

class Medio_Pago:
    tarjeta_debito=""
    tarjeta_credito=""
    transferencia_bancaria=""

    def __init__(self, Tarjeta_debito, Tarjeta_credito, Transferencia_bancaria):
        self.tarjeta_debito=Tarjeta_debito
        self.tarjeta_credito=Tarjeta_credito
        self.transferencia_bancaria=Transferencia_bancaria

    def gettarjeta_debito(self):
        return self.tarjeta_debito
    def gettarjeta_credito(self):
        return self.tarjeta_credito
    def gettransferencia_bancaria(self):
        return self.transferencia_bancaria
    

    def settarjeta_debito(self,Tarjeta_debito):
        self.tarjeta_debito=Tarjeta_debito
    def settarjeta_credito(self,Tarjeta_credito):
        self.tarjeta_credito=Tarjeta_credito
    def settransferenia_bancaria(self,Transferencia_bancaria):
        self.transferencia_bancaria=Transferencia_bancaria

class Datos_del_Pago:
    nombre_titular=""
    numero_tarjeta=int
    fecha_vencimiento=int
    dni=int

    def __init__(self, Nombre_titular, Numero_tarjeta, Fecha_vencimiento, Dni):
        self.nombre_titular=Nombre_titular
        self.numero_tarjeta=Numero_tarjeta
        self.fecha_vencimiento=Fecha_vencimiento
        self.dni=Dni

    def getnombre_titular(self):
        return self.nombre_titular
    def getnumero_tarjeta(self):
        return self.numero_tarjeta
    def getfecha_vencimiento(self):
        return self.fecha_vencimiento
    

    def setnombre_titular(self,Nombre_titular):
        self.nombre_titular=Nombre_titular
    def setnumero_tarjeta(self,Numero_tarjeta):
        self.numero_tarjeta=Numero_tarjeta
    def setfecha_vencimiento(self,Fecha_vencimiento):
        self.fecha_vencimiento=Fecha_vencimiento
