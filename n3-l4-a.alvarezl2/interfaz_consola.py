1# -*- coding: utf-8 -*-

import libreria_vuelos as lib_vuelos

def ejecutar_cargar_vuelos()->dict:
    archivo = input("Por favor ingrese el nombre del archivo de vuelos que quiere cargar: ")
    vuelos = lib_vuelos.cargar_vuelos(archivo)
    return vuelos

def ejecutar_vuelos_directos(vuelos: dict)->None:
    
    origen = input("Por favor indique el codigo del aeropuerto origen del trayecto: ")
    destino = input("Por favor indique el código del aeropuerto destino del trayecto: ")
    vuelos_directos = lib_vuelos.vuelos_directos(vuelos, origen, destino)
    if len(vuelos_directos) == 0:
        print("No se encontró ningún vuelo directo para el trayecto indicado entre", origen, "y", destino)
    else:
        print("Los vuelos directos entre ", origen, "y", destino, "son:", vuelos_directos)

def ejecutar_vuelos_con_una_escala(vuelos: dict)->None:
    
    origen = input("Por favor indique el codigo del aeropuerto origen del trayecto: ")
    destino = input("Por favor indique el código del aeropuerto destino del trayecto: ")
    vuelos_escala = lib_vuelos.vuelos_con_una_escala(vuelos, origen, destino)
    if len(vuelos_escala) == 0:
        print("No se encontró ningún vuelo con una escala para el trayecto indicado entre", origen, "y", destino)
    else:
        print("Los vuelos con una escala entre ", origen, "y", destino, "son:", vuelos_escala)

def ejecutar_sugerir_aerolinea(vuelos: dict)->None:
    
    origen = input("Por favor indique el codigo del aeropuerto origen del trayecto: ")
    destino = input("Por favor indique el código del aeropuerto destino del trayecto: ")
    sugerencia = lib_vuelos.sugerir_aerolinea(vuelos, origen, destino)
    if sugerencia == None:
        print("No se encontró ninguna aerolínea para el trayecto indicado entre", origen, "y", destino)
    else:
        print("La aerolínea sugerida para viajar entre", origen, "y", destino, "es", sugerencia)

def mostrar_menu()->None:
    print("\n\nOPCIONES")
    print("1. Cargar vuelos")
    print("2. Buscar vuelos directos")
    print("3. Buscar vuelos con una escala")
    print("4. Sugerir aerolínea")
    print("5. Salir")

def iniciar_aplicacion()->None:
    
    continuar = True
    vuelos = dict()
    while continuar:
        mostrar_menu()
        opcion = int(input("Por favor seleccione una opción del menú: "))
        if opcion == 1:
            vuelos = ejecutar_cargar_vuelos()
        elif opcion == 2:
            ejecutar_vuelos_directos(vuelos)
        elif opcion == 3:
            ejecutar_vuelos_con_una_escala(vuelos)
        elif opcion == 4:
            ejecutar_sugerir_aerolinea(vuelos)
        elif opcion == 5:
            continuar = False
        else:
            print("Por favor seleccione una de las opciones del menú.")

iniciar_aplicacion()


