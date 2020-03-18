#Trabajo, hacer un menu con 5 instrucciones
#1. Se pregunta su edad y si es mayor de 18 se le permitira ingresar
#si es mayor a 30 se le mostrara "tiene descuento de 30%"
#si es mayor a 60 se le mostrara "tiene descuento de su edad%"
#menor no ingresa

#2. Ingresar una lista de productos a comprar, al final debo mostrar cuales compro y si desea añadir algo

#3. mostrar la lista de compras cosa por cosa

#4. Eliminar cosas de la lista

#5. Salir

#------------Preguntas-------------
_PREGUNTA_EDAD = "Por favor ingresa tu edad : "
_PREGUNTA_ANADIR = "Ingresa los productos que quieras comprar, para parar de añadir porfavor escribe -nada- "
_PREGUNTA_ELIMINAR = "Que elementos (numero en la lista) quieres eliminar de tu lista de compras \n :"
#------------Mensajes--------------
MENSAJE_SELECCION = "Seleccione para \n 1. Ingresar su edad \n 2. Ingresar cosas a su carrito \n 3. Mostrar lista detallada \n 4. Eliminar cosas de su lista \n 5. Salir \n Ingrese su seleccion :"
MENSAJE_MENOR = "Usted no puede ingresar"
MENSAJE_MAYOR = "Usted puede ingresar! bienvenido"
MENSAJE_TREINTA = "ademas, tiene un descuento de 30 % "
MENSAJE_SESENTA = "ademas, tiene un descuento de "
#----------------------------------
#------------Inputs----------------
#----------------------------------
#------------Variables-------------
#----------------------------------
#------------NoVariables-----------
#----------------------------------
#------------Codigo----------------
_seleccion_usuario = int(input(MENSAJE_SELECCION))
while ( _seleccion_usuario != 5 ) :
    if _seleccion_usuario == 1 :
        edad = int(input(_PREGUNTA_EDAD))
        if edad < 18 :
            print(MENSAJE_MENOR)
        elif edad >= 18 and edad <30 :
            print(MENSAJE_MAYOR)
        elif edad >= 30 and edad < 60 :
            print(MENSAJE_MAYOR, MENSAJE_TREINTA)
        elif edad >= 60 :
            print(MENSAJE_MAYOR, MENSAJE_SESENTA, edad, "%")
    elif _seleccion_usuario == 2 : 
        compras = []
        anadir = input ("Desea ingresar compras si -> si, no -> no \n : ")
        while anadir=="si" :
            compras.append(input("Ingrese que quiere agregar : "))
            anadir = input ("Desea ingresar mas compas s -> si, n -> no \n :")
    elif _seleccion_usuario == 3 :
        print(compras)
    elif _seleccion_usuario == 4 :
        eliminar = int(input(_PREGUNTA_ELIMINAR))
        compras.pop(eliminar - 1)
    else :
        print(MENSAJE_ERROR)
    _seleccion_usuario = int(input(MENSAJE_SELECCION))