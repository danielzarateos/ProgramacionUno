#----------Importar--------
import random   
#----------Mensajes--------
MENSAJE_NO = "La suma es"
MENSAJE_SI = "La suma no es 12"
#----------Numeros---------
dado1 = random.randint(1,6)
dado2 = random.randint(1,6)
suma = dado1 + dado2
while (suma != 12) :
    print(MENSAJE_SI)
    dado1 = random.randint(1,6)
    dado2 = random.randint(1,6)
    suma = dado1 + dado2
print(MENSAJE_NO , suma)