# -*- coding: utf-8 -*-

import modulo3 as mod

def ejecutar_buscar_elementos_iguales_seguidos()->None:
    print("Teclee uno a uno los elementos de la lista. Cuando haya terminado digite *")
    car = ''
    mi_lista = []

    while car != "*":
        car = input ("Digite el número: ")
        if (car != "*"):
            valor = int(car)
            mi_lista.append(valor)
        
    print("La lista creada es: ", mi_lista)
    pos = mod.buscar_elementos_iguales_seguidos(mi_lista)
    if pos == -1:
        print("La lista no tiene elementos iguales seguidos")
    else:
        print("La posición de los primeros elementos consecutivos iguales es: ", pos)

def ejecutar_contar_apariciones()->None:
    print("Teclee uno a uno los elementos de la lista larga. Cuando haya terminado digite *")
    car=''
    mi_lista = []

    while car != "*":
        car = input ("Digite el número: ")
        if (car != "*"):
            valor = int(car)
            mi_lista.append(valor)
        
    print("La lista larga es: ", mi_lista)
        
    print("Ahora teclee uno a uno los elementos de la lista corta. Cuando haya terminado digite *")
    car = ''
    mi_lista_corta = []

    while car != "*":
        car = input ("Digite el número: ")
        if (car != "*"):
            valor = int(car)
            mi_lista_corta.append(valor)
    
    print("La lista corta es: ", mi_lista_corta)

    apariciones = mod.contar_apariciones(mi_lista, mi_lista_corta)
    if apariciones == 0:
        print("La lista corta no se encuentra en la lista larga")
    else:
        print("La lista corta aparece ", apariciones, " veces en la lista larga")
          

def mostrar_menu()->None:
    print("\n\nOPCIONES")
    print("1. Buscar elementos iguales seguidos")
    print("2. Contar apariciones")
    print("3. Salir")


def iniciar_aplicacion()->None:

    i = True
    
    while i == True:
        mostrar_menu()
        e = int(input("Seleccione 1, 2 o 3: "))
        if e == 1:
            ejecutar_buscar_elementos_iguales_seguidos()
        elif e == 2:
            ejecutar_contar_apariciones()
        elif e == 3:
            i = False
    
    return 
    
iniciar_aplicacion()