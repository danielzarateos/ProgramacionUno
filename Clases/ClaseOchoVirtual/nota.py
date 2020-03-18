class Persona ():
    def __init__(self,nombre, talla, sexualidad, peso, edad):
        self.raza = "ser humano"
        self.name = nombre
        self.size = talla
        self.gender = sexualidad
        self.weight = peso
        self.age = edad
        print ("Hola a todos soy un", self.raza, "Mi nombre es", self.name)
    def mostrar_atributos(self) :
        print("Mi nombre es", self.name)
        print("Mi edad es", self.age)
        print("Mi estatura es", self.size)
        print("Mi genero es", self.gender)
        print("Mi peso es", self.weight)
        print("Mi edad es", self.age)
    
    def caminar(self, cantidad_pasos) :
        for i in range (cantidad_pasos) :
            print ("he caminado", cantidad_pasos + 1 ,"pasos")

ser_humano_1 = Persona("Daniel", 1.82, "Masculino", "83 Kg", 26)
ser_humano_2 = Persona("Andres", 1.75, "Masculino", "67 Kg", 20)

ser_humano_1.mostrar_atributos()
ser_humano_2.mostrar_atributos()

ser_humano_1.caminar(100)