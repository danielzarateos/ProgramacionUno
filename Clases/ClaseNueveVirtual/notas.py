def hablar (mensaje ):
    print(mensaje)
    return "Exitoso"

def validar_clave(CLAVE_REAL, _claveIngresada):
    STATE = "Por definir"
    if CLAVE_REAL == _claveIngresada :
        print("Ingreso exitoso")
        STATE = "Clave valida"
    else :
        print("Clave incorrecta")
        STATE = "Clave invalida"

    return STATE

def mostrar_dos_listas(lista_1, lista_2):
    if (len(lista_1) == len(lista_2)):
        print("elemento", "precio")
        for i in range (len(lista_1)):
            print(lista_1[i],lista_2[i])
    else :
        print("No se pueden mostrar uno a uno")

def bienvenida(): print ("Bienvenido al codigo")
bienvenida()

def mostrar_lista(lista):
    contador = 1
    for elemento in lista :
        print(contador, "-",elemento)
        contador += 1



intentos = 0
estado = validar_clave(1234, int(input("Ingrese la clave : ")))
while (estado != "Clave valida" and intentos < 3) :
    estado = validar_clave(1234, int(input("Ingrese la clave : ")))
    intentos += 1

#hablar("Hola como estan")
#if hablar("hola a todos") == ("Exitoso") :
#    print("El mensaje se mostro con exito")

comidas = ["carne", "pollo", "huevo", "queso"]
mostrar_lista(comidas)

precios = [9100, 8000, 10000, 4800]
mostrar_dos_listas(comidas,precios)