import matplotlib.pyplot as plt
import pandas as p 
#1.	Grafico de barras de elementos contra unidades
inventario = p.read_csv("inventario.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
plt.title("Elementos vs Unidades", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Unidades"].values(),color = "r", alpha=0.5,align="center")
plt.xlabel("Elemento")
plt.ylabel("Unidades")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Elementos_Unidades.png")
plt.close()

#2.	Grafico de barras de elementos contra viejos
plt.title("Elementos vs Elementos Viejos", fontsize=20)
plt.bar(inventario["Elemento"].values(),inventario["Viejo"].values(),color = "b", alpha=0.5, align="center")
plt.xlabel("Elemento")
plt.ylabel("Viejos")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Elementos_Viejos.png")
plt.close()

#3.	Grafico de barras de elementos contra nuevos
plt.bar(inventario["Elemento"].values(),inventario["Nuevos"].values(),color = "g", alpha=0.5)
plt.title("Elementos vs Elementos Nuevos")
plt.xlabel("Elementos")
plt.ylabel("Nuevos")
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Elementos_Nuevos.png")
plt.close()

#4. Leer PPG
ppg =p.read_csv("ppg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ppg["muestra"].values())
y = list(ppg["valor"].values())
plt.title("Lectura PPG")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("mi_ppg.png")
plt.close()
#Adicional picos
print("se ven picos")
#5. Mostrar pie 
labels = 'Hospitalizados', 'UCI', 'En casa'
sizes = [10, 5, 85]
explode = (0, 0.1, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Tratamiento diagnosticados")
plt.savefig("Pie_diagnosticados.png")
plt.close()