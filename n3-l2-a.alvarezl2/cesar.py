# -*- coding: utf-8 -*-
"""
Created on Sun Apr 18 14:12:29 2021

@author: alejo
"""

def trad_valor(crcr: str, corrimiento: int)->str:

    a = 0
    
    z = 0

    numero_codigo = ord(crcr)
    
    if numero_codigo >= 65 and numero_codigo <= 90:
        a = 65
        z = 90
        
    elif numero_codigo >= 97 and numero_codigo <= 122:
        a = 97
        z = 122
        
    else: 
        return crcr
    
    if numero_codigo < (a + corrimiento - 1):
        resultado = z + numero_codigo - a - corrimiento + 1
    else:
        resultado = numero_codigo - corrimiento
    
    resultado =  chr(resultado)
    
    return resultado            

def descifrar_codigo_cesar(texto_cifrado: str, corregimiento: int) -> str:
    
    resultado = ""
    
    for character in texto_cifrado:
        resultado += trad_valor(character, corregimiento)

    return resultado
            
            
    
    