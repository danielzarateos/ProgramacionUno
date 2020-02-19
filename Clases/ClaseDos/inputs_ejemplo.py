#Para no tener que escribir mil veces la pregunta
#---------------Mensajes----------------------
PREGUNTA_NOMBRE = "ingrese su nombre \n:"
MENSAJE_ANTES_NOMBRE = "Hola"
MENSAJE_DESPUESS_NOMBRE = "bienvenido a este programa"
PREGUNTA_EDAD = "ingrese su edad \n: "
MENSAJE_EDAD ="Su edad es"
PREGUNTA_ESTATURA = "ingrese su estatura \n: "
MENSAJE_ESTATURA = "Su estatura es"
#---------------------------------------------
#---------------Codigo-------------------------
#Mostrar la pregunta
_nombrePersona = input(PREGUNTA_NOMBRE)
#Dar el nombre y un mensaje
print(MENSAJE_ANTES_NOMBRE,_nombrePersona,MENSAJE_DESPUESS_NOMBRE)
#Mostrar de que tipo es el nombre
print(type(_nombrePersona))
#Se inlcute int o float antes del input para darle un tipo distinto a str
_edadPersona = int(input(PREGUNTA_EDAD))
print(MENSAJE_EDAD,_edadPersona)
print(type(_edadPersona))
_estaturaPersona = float(input(PREGUNTA_ESTATURA))
print(MENSAJE_ESTATURA,_estaturaPersona)
print(type(_estaturaPersona))
