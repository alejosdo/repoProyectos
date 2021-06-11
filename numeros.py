# -*- coding: utf-8 -*-
"""
Created on Sun Apr 25 14:43:10 2021

@author: alejo
"""

def sumar_valores_pares(numeros: list) -> int:
    
    i = 0
    
    for n in numeros:
        if n % 2 == 0:
            i += n
    
    return i

def sumar_pares(numeros: list) -> int:
    
    suma = 0
    i = 0
        
    while i < len(numeros):
        c = numeros[i]
        if i % 2 == 0:
            suma += c
        i += 1
            
    return suma

def clasificar_ciudades(ciudades: list, minimo: int) -> dict:
    
    if ciudades == []:
        return None
    
    resultado = {"viables" : [], "inviables": []}
    
    for ciudad in ciudades:
        if ciudad["poblacion"] >= minimo:
            resultado["viables"].append(ciudad)
        else:
            resultado["inviables"].append(ciudad)
            
    return resultado 
