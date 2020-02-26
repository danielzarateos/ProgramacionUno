#----------No Variables----------
RIESGO_BAJO = 1000
RIESGO_MEDIO = 5000
#----------Mensajes--------------
MENSAJE_PACIENTES = "Ingrese la cantidad de pacientes \n :"
MENSAJE_PACIENTES_UCI = "Ingrese la cantidad de pacientes en UCI \n :"
MENSAJE_RIESGO_ALTO = "Su hospital tiene un riesgo de operacion alto."
MENSAJE_RIESGO_BAJO = "Su hospital tiene un riesgo de operacion bajo."
MENSAJE_RIESGO_MEDIO = "Su hospital tiene un riesgo de operacion medio."
MENSAJE_ERROR = "Datos erroneos, verifique."
#----------Entradas--------------
_cantidadPacientes = 0
_cantidadPacientesUCI = 0
#----------Codigo----------------
_cantidadPacientes = int(input(MENSAJE_PACIENTES))
#_cantidadPacientesUCI = int(input(MENSAJE_PACIENTES_UCI))
if _cantidadPacientes > 0 and _cantidadPacientes <= RIESGO_BAJO :
    print(MENSAJE_RIESGO_BAJO)

elif _cantidadPacientes >0 and _cantidadPacientes <= RIESGO_MEDIO :
    _cantidadPacientesUCI = int(input(MENSAJE_PACIENTES_UCI))
    if _cantidadPacientesUCI >= RIESGO_BAJO :
        print(MENSAJE_RIESGO_ALTO)
    else :
        print(MENSAJE_RIESGO_BAJO)
elif _cantidadPacientes >= RIESGO_MEDIO :
    print(MENSAJE_RIESGO_ALTO)
else :
    print(MENSAJE_ERROR)