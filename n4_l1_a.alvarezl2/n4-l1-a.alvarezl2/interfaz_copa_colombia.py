# -*- coding: utf-8 -*-

import modulo_copa_colombia as mod

def ejecutar_cargar_equipos()->dict:
    archivo = input("Por favor ingrese el nombre del archivo con la lista de equipos que desea cargar: ")
    equipos = mod.cargar_equipos(archivo)
    print(equipos)
    return equipos


def ejecutar_cargar_tablero_goles()->list:
    archivo = input("Por favor ingrese el nombre del archivo con el tablero de goles que desea cargar: ")
    tablero = mod.cargar_tablero_goles(archivo)
    print(tablero)
    return tablero


def imprimir_tablero_goles(tablero_goles:list, equipos:dict)->None:
    print("{0:>17}".format(" "),end='')
    for equipo in equipos.keys():
        print("{0:>17}".format(equipo),end='')
    print()
    
    i = 0

    for equipo in equipos:
        print("{0:>17}".format(equipo),end='')
        for j in range(0, len(tablero_goles[0])):
            if (tablero_goles[i][j] == -1):
                print("{0:>17}".format("x"),end='')
            elif (tablero_goles[i][j] == -2):
                print("{0:>17}".format("-"),end='')
            else:
                print("{0:>17}".format(str(tablero_goles[i][j])),end='')
        print()
        i+=1


def ejecutar_anotar_marcador(tablero_goles:list, equipos:dict)->list:
    equipo1 = input("Teclee el nombre del equipo 1: ")
    equipo2 = input("Teclee el nombre del equipo 2: ")
    marcador = input("Teclee el marcador en formato goles1-goles2: ")
    tablero_goles = mod.anotar_marcador(tablero_goles,equipos,equipo1,equipo2,marcador)
    return tablero_goles


def ejecutar_total_goles(tablero_goles:list)->None:
    total_goles = mod.total_goles(tablero_goles)
    print("El total de goles marcados en el campeonato son: ",total_goles)


def ejecutar_partidos_jugados(tablero_goles:list)->None:
    total_partidos = mod.partidos_jugados(tablero_goles)
    print("El total de partidos que se han jugado en el campeonato son: ",total_partidos)


def ejecutar_equipo_mas_goleador(tablero_goles:list, equipos:dict)->None:
    equipo_mas_goleador = mod.equipo_mas_goleador(tablero_goles,equipos)
    print("El equipo m??s goleador es: ", equipo_mas_goleador)


def ejecutar_equipo_mas_goleado(tablero_goles:list, equipos:dict)->None:
    equipo_mas_goleado = mod.equipo_mas_goleado(tablero_goles, equipos)
    print("El equipo m??s goleado es: ", equipo_mas_goleado)


def ejecutar_partidos_empatados(tablero_goles:list)->None:
    partidos_empatados = mod.partidos_empatados(tablero_goles)
    print("El total de partidos empatados en el campeonato son: ",partidos_empatados)


def ejecutar_mayor_numero_goles(tablero_goles:list)->None:
    mayor_numero = mod.ejecutar_mayor_numero_goles(tablero_goles)
    print("El mayor n??mero de goles marcados en un partido es: ",mayor_numero)

    
def mostrar_menu()->None:
    print("\n\nOPCIONES")
    print("1. Cargar equipos")
    print("2. Cargar tablero goles")
    print("3. Imprimir tablero goles")
    print("4. Anotar marcador")
    print("5. Total de goles")
    print("6. Partidos jugados")
    print("7. Equipo m??s goleador")
    print("8. Equipo m??s goleado")
    print("9. Partidos empatados")
    print("10. Mayor n??mero de goles")
    print("11. Salir")


def iniciar_aplicacion()->None:
    """
    Esta funci??n mantiene el programa funcionando hasta que el usuario seleccione la opci??n para salir.
    La funci??n primero debe mostrar el men?? de opciones usando la funci??n mostrar_menu().
    A continuaci??n, debe solicitarle al usuario una opci??n.
    Seg??n lo que haya seleccionado el usuario, debe llamar a una de las funciones cuyo nombre inicia con ejecutar_
    Si el usuario seleccion?? la opci??n de Salir, la funci??n debe terminar su ejecuci??n para que el programa pueda terminar.
    Si el usuario seleccion?? cualquier otra opci??n, despu??s de ejecutar la opci??n seleccionada se debe volver
    a mostrar el men?? de opciones y se debe repetir el proceso.
    """

    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    print("BIENVENIDO A LA APP COPA COLOMBIA 2019")
    print("-----------------------------------------------------------------------")
    print("-----------------------------------------------------------------------")
    continuar = True
    tablero_goles = []
    equipos = {}
    while continuar:
        mostrar_menu()
        opcion = int(input("Por favor seleccione una opci??n del men??: "))
        if opcion == 1:
            equipos = ejecutar_cargar_equipos()
        elif opcion == 2:
            tablero_goles = ejecutar_cargar_tablero_goles()
        elif opcion == 3:
            imprimir_tablero_goles(tablero_goles, equipos)
        elif opcion == 4:
            tablero_goles = ejecutar_anotar_marcador(tablero_goles, equipos)
        elif opcion == 5:
            ejecutar_total_goles(tablero_goles)
        elif opcion == 6:
            ejecutar_partidos_jugados(tablero_goles)
        elif opcion == 7:
            ejecutar_equipo_mas_goleador(tablero_goles, equipos)
        elif opcion == 8:
            ejecutar_equipo_mas_goleado(tablero_goles, equipos)
        elif opcion == 9:
            ejecutar_partidos_empatados(tablero_goles)
        elif opcion == 10:
            ejecutar_mayor_numero_goles(tablero_goles)
        elif opcion == 11:
            continuar = False
        else:
            print("Por favor seleccione una de las opciones del men??.")



iniciar_aplicacion()