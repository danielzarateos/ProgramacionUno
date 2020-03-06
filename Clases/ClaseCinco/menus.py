#Hacer menu que cuando la persona ingrese 1, 2, 3 ó 4 diga
#si 1, mostrar nombre
#si 2, mostrar edad
#si 3, mostrar notas
#si 4, salir 
#siempre mostrar el menu
#otro numero es invalido 
#-----------Mensajes-------------
MENSAJE_SELECCION = "Seleccione entre ver \n 1. Nombres \n 2. Edades \n 3. Notas \n 4. Salir \n Ingrese su seleccion :"
MENSAJE_SALIDA = "Salida exitosa."
MENSAJE_ERROR = "No es una opcion valida, ingrese un valor valido"
#-----------Listas----------------
lista_opciones = [1,2,3,4]
lista_nombres = ["Juanes", "Marco", "Santiago", "Leslly", "Camila", "Camila", "Ysabella", "Elena", "Santiago", "Maria", "Susana", "David", "Daniel", "Daniel"]
lista_edades = [16, 19, 20, 19, 19, 19, 19 , 19, 19, 19, 20, 22, 19, 26]
lista_notas = [3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2, 4,3]
_seleccion_usuario = int(input(MENSAJE_SELECCION))
while ( _seleccion_usuario != 4 ) :
    if _seleccion_usuario == 1 :
        print(lista_nombres)
    elif _seleccion_usuario == 2 : 
        print(lista_edades)
    elif _seleccion_usuario == 3 :
        print(lista_notas)
    else :
        print(MENSAJE_ERROR)
    _seleccion_usuario = int(input(MENSAJE_SELECCION))