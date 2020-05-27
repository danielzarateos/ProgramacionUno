import sys
import matplotlib.pyplot as plt
import pandas as p
#1.Abrir archivo dicho por el usuario y graficarlo
def abrir_archivo(archivo):
  assert(archivo)
  return False 
archivo_existe = True 

while(archivo_existe):
  archivo = input("Ingresa el nombre del archivo que deseas graficar: ")
  try :
    archivo_existe = open(archivo)
    archivo_existe = False
  except FileNotFoundError :
    print("Ingresaste un archivo que no existe")

graficar = p.read_csv(archivo,encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(graficar["muestra"].values())
y = list(graficar["valor"].values())
plt.title(input("Ingresa el nombre del grafico:"))
plt.xlabel(input("Ingresa el nombre del eje x:"))
plt.ylabel(str(input("Ingresa el nombre del eje y:")))
plt.plot(x,y)
plt.savefig("Profe_muchas_gracias.png")
plt.close()
plt.show  
#2. Imc
def datos_imc():
    try:
        nombre = (input('Ingrese su nombre :'))
        estatura = float(input('Ingrese su estatura :'))
        peso = float(input('Ingrese su peso :'))
    except ValueError:
        print("Alguno de los datos que pusiste esta en el formato equivocado")
        datos_imc()
    lista = [nombre,estatura,peso]
    return lista
variable = datos_imc()
imc = variable[2]/variable[1]**2
print(variable[0].capitalize(),"tu imc es de",imc)

#3. graficar los 3 archivos y unas barras que comparen los picos
ecg =p.read_csv("ecg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title("ECG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("Mi_ecg.png")
plt.close()
eeg =p.read_csv("eeg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title("EEG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("Mi_eeg.png")
plt.close()
ppg =p.read_csv("ppg.csv",encoding='UTF-8',header=0, delimiter=";").to_dict()
x= list(ecg["muestra"].values())
y = list(ecg["valor"].values())
plt.title("PPG-uV")
plt.xlabel("Tiempo(ms)")
plt.ylabel("Volataje(uV)")
plt.plot(x,y)
plt.savefig("Mi_ppg.png")
plt.close()
diccionario_picos = {
    "Cosa" : ["ecg","eeg", "ppg"],
    "Picos" : [9,9,9]
}
plt.title("-----grama vs Picos", fontsize=20)
plt.bar(diccionario_picos["Cosa"],diccionario_picos["Picos"],align="center")
plt.xlabel("------grama")
plt.ylabel("Picos")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Por_Picos .png")
plt.close()
#plt.show()
#4. pie donde mas haya estado en casa
labels = "Habitacion", "Cocina", "Sala","En la calle","Baño","Sacando a bruno"
sizes = [45, 15, 5, 15, 5, 15]
explode = (0.1, 0, 0, 0, 0, 0) 
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Porcentajes de casa")
plt.savefig("Todo_Grafico_casa.png")
plt.show()
#5. diferencias entre aprendizaje supervisado y no supervisado
#El aprendizaje supervisado puede ser tal ves mas riguroso, pero el no supervizado permite a quienes aprendemos distinto mejorar (en lo que nos gusta) y tal vez deja caer un poco mas las materias que tal vez no se comprenden tan bien










