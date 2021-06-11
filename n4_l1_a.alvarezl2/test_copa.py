# -*- coding: utf-8 -*-

import modulo_copa_colombia as copa

def test_asignar_equipo():

    archivo = "equipos.csv"
    salida = 5
    resultado = copa.cargar_equipos(archivo)
    resultado = copa.asignar_equipo(resultado, salida)

    print(resultado)
    assert(resultado == "Dep. Pereira")