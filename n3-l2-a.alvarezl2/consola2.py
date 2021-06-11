# -*- coding: utf-8 -*-

import modulo2 as mod

def ejecutar_es_palindroma()->None:
    print("Evaluador de cadenas palíndromas")
    cad = str(input("Por favor digite la cadena: "))
    es = mod.es_palindroma(cad)
    if es == True:
        print("La cadena ", cad, "sí es palíndroma")
    else:
        print("La cadena ", cad, "no es palíndroma")

def ejecutar_letra_mas_comun()->None:
    print("Buscando la letra más común")
    cad = str(input("Por favor ingrese la cadena: "))
    letra = mod.letra_mas_comun(cad)
    print("En la cadena ingresada, la letra ", letra, "es la letra más común")
          
def mostrar_menu()->None:
    print("\n\nOPCIONES")
    print("1. Palabra palíndroma")
    print("2. Letra más común")
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
    
    ejecutando = True
    """while ejecutando:
        ejecutando = mostrar_menu()
    if ejecutando:
        input("Presione cualquier tecla para continuar ... ")"""
    
    while ejecutando == True:
        mostrar_menu()
        usuario_dice = int(input("Ingrese una opción valida: "))
        if usuario_dice == 1:
            ejecutar_es_palindroma()
        elif usuario_dice == 2:
            ejecutar_letra_mas_comun()
        elif usuario_dice == 3:
            ejecutando = False
        else :
            print("Por favor ingrese una opción valida")

iniciar_aplicacion()