# -*- coding: utf-8 -*-

import modulo_analisis_covid as covidanal
import modulo_analisis_matriz as matrizanal

def test_buscar_fechas():

    archivo = "Casos_positivos_de_COVID-19_en_Colombia.csv"
    cargar = covidanal.cargar_datos_csv(archivo)
    llave_fecha = "Fecha de muerte"
    fecha_busqueda = ("2020", "04", "05")
    salida = covidanal.buscar_casos_por_fecha(cargar, llave_fecha, fecha_busqueda)

    assert(len(salida) == 8)

def test_columna_con_mas_ocurrencias():

    archivo = "datos.csv"
    cargar = matrizanal.cargar_matriz_de_csv(archivo)
    valor = 4
    salida = matrizanal.columna_con_mas_ocurrencias(cargar, valor)

    print(salida)
    assert(salida == 9)

test_buscar_fechas()
test_columna_con_mas_ocurrencias()