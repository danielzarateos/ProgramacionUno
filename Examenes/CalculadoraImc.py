#-------Instrucciones-----------
#Pedir el peso, la estatura, calcular imc y decir en que estado esta
#--------Mensajes---------------
PREGUNTA_NOMBRE = " Bienvenido, ingresa tu nombre por favor \n: "
PREGUNTA_MASA = " ingresa tu masa "
PREGUNTA_ESTATURA = " ingresa tu estatura "
MENSAJE_PREVIO_IMC = " Su imc es de  "
MENSAJE_INSUFICIENTE = " indica que esta en insuficiencia "
MENSAJE_NORMAL = " indica que esta bien "
MENSAJE_SOBREPESO = " indica que esta en sobrepeso "
MENSAJE_OBESO = " indica que esta obeso "
MENSAJE_ERROR = " Alguno de los datos fue ingresado erroneamente "
MENSAJE_DESPEDIDA = " Gracias por usar la calculadora de imc"


#--------No Variables-----------
INSUFICIENTE = 18.4
NORMAL = 24.9
SOBREPESO = 29.9
OBESO = 30
#IMC = (_pesoUsuario/_estaturaUsuario**2)
#--------Entradas---------------
_nombreUsuario = ""
_pesoUsuario = 0
_estaturaUsuario = 0
#--------Codigo-----------------
_nombreUsuario = input(PREGUNTA_NOMBRE)
_estaturaUsuario = float(input(PREGUNTA_ESTATURA))
_pesoUsuario = float(input(PREGUNTA_MASA))
IMC = (_pesoUsuario/_estaturaUsuario**2)
print(MENSAJE_PREVIO_IMC, IMC,)
if (IMC >= 0) and (IMC <= INSUFICIENTE) :
    print(MENSAJE_INSUFICIENTE)
elif (IMC > INSUFICIENTE) and (IMC <= NORMAL) :
    print(MENSAJE_NORMAL)
elif (IMC > NORMAL) and (IMC <= SOBREPESO) :
    print(MENSAJE_SOBREPESO)
elif (IMC > SOBREPESO) and (IMC <= 1000) :
    print(MENSAJE_OBESO)
else :
    print(MENSAJE_ERROR)
print(MENSAJE_DESPEDIDA)