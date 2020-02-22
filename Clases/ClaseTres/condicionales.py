#-----------------Recordar----------
# antes de las entradas siempre va _xxxx
# formato de IF -> 
#if (x x x) :
#   if not then  
#elif
#
#   else
#
#
# OR es para o a o b
# una sola tiene que ser verdadera
# AND es para a y b
# ambas tienen que ser verdaderas
# 
#------------Mensajes--------------
PREGUNTA_NOMBRE = "Ingrese su nombre \n"
PREGUNTA_EDAD = "Ingrese porfavoshito su edad \n"
MENSAJE_DE_BIENVENIDA = "Bienvenido"
MENSAJE_TOCAYOS = "Hola hermano somos tocayos"
MENSAJE_DESPEDIDA = "Adios"
MENSAJE_JOVEN = "Usted es joven"
MENSAJE_ADULTO = "Usted es adulto"
MENSAJE_VIEJO = "Usted es viejo"
MENSAJE_EDAD_MALA = "Usted ingreso una edad menor a cero o mayor a 300"
#----------------------------------
#-------------No variables---------
NOMBRE_PERSONAL = "Daniel"
#----------------------------------
#-------------Entradas-------------
_nombreUsuario = " "
_edadUsuario = 0
#----------------------------------
#-------------Codigo---------------
print(MENSAJE_DE_BIENVENIDA)
_nombreUsuario = input(PREGUNTA_NOMBRE)
if (_nombreUsuario == NOMBRE_PERSONAL) :
    print(MENSAJE_TOCAYOS)
_edadUsuario = int(input(PREGUNTA_EDAD))
if (_edadUsuario >= 0) and (_edadUsuario <= 25) :
    print(MENSAJE_JOVEN)
elif (_edadUsuario > 25) and (_edadUsuario <= 65) :
    print(MENSAJE_ADULTO)
else :
    print(MENSAJE_VIEJO)
print(MENSAJE_DESPEDIDA)