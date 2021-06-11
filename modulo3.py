# -*- coding: utf-8 -*-

def buscar_elementos_iguales_seguidos(lista: list)->int:
    
    pos = -1
    
    for i in range(len(lista) - 1):
        if lista[i] == lista[i + 1]:
            pos = i
            break
    return pos

def contar_apariciones(lista: list, sublista:list)->int:
    
    n = 0
    
    for i in range(len(lista) - len(sublista) + 1):
        if lista[i:i + len(sublista)] == sublista:
            n += 1
    return n