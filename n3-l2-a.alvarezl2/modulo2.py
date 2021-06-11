# -*- coding: utf-8 -*-

def es_palindroma(cadena: str)->bool:
    
    inicio = 0
    
    r = cadena.lower()
    
    r = r.replace(" ", "")
    
    resultado = True
    
    final = len(r) - 1
    
    while inicio != final:
        if r[inicio] == r[final]:
            inicio += 1
            final -= 1
        else :
            resultado = False
    return resultado

def letra_mas_comun(cadena: str)->str:
    
    cadena = cadena.lower()
    
    cadena = cadena.replace(" ", "")

    mayorl = ""
    
    mayorn = 0
    
    if cadena.isnumeric() == True:
        return mayorl

    for i in range(len(cadena)):
        r = cadena.count(cadena[i])
        if r > mayorn:
            mayorn = r
            mayorl = cadena[i]
    return mayorl
        

