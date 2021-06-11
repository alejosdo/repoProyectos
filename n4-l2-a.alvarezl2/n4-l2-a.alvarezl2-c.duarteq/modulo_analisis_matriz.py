# -*- coding: utf-8 -*-

def cargar_matriz_de_csv(nombre_archivo:str) -> list:
    
    archivo = open(nombre_archivo, "r")
    
    M = []
    
    for linea in archivo:
        datos_linea = linea.replace('\n', '')
        datos_linea = datos_linea.split(";")
        datos_enteros = []
        for dato in datos_linea:
            entero = int(dato)
            datos_enteros.append(entero)
        
        M.append(datos_enteros)  
    
    archivo.close()
    
    return M


def dar_estadisticas_matriz(M:list)-> tuple:

    conteo_0 = 0
    conteo_10 = 0
    suma_valores = 0
    promedio_valores = 0
    total = 0

    for conjunto in M:
        for dato in conjunto:
            total += 1
            suma_valores += dato
            if dato == 0:
                conteo_0 += 1
            if dato == 10:
                conteo_10 += 1

    promedio_valores = suma_valores / total
    tupla = (conteo_0, conteo_10, suma_valores, promedio_valores)

    return tupla


def contar_ocurrencias_por_columna (M:list, columna:int, valor:int) -> int:

    entero = 0
    fila = 0

    while fila < len(M):
        if M[fila][columna] == valor:
            entero += 1
        fila += 1
    
    return entero
    
    
def columna_con_mas_ocurrencias (M:list, valor:int) -> int:

    contador = 0
    columna = 0
    cebo = 0

    while contador < len(M[0]):
        fila = 0
        ocurrencia = 0
        while fila < len(M):
            if M[fila][contador] == valor:
                ocurrencia += 1
            fila += 1
        if ocurrencia > cebo:
            cebo = ocurrencia
            columna = contador
        contador += 1
    
    return columna


M = cargar_matriz_de_csv("datos.csv")


