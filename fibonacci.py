# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 13:55:39 2021

@author: alejo
"""

def sucesion_fibonacci(cantidad_numeros: int) -> str:
    
    fibonacci_list = []
    contador = 1
    a = 0
    b = 1
    
    if cantidad_numeros == 0 or cantidad_numeros == 1:
        fibonacci_list.append(a)
    elif cantidad_numeros == 2:
        fibonacci_list.append(a)
        fibonacci_list.append(b)
    elif cantidad_numeros > 2:
        fibonacci_list.append(a)
        fibonacci_list.append(b)
        while contador < cantidad_numeros - 1:
            
            nuevo= fibonacci_list[contador] + fibonacci_list[contador - 1]
            fibonacci_list.append(nuevo)
            contador += 1

    x = str(fibonacci_list)
    y = x.replace("[", "")
    z = y.replace(" ", "")
    fibonacci = z.replace("]", "")
    return fibonacci

