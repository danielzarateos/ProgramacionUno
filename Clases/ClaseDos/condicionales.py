#== igual, != diferente, > mayor, < menor
#-------------Mensajes-------------
HOLA = "Hola mundo que hace"
MUNDO = "mundo"
MENSAJE_A_IGUAL_B = "a es igual a b"
MENSAJE_A_MENOR_B = "a es menor a b"
MENSAJE_A_MAYOR_B = "a es mayor a b"
MENSAJE_A_DISTINTO_B = "a es distinyo a b"
#---------------------------------
_a = int(input("ingrese A:"))
_b = int(input("ingrese B:"))
print(MENSAJE_A_IGUAL_B,_a==_b,MENSAJE_A_MENOR_B, _b>_a,MENSAJE_A_MAYOR_B, _b<_a,MENSAJE_A_DISTINTO_B, _a != _b)
print(HOLA,MUNDO)
print(MUNDO in HOLA)
print(MUNDO not in HOLA)