#def leer_archivo(nombre_archivo):
#    archivo_en_memoria = open(nombre_archivo,"r", encoding = "UTF-8")
#    lineas_archivo = archivo_en_memoria.read().splitlines()
#    archivo_en_memoria.close()
#    return lineas_archivo

#print(leer_archivo("estudiantes.csv"))

import pandas as pd
#Primera entrada nombre de archiv0
#Segunda el encoding
#Tercera el header
#Cuarto lo que separa
#.to_dict() lo hace un diccionario
diccionario = pd.read_csv("estudiantes.csv",encoding="UTF-8",header = 0,delimiter=";").to_dict()
print(diccionario)
print(diccionario.keys())
print(diccionario["Nombre"])

#Por el nombre mas largo
mayor_nombre = max(diccionario["Nombre"].values)
print(mayor_nombre)
#Por el valor ( con letras )
mayor_nombre = max(diccionario["Nombre"].values(), key=len)
menor_nombre = min(diccionario["Nombre"].values(), key=len)

print("El estudiante con el nombre mas largo es {} y el que tiene el nombre mas corto es {}".format(mayor_nombre,menor_nombre))

#Por la edad mas grande y mas pequeña
mayor_edad = max(diccionario["Edad"].values())
menor_edad = min(diccionario["Edad"].values())
print(mayor_edad)
print(menor_edad)
#Notas
nota_mayor_parcial2 = max(diccionario["Parcial2"].values())
print(nota_mayor_parcial2)

nota_menor_parcial2 = min(diccionario["Parcial2"].values())
print(nota_menor_parcial2)
