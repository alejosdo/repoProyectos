# -*- coding: utf-8 -*-
"""
Modulo de logica que permite generar una matriz aleatoria 
de numeros enteros entre 0 y 10, en un archivo csv
"""


import random

def crear_matriz_nula(filas:int, columnas:int) -> list:

    M = []
    for i in range (0, filas):
        M.append([0] * columnas)
    
    return M


def crear_matriz_aleatoria(filas:int, columnas:int) -> list:
    """
    Crea una matriz aleatoria de datos enteros
    Parámetros:
        filas (int): Cantidad de filas para crear la matriz aleatoria
        columnas (int): Cantidad de columnas para crear la matriz aleatoria
    Retorna:
        list: Lista de listas, que representa la matriz aleatoria
    """
    
    M = crear_matriz_nula(filas, columnas)
    
    # Recorre una dimension
    for i in range(0,filas):
        # Recorre otra dimension
        for j in range(0,columnas):
            M[i][j] = random.randint(0,10)
    return M


def exportar_matriz_a_csv(M:list, nombre_archivo:str)-> None:
    """
    Crea un archivo csv apartir de los datos de una matriz numerica
    Cada fila de la matriz, se convierte en una linea en el archivo csv
    Cada columna de la matriz, en un dato de una linea separado por coma
    Parámetros:
        M (list): Matriz con numeros a exportar. 
    Retorna:
        None: No retorna nada, imprime en un archivo datos.csv la matriz recibida por parametro
    """
    archivo = open(nombre_archivo, "w")
    
    for i in range(0,len(M)):
        datos = []
        for j in range(0,len(M[0])):
            datos.append(str(M[i][j]))
        
        linea_datos = ",".join(datos)
        archivo.write(linea_datos + "\n")
    
    archivo.close()

# Programa principal
    
# Pedimos la dimensión de la matriz
print("---Programa Generador de matriz aleatoria ----")
m = int(input("Digite el número de filas: "))
n = int(input("Digite el número de columnas: "))

print("\nGenerando matriz...")
matriz = crear_matriz_aleatoria(m,n)
print("\nMatriz generada")

print("\nExportando matriz a csv...")
exportar_matriz_a_csv(matriz, "datos.csv")
print("\nMatriz exportada datos.csv")

