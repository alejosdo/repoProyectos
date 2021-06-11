# -*- coding: utf-8 -*-
"""
Created on Mon May  3 20:13:42 2021

@author: alejo
"""

#import asistencia_congreso as con

def test_cargar_congreso():

    nombre = None
    archivo = "asistencia_congreso_v2.csv"
    
    resultado = con.cargar_datos(archivo)

    print(len(resultado))
    assert(len(resultado) == 177)
    
def test_analisar_asis():

    hombre = "DIAZ BURBANO JIMMY HAROLD"
    
    archivo = "asistencia_congreso_v2.csv"
    
    resultado = con.cargar_datos(archivo)
    
    resultado = con.analizar_asis(resultado)

    print(resultado)
    
def test_inasistencias():
    
    archivo = "asistencia_congreso_v2.csv"
    
    resultado = con.cargar_datos(archivo)
    
    resultado = con.mas_inasistencias(resultado)

    print(resultado)
    
def test_mas_asistencias():
    
    archivo = "asistencia_congreso_v2.csv"
    
    resultado = con.cargar_datos(archivo)
    
    resultado = con.mas_asistencias(resultado)

    print(resultado)
    
def test_mas_inasistencias_excusa():
    
    hombre = "ACOSTA INFANTE YESICA SUGEIN"
    
    archivo = "asistencia_congreso_v2.csv"
    
    resultado = con.cargar_datos(archivo)
    
    resultado = con.mas_inasistencias_excusa(resultado[hombre]["asistencia"])

    print(resultado)

def test_asistencias_partido():

    archivo = "asistencia_congreso_v2.csv"

    resultado = con.cargar_datos(archivo)

    resultado = con.asistencias_partido(resultado)

    print(resultado)
    assert(resultado["ALIANZA VERDE"] == 0.97)

def test_porcentaje_asistencias():

    archivo = "asistencia_congreso_v2.csv"

    resultado = con.cargar_datos(archivo)

    resultado = con.porcentaje_asistencias(resultado)

    print(resultado[0])

    assert(resultado[0]["porcentaje_asistencia"] == 0.96)

def test_mas_inasistencias():
    pass

def test_mas_X_inasistencias():

    archivo = "asistencia_congreso_v2.csv"

    resultado = con.cargar_datos(archivo)

    resultado = con.mas_X_inasistencias(resultado, 40)

    print(resultado)

    assert(resultado["ROJANO PALACIO KARINA ESTEFANIA"] == 48)

def test_mes_mayor_sesiones():

    archivo = "asistencia_congreso_v2.csv"

    resultado = con.cargar_datos(archivo)

    resultado = con.mes_mayor_sesiones(resultado)

    print(resultado)

    assert(resultado == "En el mes 08/2020 hubo 2565 sesiones")

def test_asistio_fecha():

    archivo = "asistencia_congreso_v2.csv"

    resultado = con.cargar_datos(archivo)

    resultado = con.asistio_fecha(resultado, "ALBAN URBANO LUIS ALBERTO", 20, 7, 2018)

    print(resultado)

    assert(resultado == True)

def test_asistencia_circunscripcion_fecha():

    archivo = "asistencia_congreso_v2.csv"

    resultado = con.cargar_datos(archivo)

    resultado = con.asistencia_circunscripcion_fecha(resultado, 3, 2019)

    print(resultado)

    assert(resultado["ANTIOQUIA"] == 52)

#test_cargar_congreso()
#test_analisar_asis()
#test_inasistencias()
#test_mas_asistencias()
#est_mas_inasistencias_excusa()
#test_asistencias_partido()
#test_porcentaje_asistencias()
#test_mas_inasistencias()
#test_mas_X_inasistencias()
#test_mes_mayor_sesiones()
#test_asistio_fecha()
#test_asistencia_circunscripcion_fecha()