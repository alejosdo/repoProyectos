# -*- coding: utf-8 -*-

def maximo_comun_divisor(n1: int, n2: int)-> int:
    
    max_com_div = 1
    
    contador = 2
    
    if n1 < n2:
        menor = n1
        mayor = n2
        
    else :
        menor = n1
        mayor = n2
        
    while contador <= menor:
        if mayor % contador == 0 and menor % contador == 0:
            max_com_div = contador
        contador += 1
        
    return max_com_div

def jugar_PUM(jugadores: int, numero: int)-> None:

    print('Jugador\t\tJugada')
    
    a = 1
    
    b = 1
    
    if numero < 10:
        while b < 501:
            if b % numero == 0:
                print(f'{a}\t\tPUM')
            else :
                print(f'{a}\t\t{b}')
            if a == jugadores:
                a = 1
            else :
                a += 1
            b += 1
    else:
        print('Numero no válido.')