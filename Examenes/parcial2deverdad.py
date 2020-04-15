#En una universidad deseamos crear un nuevo curso y para ello necesitamos de sus servicios.
#Para nosotros es vital saber de nuestros estudiantes su nombre, edad, genero, colegio del que
#se graduó. También nos interesa mucho ingresar un profesor por materia del cual nos importa
#su nombre, edad y nivel educativo.

#(Valor 1.0) Se le pide hacer una clase de estudiante que tenga sus atributos, tambien que
#tenga una función que le permita asistir a clases, esta función solo mostrará a cuantas clases
#asistió el día de hoy y tendrá de entrada la cantidad de clases.
class Estudiantes ():
    def __init__(self,nombre_ingresado,edad_ingresada,genero_ingresado,colegio_ingresado):
        self.nombre = nombre_ingresado
        self.edad = edad_ingresada
        self.genero = genero_ingresado
        self.colegio = colegio_ingresado
    def asistir_a_clase(self,cantidad_clases_asistidas):
        print("Hola a todos soy {} y fui a {} clases".format(self.nombre,cantidad_clases_asistidas))

#(Valor 1.0) También debemos crear una clase profesor que tenga sus atributos y que tenga
#un función que sea dictar clases también tendrá una entrada de cuantas clases dará y se
#mostrará en pantalla cuatas dio.
class Profesores ():
    def __init__(self,nombre_ingresado,edad_ingresada,nivel_educativo_ingresado):
        self.nombre = nombre_ingresado
        self.edad = edad_ingresada
        self.nivel = nivel_educativo_ingresado
    def dictar_clase(self,cantidad_clases_dictadas):
        print("Hola a todos soy {} y dicte {} clases".format(self.nombre,cantidad_clases_dictadas))

#(Valor 1.0) A su vez los profesores se pueden especializar y volverse Directores, estos
#directores nos permiten contratar profesores y mantienen sus funciones habituales.
class Directores(Profesores):
    def contratar (self,nombre,edad,nivel):
        profesor = Profesores(nombre,edad,nivel)
        print("Hola a todos soy {} y acabo de contratar a un profe, tiene {} años y un {}".format(self.nombre,edad,nivel))
        return profesor
#(Valor 1.0) Crear 5 alumnos, 2 profesores y un Director. Cada uno debe ejecutar una función
#como mínimo. El director contratará dos profesores más. Mostrar en pantalla los resultados
estudiante1 = Estudiantes("Andres",16,"masculino","San jose de las Vegas")
estudiante1.asistir_a_clase(4)

estudiante2 = Estudiantes("Ana",15,"femenino","Santa Maria del Rosario")
estudiante2.asistir_a_clase(5)

estudiante3 = Estudiantes("Daniel",16,"masculino","San Ignacio")
estudiante3.asistir_a_clase(2)

estudiante4 = Estudiantes("Luisa",13,"femenino","Colombo britanico")
estudiante4.asistir_a_clase(4)

estudiante5 = Estudiantes("Esteban",14,"masculino","San Jose de la Salle")
estudiante5.asistir_a_clase(8)

profesor1= Profesores("Daniel",26,"Master")
profesor1.dictar_clase(5)

profesor2= Profesores("Miguel",37,"Pregrado")
profesor2.dictar_clase(2)

director1= Directores("Carolina",37,"Phd")
director1.contratar("Carolina",33,"Master")
director1.contratar("Diego",35,"PhD")

#(Valor 1.0) Crear un menu con las siguientes opciones
#1. Mostrar los atributos de los estudiantes s
#2. Mostrar los atributos de los profesores
#3. Mostrar los atributos del director
#4. Salir
print("-------------MENU-------------")
MENSAJE_SELECCION = "¿Que deseas hacer? \n 1. Ver estudiantes y datos \n 2. Ver profesores y datos \n 3. Ver los datos de la directora \n 4. Salir \n Ingrese su seleccion :"
MENSAJE_ERROR = "No es una opcion, intente otra vez"
_seleccion_usuario = int(input(MENSAJE_SELECCION))
while ( _seleccion_usuario != 4 ) :
    if _seleccion_usuario == 1 :
        print("Nombre :",estudiante1.nombre,"-Edad :",estudiante1.edad,"-Colegio del que salio :",estudiante1.colegio, "\n",
              "Nombre :",estudiante2.nombre,"-Edad :",estudiante2.edad,"-Colegio del que salio :",estudiante2.colegio, "\n",
              "Nombre :",estudiante3.nombre,"-Edad :",estudiante3.edad,"-Colegio del que salio :",estudiante3.colegio, "\n",
              "Nombre :",estudiante4.nombre,"-Edad :",estudiante4.edad,"-Colegio del que salio :",estudiante4.colegio, "\n",
              "Nombre :",estudiante5.nombre,"-Edad :",estudiante5.edad,"-Colegio del que salio :",estudiante5.colegio, "\n" )
    elif _seleccion_usuario == 2 : 
        print("Nombre :",profesor1.nombre,"-Edad :",profesor1.edad,"-Nivel educativo :",profesor1.nivel, "\n",
              "Nombre :",profesor2.nombre,"-Edad :",profesor2.edad,"-Nivel educativo :",profesor2.nivel, "\n")
    elif _seleccion_usuario == 3 :
        print("Nombre :",director1.nombre,"-Edad :",director1.edad,"-Nivel educativo :",director1.nivel, "\n")
    else :
        print(MENSAJE_ERROR)
    _seleccion_usuario = int(input(MENSAJE_SELECCION))