class Canguro():
    def __init__(self, especie, identificacion, edad, saltos):
        self.especie = "Canguro"
        self.identificacion = identificacion
        self.edad = edad
        self.saltos = saltos

class Cuidador():
    def __init__(self, identificacion, nombre, alimentados):
        self.nombre = nombre
        self.identificacion = identificacion
        self.alimentados = alimentados
    def alimentar(self, alimentados):
        self.alimentados = Cuidador.alimentados
        print("He alimentado", Cuidador.alimentados, "canguros")


class Jefe(Cuidador):
    def contratarCuidador(self, identificacion, nombre, alimentados):
        contratado = Cuidador(identificacion, nombre, alimentados)
        return contratado

cuidador1 = Jefe(421789, "Daniel", 33)
cuidador6 = cuidador1.contratarCuidador(748203, "Luisa", 0)
cuidador2 = Cuidador(231244, "Alejandra", 25)
cuidador3 = Cuidador(325985, "Miguel", 44)
cuidador4 = Cuidador(875093, "Yeison", 5)
cuidador5 = Cuidador(745394, "BadBunny", 66)

canguro1 = Canguro("Canguro",1, 10, 36453)
canguro2 = Canguro("Canguro",2, 5,5564)
canguro3 = Canguro("Canguro",3, 13, 42352)
canguro4 = Canguro("Canguro",4, 7, 23452)
canguro5 = Canguro("Canguro",5, 8, 45645)
canguro6 = Canguro("Canguro",6, 3, 7648)
canguro7 = Canguro("Canguro",7, 16, 4364563)
canguro8 = Canguro("Canguro",8, 1, 5345)
canguro10 = Canguro("Canguro",10, 4, 4534)

print("El canguro con identificacion", canguro1.identificacion, "ha dado", canguro1.saltos, "saltos")
print("El canguro con identificacion", canguro2.identificacion, "ha dado", canguro2.saltos, "saltos")
print("El canguro con identificacion", canguro3.identificacion, "ha dado", canguro3.saltos, "saltos")
print("El canguro con identificacion", canguro4.identificacion, "ha dado", canguro4.saltos, "saltos")
print("Mi nombre es", cuidador1.nombre, "soy el jefe y contrate a", cuidador6.nombre)
