#matplotlib.pyplot es lo de los graficos
import matplotlib.pyplot as plt
import pandas as p 

personas = {
  "Nombres" : ["Pepito","Zacarias","Julio","Popeye","Maria"],
  "Pesos" : [72,45,87,124,56]
}
#Como graficar cantidades vs pesos
#tiene que tener la misma cantidad de datos 

print(personas["Nombres"])
print(personas["Pesos"])
#crear
plt.bar(personas["Nombres"],personas["Pesos"],color = "b", alpha=0.5)
#titulo
plt.title("Peso de pacientes")
#Titulos x y y  
plt.xlabel("Nombres")
plt.ylabel("Pesos en kilos")
#Salvar
plt.savefig("pesos.png")
#mostrar
plt.close()

#crear pero de lado
plt.barh(personas["Nombres"],personas["Pesos"],color = "g", alpha=0.5)
#titulo
plt.title("Peso de pacientes")
#Titulos x y y  
plt.xlabel("Nombres")
plt.ylabel("Pesos en kilos")
#si esta cortando algo 
figure = plt.gcf()
figure.set_size_inches(9,9)
#Salvar
plt.savefig("pesos_delado.png")
#mostrar
plt.close()


barrios = p.read_csv("barrios.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
print(barrios)
plt.title("Barrios vs Habitantes", fontsize=20)
plt.bar(barrios["Barrio"].values(),barrios["Habitantes"].values(),align="center")
plt.xlabel("BARRIOS")
plt.ylabel("HABITANTES")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Barrios.png")
plt.close()
#plt.show()


