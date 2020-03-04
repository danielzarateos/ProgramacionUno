#-----------Mensajes-----------
MENSAJE_FALLO = "Fallaste"
PREGUNTA_NUMERO = "Intente adivinar mi numero favorito entre 1 y 10 \n:"
MENSAJE_ACIERTO = "Felicidades, adivinaste"
MENSAJE_MAYOR = "Es mayor."
MENSAJE_MENOR = "Es menor."
#-----------Variables----------
_numero = 0
#----------Constantes----------
import random
NUMERO_FAVORITO = random.randint(1,10)
#-----------Entradas-----------
#-----------Codigo-------------
_numero = int(input(PREGUNTA_NUMERO))
while ( _numero != NUMERO_FAVORITO ) :
    print(MENSAJE_FALLO)
    if _numero < NUMERO_FAVORITO :
        print(MENSAJE_MAYOR)
    else :
        print(MENSAJE_MENOR)
    _numero = int(input(PREGUNTA_NUMERO))
print(MENSAJE_ACIERTO)