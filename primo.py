# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 09:31:13 2021

@author: alejo
"""

def es_primo(numero: int)->bool:

    i = 2
    
    while numero / i != 1:
        if numero % i == 0:
            return False
        i += 1
    return True

    