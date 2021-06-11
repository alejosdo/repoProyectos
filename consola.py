# -*- coding: utf-8 -*-

import modulo as mod

def ejecutar_maximo_comun_divisor()->None:
    print("Buscando el máximo común divisor entre dos números")
    numero1 = int(input("Por favor digite el primer número: "))
    numero2 = int(input("Por favor digite el segundo número: "))
    mcd = mod.maximo_comun_divisor(numero1, numero2)
    print("El máximo común divisor de ", numero1, " y ",numero2, "es: ", mcd)

def ejecutar_PUM()->None:
    print("Vamos a jugar al PUM")
    n = int(input("Por favor digite la cantidad de jugadores: "))
    x = int(input("Por favor digite el número escogido para el PUM: "))
    mod.jugar_PUM(n, x)

def mostrar_menu()->None:
    print("1. Encontrar máximo común divisor")
    print("2. Jugar PUM")
    print("3. Salir")

def iniciar_aplicacion()->None:
    """
    Esta función mantiene el programa funcionando hasta que el usuario seleccione la opción para salir.
    La función primero debe mostrar el menú de opciones usando la función mostrar_menu().
    A continuación, debe solicitarle al usuario una opción.
    Según lo que haya seleccionado el usuario, debe llamar a una de las funciones cuyo nombre inicia con ejecutar_
    Si el usuario seleccionó la opción de Salir, la función debe terminar su ejecución para que el programa pueda terminar.
    Si el usuario seleccionó cualquier otra opción, después de ejecutar la opción seleccionada se debe volver
    a mostrar el menú de opciones y se debe repetir el proceso.
    """
    i = True
    
    while i == True:
        mostrar_menu()
        e = int(input("Seleccione 1, 2 o 3: "))
        if e == 1:
            ejecutar_maximo_comun_divisor()
        elif e == 2:
            ejecutar_PUM()
        elif e == 3:
            i == False

iniciar_aplicacion()