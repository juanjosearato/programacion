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

class Categorias:
    inicial=""
    intermendio=""
    avanzado=""

class Clase:
    fecha=""
    titulo=""
    contenido=""
    URLDrive=""

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

class Carrito_Compra:
    foto=""
    titulo_del_curso=""
    duracion=""
    costo=""

class Medio_Pago:
    tarjeta_debito=""
    tarjeta_credito=""
    transferencia_bancaria=""

class Datos_del_Pago:
    nombre_titular=""
    numero_tarjeta=int
    fecha_vencimiento=int
    DNI=int


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



