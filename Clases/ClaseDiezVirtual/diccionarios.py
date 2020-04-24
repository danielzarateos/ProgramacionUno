#Forma de crear diccionarios
diccionario = {}
medios_transporte = {}
medios_transporte["carros"] = ["bmw","audi","mazda","mercedes benz"]
medios_transporte["motos"] = ["bmw","ducati","benelli","aprilia"]
print(medios_transporte["motos"])

print("#"*60)
print("los elementos que componen la llave de carros son : {}".format(medios_transporte["carros"]))

print("#"*60)
print("los elementos que componen la llave de motos son : {}".format(medios_transporte["motos"]))

print("#"*60)
#Otra forma de crear diccionarios
estudiantes_programacion = {
    "Nombres" : ["Daniel", "Valeria", "Santiago", "Juanes", "Ysabella", "David", "Marco", "Maria C", "Maria C", "Mafe", "Santiago", "Elena"],
    "Edad" : [19,18,20,18,17,19,20,22,24,21,19,22]
}

print(estudiantes_programacion["Nombres"])
print("#"*60)
print(medios_transporte.keys())
print(estudiantes_programacion.keys())
print("#"*60)
print(list(medios_transporte.keys()))
print("#"*60)
print(medios_transporte.values())
valores = list(medios_transporte.values())
#PRIMER CONJUNTO DE VALORES
print("#"*60)
print(valores[0])
print("#"*60)
print(valores[1])

#Otra forma de crear diccionarios

diccionario = {}
diccionario["Estudiantes"]=["Meli","Vale","Cathe"]
diccionario["Profesores"]=["Braiam","Diego"]
diccionario["aulas"]=["A202","A206"]
print("#"*60)
print(diccionario)
print("#"*60)
print(list(diccionario.keys()))
print("#"*60)
print(list(diccionario.values()))
print("#"*60)
print(diccionario)
print("#"*60)
print(diccionario["Profesores"])
print("#"*60)
#Diccionario de diccionarios
materiales = {}
materiales["oro"]=["18k","16k"]
materiales["marcadores"]=["pelikan","paper maker"]
print(type(materiales))
print("#"*60)
diccionario["Elementos"]=materiales
print(diccionario["Elementos"]["marcadores"])
print("#"*60)

#operando
notas = {}
notas ["QUIZ1"] = [5,4,5,3,3,5,4,2]
notas ["QUIZ2"] = [5,4,5,3,3,5,4,2]
notas ["PARCIAL"] = [5,4,5,3,3,5,4,2]
notas ["TALLERES"] = [5,4,5,3,3,5,4,2]
estudiantes_programacion["notas"] = notas
print(estudiantes_programacion)
print("#"*60)
print(estudiantes_programacion["notas"]["QUIZ1"])
print("#"*60)

#Generar copia sin afectar el contenido
diccionario_copia = diccionario.copy()
print(diccionario_copia)
print("#"*60)
#limpiar un diccionario
diccionario_copia.clear()
print(diccionario_copia)
print("#"*60)
#crear diccionarios con llaves cuyo valor inicial sera el mismo para todos 
keys = ["idiomas","carreras"]
values = ["soy un valor generico"]
created_dic= dict.fromkeys(keys,values)
print(created_dic)
print("#"*60)
#crearlo sin valor inicial
created_dic= dict.fromkeys(keys)
print(created_dic)
print("#"*60)
#obtener la informacion directamente de otra manera en una lista
print(estudiantes_programacion.get("Nombres"))
print("#"*60)

#eliminar un componente de un diccionario
diccionario_copy = diccionario.copy()
diccionario_copy.pop("Profesores")
print(diccionario_copy)
print("#"*60)
#Elimina la ultima llave agregada
diccionario_copy.popitem()
print(diccionario_copy)
print("#"*60)
#Agregar una llave o si existe sobre escribe su valor
diccionario_copy.setdefault("Computadoras",["Apple","Lenovo","Dell"])
print(diccionario_copy)
print("#"*60)
print(diccionario_copy.setdefault("Computadoras",["Apple","Dell","Lenovo","IBM"])
print("#"*60)
print(diccionario_copy)