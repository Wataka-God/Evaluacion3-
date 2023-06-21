

def grabarVehiculo():
    global patente, tipo, marca, fechaRegistro, precio, NombreDueño
    tipo = int(input("Ingrese el tipo del auto:  "))
    patente = int(input("Introduzca la patente:  "))
    marca = int(input("Introduzca la marca del auto: "))
    precio = int(input("Introduzca el precio del auto:  "))
    fechaRegistro = int(input(" Introduzca la fecha de registro del auto:  "))
    NombreDueño = input("Introduzca su nombre:  ")
    patenteverificador = patente
    precioauto = 5000000
    if patente == patenteverificador: 
        print("Esta es su patente ", patenteverificador)     
    elif precio > precioauto:
        print("el precio de su auto es de:  ", precio)
    else: 
        if precio < precioauto:
            print("El precio tiene que ser arriba de: ", precioauto)
    return

def buscarVehiculo(): 
    global patente, tipo, marca, fechaRegistro, precio, NombreDueño
    buscarAuto = int(input("Busque auto deseado por su patente:  "))
    if buscarAuto == patente:
        print("La patente es", patente)
        print("El tipo es:  ", tipo)
        print("la marca es:  ", marca)
        print("fecha de registro es: ", fechaRegistro)
        print("el precio es: ", precio)
        print("El dueño es: ", NombreDueño)
        return

def certificados():
    import numpy as fn 
    import random as rd
    matriz = fn.zeros((3,3))

    #print(matriz)

    for f in range(3):
        for c in range(3):
            matriz[f][c] = rd.randint(1500,3500)
    print(matriz)
    return

def salir():
    nombre = []
    print("!!!Hasta PRONTO¡¡¡¡")
    print("DANIEL OSEGA")
    print (" VERSION 3.11.3")




def Menu():
    miMatriz = [[0] * 6 for _ in range(7)]
    while True:
        print(" 1. Grabar \n 2. Buscar \n 3. imprimir Certificados \n 4. Salir ")
        opc = int(input("Su opcion es:  "))
        if opc == 1:
            grabarVehiculo()    
        elif opc == 2:
            buscarVehiculo()
        elif opc == 3:
            certificados()
        elif opc == 4:
            salir()
        else:
            print("OPCION NO ADECUADA")
Menu()            


        

    
