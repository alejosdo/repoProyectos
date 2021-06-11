# -*- coding: utf-8 -*-

def cargar_tablero_goles(ruta_archivo: str)->list:

    archivo = open(ruta_archivo)
    dimensiones = archivo.readline().split(",")
    filas = int(dimensiones[0])
    columnas = filas
    tablero = []

    for i in range(0, filas):
        tablero.append([0] * columnas)

    linea = archivo.readline()
    i = 0

    while len(linea) > 0:
        datos = linea.split(",")
        for j in range(0, columnas):
            tablero[i][j] = int(datos[j])
        i += 1 
        linea = archivo.readline()

    archivo.close()
    return tablero


def cargar_equipos(ruta_archivo: str)->dict:

    archivo = open(ruta_archivo)
    equipos = {}
    linea = archivo.readline()
    while len(linea) > 0:
        datos = linea.split(",")
        equipos[datos[0]] = int(datos[1])
        linea = archivo.readline()

    archivo.close()
    return equipos


def anotar_marcador(tablero_goles: list, equipos:dict, equipo1:str, equipo2: str, marcador:str)->list:

    posEquipo1 = int(equipos.get(equipo1))
    posEquipo2 = int(equipos.get(equipo2))
    marcador = marcador.split("-")
    tablero_goles[posEquipo1][posEquipo2] = int(marcador[0])
    tablero_goles[posEquipo2][posEquipo1] = int(marcador[1])

    return tablero_goles


def asignar_equipo(equipos: dict, num: int) -> str:

    team = ""

    for numero in equipos:
        if num == numero:
            team = equipos.keys()

    return team


def total_goles(tablero_goles: list)->int:

    total = 0

    for fila in tablero_goles:
        for gol in fila:
            if gol != -1 and gol != -2:
                total += gol

    return total


def partidos_jugados(tablero_goles: list)->int:

    partidos = 0

    return partidos

def equipo_mas_goleador(tablero_goles: list, equipos:dict)->str:

    goleador = ""
    goles = 0
    fila = 0
    columna = 0

    while fila > len(tablero_goles):
        for marcador in tablero_goles[fila][columna]:
            if -1 != marcador and marcador != -2:
                goles += marcador
                goleador = equipos[equipo]
            columna += 1
        fila += 1
        for marcador in tablero_goles:
            if marcador > goles:
                goles = marcador
                

    return goleador

def equipo_mas_goleado(tablero_goles: list, equipos:dict)->str:
    """
    Esta función retorna el nombre del equipo al cual le han marcado más goles en el
    campeonato
    Parámetros:
        tablero_goles (list): matriz que contiene el tablero de goles
        equipos (dict): diccionario de los equipos del campeonato
    Retorno: str
        El nombre del equipo más goleado del campeonato
    """
    return "Ninguno"


def partidos_empatados(tablero_goles: list)->int:
    """
    Esta función calcula el total de partidos que se han quedado empatados en el campeonato
    Parámetros:
        tablero_goles (list): matriz que contiene el tablero de goles
    Retorno: int
        El total de partidos empatados en el campeonato
    """
    return 0

def mayor_numero_goles(tablero_goles: list)->int:
    """
    Esta función calcula el mayor número de goles marcados en un partido del campeonato 
    (sumando los goles de los dos equipos)

    Parámetros:
        tablero_goles (list): matriz que contiene el tablero de goles
    Retorno: int
        El mayor número de goles marcados en un partido del campeonato
    """
    return 0