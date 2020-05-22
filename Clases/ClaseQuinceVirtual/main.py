import sys
#Se establece desde el principio el error 
edad = "No ingresaste edad"
#Probar o intentar
try:
    #Pedir edad
    edad = int (input('Ingrese su edad :'))
    #Si no es un int de lleve a la siguiente excepcion (se le pone el tipo de error)
except ValueError:
    print ("ingresaste mal la edad")
    #ahora con archivos
try :
    archivo = open ("Soy_un_archivo_que_no_existe.txt")
    #si no existe
except FileNotFoundError :
    print("Ingresaste un archivo que no existe")
#probar si es el sistema operativo
def os_validate(so):
    assert(so in sys.platform)
    print ("Estas en el sistema operativo", so)

try :
    os_validate('linux')
except AssertionError:
    print("Hola no eres linux")

try:
    os_validate('darwin')
except AssertionError:
    print("no eres mac")

def validador_parrafo(parrafo):
    assert(parrafo.endswith("."))
    return False
validador = True

while (validador):
    parrafo =  input('ingrese un parrafo debe finalizar con .')
    try:
        validador = validador_parrafo(parrafo)
    except AssertionError:
        print("Entrada no válida")
