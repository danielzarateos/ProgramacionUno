texto = "qui lorem ipsum quia dolor sit amet onsectetur adipisci velit"
#separe cada vez que haya una X letra (Q)
print(texto.split("q"))
#paso a ser lista
lista = ["hola","a","todos"]
#de lista a string + lo que haya en el "" es lo qe lo separa
string_lista = " ".join(lista)
print(string_lista)
#cambiar las q por las t (join + split)
print('t'.join(texto.split('q')))
#separar todas las palabras
lista_palabras_texto = texto.split()
print(lista_palabras_texto)
#palabra mas larga
print ( max (lista_palabras_texto,key=len))
#Esto retorna que a es más grande por el código ASCII
print(max("ZaWU"))
print(min("ZaWU"))
#volver la primera letra mayucula
txt_primera_mayuscula= texto.capitalize()
print(txt_primera_mayuscula)
#todo el texto en mayuscula
txt_mayuscula= texto.upper()
print(txt_mayuscula)
#ahora de mayuscula a minuscula
txt= "HOLA A TODOS"
print (txt.casefold())

#cantidad de caracteres a la izquierda que quiero mover un texto

txt= "Quiero ir en otro lugar"
print(txt.center(31))
#Verificar si termina en algo
parrafo = "hola cualquier cosa hola cualquier cosa  algo hola cualquier cosa."
print(parrafo.endswith("."))
#encontrar en que # de letra comienza cierta palabra
coordenada_inicio = parrafo.find("algo")
#lo mismo pero donde acaba 
cordenada_final = coordenada_inicio+ len("algo")+1
#¿de donde a donde va?
print(parrafo[coordenada_inicio:cordenada_final])

txt = "AAAA"
#¿son numeros?
print(txt.isnumeric())
#¿son alfa?
print(txt.isalpha())
#¿es ascii?
print(txt.isascii())
#¿se puede imprimir?
print(txt.isprintable())
#¿esta en mayucula?
print(txt.isupper())
"print(txt.is)"

#reemplazar algo por algo
txtx = "me gusta programar en Java"
print (txtx.replace("Java", "Python"))