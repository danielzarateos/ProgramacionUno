#Se cuenta con una lista de edades iniciales de unos pacientes igual a :
listaEdadesIniciales = [1,2,4,8,16,32,64]
#Se le pide que cree una lista de edad de pacientes que ingresan el día de hoy al hospital mediante preguntar al usuario del programa las edades de los nuevos pacientes, el usuario determinará cuando a agregado todos.
listaEdadesHoy = []
_seleccion_usuario2 = str(input("¿Desea usted ingresar la edad de algun usuario que haya ingresado hoy? (si o no) : "))
while _seleccion_usuario == "si" :
    listaEdadesHoy.append(int(input("Ingrese la edad a adicionar : ")))
    _seleccion_usuario = str(input("¿Desea añadir otra edad? (si o no) : "))
#Despues de esto se le pide que muestre la lista de las edades ingresadas por los pacientes en el día de hoy.
print("Las edades de los pacientes de hoy es : ", listaEdadesHoy)
#Luego que muestra la lista de las edades de los  pacientes totales (inicial+la del día)
listaEdadesIniciales.extend(listaEdadesHoy)
print("Las edades de los pacientes totales son :", listaEdadesIniciales)
#Cual es la edad promedio?
suma_listaTotal = sum(listaEdadesIniciales) 
Longitud_listaTotal = int(len(listaEdadesIniciales))
print("El promedio es de :", suma_listaTotal/ Longitud_listaTotal)
#Cual es la edad del paciente más longevo?
print ("El paciente mas longevo en la lista {} tiene {}"
.format(listaEdadesIniciales,max (listaEdadesIniciales))) 
#Cual es la edad del paciente más joven? 
print ("El paciente mas joven en la lista {} tiene {}"
.format(listaEdadesIniciales,min (listaEdadesIniciales))) 
#Muestre la lista en orden creciente
#Muestre la lista en orden decreciente
#creciente
listaEdadesIniciales.sort()
print ("lista ordenada creciente {}".format(listaEdadesIniciales))
#decreciente
listaEdadesIniciales.sort(reverse=True)
print ("lista ordenada decrecientemente {}".format(listaEdadesIniciales))
#Al final del día llega un paciente y por error un auxiliar en la salud inserta una edad en la posición 4 igual a 87 años, muestre como quedaría la lista después de este error
listaEdadesIniciales.insert(3,87)
print ("Despues del error la lista se ve asi : ", listaEdadesIniciales)
#Luego se enteran que el paciente en la posición 6 se fue. Como queda la lista de edades? 
listaEdadesIniciales.pop(7)
print(listaEdadesIniciales)
