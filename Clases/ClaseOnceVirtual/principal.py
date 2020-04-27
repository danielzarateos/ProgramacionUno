#El archivo balance.csv cuenta con una información ficticia referente al estado de cuentas de una ciudad empleando la libreria pandas y segun lo visto en clase  proceder a resolver las siguientes preguntas:

#1.Cual es la ciudad con el nombre más largo?
#2.Cual es la ciudad con el nombre más corto?
#3.Cual fue el mayor monto de ganancias? 
#4.Cual fue el mayor monto de perdidas? 
diccionario = pd.read_csv("balance.csv",encoding="UTF-8",header = 0,delimiter=";").to_dict()
#1.
nombre_mas_largo = max(diccionario["Ciudad"].values(), key=len)
#2.
nombre_mas_corto = min(diccionario["Ciudad"].values(), key=len)
#3.
mayor_ganancias = max(diccionario["Ganancias"].values())
#4.
mayor_perdidas = max(diccionario["Perdidas"].values())

print("La ciudad con el nombre mas largo es {} \n La ciudad con el nombre mas corto es {} \n La ciudad con mas ganancias es {} \n La ciudad con mas perdidas es {}".format(nombre_mas_largo,nombre_mas_corto,mayor_ganancias,mayor_perdidas))