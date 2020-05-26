import sys
import matplotlib.pyplot as plt
import pandas as p
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
plt.savefig("mi_grafico.png")
plt.close()
plt.show  
####################################
nombre = (input('Ingrese su nombre :'))
estatura = float(input('Ingrese su estatura :'))
peso = float(input('Ingrese su peso :'))
"""def verificar_imc(nombre,estatura,peso):
  try:
    nombre_verificado = str(nombre)
  except ValueError:
    print ("ingresaste mal tu nombre")
    nombre = (input('Ingrese su nombre :'))
    verificar_imc(nombre,estatura,peso)
  try:
    estatura_verificada = float(estatura)

  except ValueError:
    print ("ingresaste mal tu estatura")
    estatura = (input('Ingrese su estatura :'))
    verificar_imc(nombre,estatura,peso)
  try:
    peso_verificado = float(peso)
  except ValueError:
    print ("ingresaste mal tu peso")
    peso = (input('Ingrese su peso :'))
    verificar_imc(nombre,estatura,peso)
  imc = (peso_verificado) / (estatura_verificada*estatura_verificada)"""""
imc = peso / (estatura*estatura)
print(nombre.capitalize(),"tu imc es de",imc)

"""""""verificar_imc(nombre,estatura,peso)"""

#############################################
kilos_arroz = float(input("Ingrese cuantos kilos tiene de arroz :")) 
kilos_lenteja = float(input("Ingrese cuantos kilos tiene de lenteja :"))  
kilos_frijoles = float(input("Ingrese cuantos kilos tiene de frijoles :")) 
kilos_papa = float(input("Ingrese cuantos kilos tiene de papa :")) 
diccionario = {
  "Cosas" : ["Arroz","Lentejas","Frijoles","Papa"],
  "Cantidad" : [kilos_arroz,kilos_lenteja,kilos_frijoles,kilos_papa]
}


plt.title("Kilos vs Producto", fontsize=20)
plt.bar(diccionario["Cosas"],diccionario["Cantidad"],align="center")
plt.xlabel("Kilogramos")
plt.ylabel("Producto")
plt.xticks(rotation=90)
figure = plt.gcf()
figure.set_size_inches(12,18)
plt.savefig("Productos .png")
plt.close()
#plt.show()
###############################################
texto = input("Cuentanos, ¿como te has sentido?, termina por favor lo que nos cuentes con un punto:")
def sentimientos(texto):
  if texto.endswith(".") == True :
    print("Gracias por darnos tu opinion")
  else :
    print("Por favor vuelve a intentarlo, recuerda que tu texto debe terminar con un punto. ")
    texto = input("Cuentanos, ¿como te has sentido?, termina por favor lo que nos cuentes con un punto: ")
    sentimientos(texto)
sentimientos(texto)
#############################################
#Se ha notado los siguiente respecto a las compras en una tienda el 12% compra leche, el 8% huevo, el 4% Vino, el 26% arroz, 30% Queso y 20% salchichas mostrar esta información en un gráfico de pie resaltando el queso.
labels = 'Leche', 'Huevo', 'Vino', 'Arroz',"Queso","Salchichas"
sizes = [12, 8, 4, 26, 30,20]
explode = (0, 0, 0, 0, 0.1, 0) 
plt.pie(sizes, explode=explode, labels=labels, shadow=False, startangle=0)
plt.title("Porcentajes de compra")
plt.savefig("Grafico_pie.png")
plt.show()
print("Recuerda buscar grafico_pie.png para que veas el grafico de pie de los productos")