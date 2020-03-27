#----Listas--------------------------------------------
pesosPacientesIniciales = [32,64,74,85,98,115,122,127,137,148]
presionesPacientes = []
for i in range (len(pesosPacientesIniciales)) :
    presionesPacientes.append(pesosPacientesIniciales[i] * 6)

#----Mensajes------------------------------------------
MENSAJE_SELECCION = "Seleccione entre \n 1. Ver pesos y presiones \n 2. Añadir pesos a la lista \n 3. Ver el paciente con la presion mas baja, mas alta, la lista de presiones organizada de mayor a menor, cantidad y cada cuanto se esta tomando una presion \n 4. Salir \n Ingrese su seleccion :"
#----Variables-----------------------------------------
_seleccion_usuario = int(input(MENSAJE_SELECCION))
#----Codigo--------------------------------------------
while ( _seleccion_usuario != 4 ) :
    if _seleccion_usuario == 1 :
        print("se muesta la presion en 𝑚𝑚/ℎ𝑔 abajo de cada peso \n", pesosPacientesIniciales, "\n", presionesPacientes )
    elif _seleccion_usuario == 2 : 
        _seleccion_usuario2 = str(input("¿Desea usted ingresar el peso de algun paciente ? (si o no) : "))
        while _seleccion_usuario2 == "si" :
            pesosPacientesIniciales.append(int(input("Ingrese el peso a adicionar : ")))
            presionesPacientes = []
            for i in range (len(pesosPacientesIniciales)) :
                presionesPacientes.append(pesosPacientesIniciales[i] * 6)
            _seleccion_usuario2 = str(input("¿Desea añadir otro peso? (si o no) : "))
        print("Nueva lista de pesos de pacientes : \n", pesosPacientesIniciales)
    elif _seleccion_usuario == 3 :
        presion_mas_alta = max(pesosPacientesIniciales) / 6
        presion_mas_baja = min(pesosPacientesIniciales) / 6
        print ("El paciente con la presion mas alta tiene", presion_mas_alta, "𝑚𝑚/ℎ𝑔")
        print ("El paciente con la presion mas baja tiene", presion_mas_baja, "𝑚𝑚/ℎ𝑔")
        pesosPacientesIniciales.sort(reverse=True)
        print ("lista ordenada decrecientemente {}".format(pesosPacientesIniciales))
        print("En total hay ", len(pesosPacientesIniciales), "pacientes")
        tiempo_entre_pacientes = 24 / len(pesosPacientesIniciales) 
        print("Se esta ingresando un paciente cada ", tiempo_entre_pacientes, "horas")
    else :
        print(MENSAJE_ERROR)
    _seleccion_usuario = int(input(MENSAJE_SELECCION))