#-----------No variables-----------
TEMPERATURA_HIPOTERMIA = 36
TEMPERATURA_SALUDABLE = 38.4
TEMPERATURA_ALERTA = 40
PAIS_OBSERVACION_1 = "China"
PAIS_OBSERVACION_2 = "Italia"
PAIS_OBSERVACION_3 = "Iran"
#-------------Mensajes-------------
MENSAJE_TEMPERATURA = "Por favor ingrese la temperatura del usuario \n :"
MENSAJE_PAIS_ORIGEN = "Por favor ingrese el pais del que viene (primera letra en mayuscula y sin tildes) \n :"
MENSAJE_NEGATIVA = "El usuario parece estar muerto o el sensor malo, verifique."
MENSAJE_HIPOTERMIA = "El usuario esta en estado de hipotermia."
MENSAJE_SALUDABLE = "El usuario esta en estado saludable."
MENSAJE_ALERTA = "El usuario esta en estado de alerta."
MENSAJE_PELIGRO = "El usuario esta en estado de peligro."
MENSAJE_OBSERVACION = "El usuario esta en estado de observacion."
#-------------Entradas-------------
_paisOrigenUsuario = ""
_temperaturaUsuario = 0
#------------Codigo----------------
_paisOrigenUsuario = input(MENSAJE_PAIS_ORIGEN)
if _paisOrigenUsuario == PAIS_OBSERVACION_1 or _paisOrigenUsuario == PAIS_OBSERVACION_2 or _paisOrigenUsuario == PAIS_OBSERVACION_3 :
    print(MENSAJE_OBSERVACION)
else : 
    _temperaturaUsuario = float(input(MENSAJE_TEMPERATURA))
    if _temperaturaUsuario > 0 and _temperaturaUsuario < TEMPERATURA_HIPOTERMIA :
        print(MENSAJE_HIPOTERMIA)
    if _temperaturaUsuario >= TEMPERATURA_HIPOTERMIA and _temperaturaUsuario <= TEMPERATURA_SALUDABLE :
        print(MENSAJE_SALUDABLE)
    if _temperaturaUsuario > TEMPERATURA_SALUDABLE and _temperaturaUsuario < TEMPERATURA_ALERTA :
        print(MENSAJE_ALERTA)
    if  _temperaturaUsuario >= TEMPERATURA_ALERTA :
        print(MENSAJE_PELIGRO)
    elif _temperaturaUsuario < 0 :
        print(MENSAJE_NEGATIVA)
