# -*- coding: utf-8 -*-

def cargar_datos_csv(nombre_archivo:str)->list:
    
    lista_casos = []
    archivo = open(nombre_archivo, "r", encoding = "utf-8")
    
    print("Leyendo archivo: ", nombre_archivo,"\n\n")
    
    primera_linea = archivo.readline()
    titulos = primera_linea.split(",")
    titulos[-1] = titulos[-1].replace('\n','')
    
    print("Titulos de los campos: \n")
    print(titulos)
   
    linea = archivo.readline()

    print("\nInició lectura...")

    while len(linea) > 0:
        datos = linea.split(",")
        datos[-1] = datos[-1].replace('\n','')
        caso =  {}
        posicion = 0
        for titulo in titulos:
            dato = datos[posicion]
            if titulo.lower().startswith('fecha') or titulo == 'FIS':
                if titulo == 'FIS' and datos[posicion] == 'Asintomático':
                    dato = ()
                elif datos[posicion] == "-   -":
                    dato = None
                else:
                    fecha_texto = datos[posicion].replace("T00:00:00.000","")
                    (anio, mes, dia) = fecha_texto.split("-")
                    dato = (anio, mes, dia)
            caso[titulo] = dato
            posicion += 1

        lista_casos.append(caso)
        linea = archivo.readline()
    
    print("\nTerminó lectura")
    print("\nCantidad de casos cargados: ", len(lista_casos))
    print("\nPara ver un ejemplo de un caso escriba:", "casos_covid[0]")

    archivo.close()
    
    return lista_casos


def buscar_casos_por_fecha(casos_covid: list, llave_fecha:str, fecha_busqueda:tuple) -> list:
    
    lista_filtrada = []
    fechas_validas = (
            'Fecha de notificación', 
            'FIS', 
            'Fecha de muerte',
            'Fecha diagnostico',
            'Fecha recuperado',
            'fecha reporte web')
    
    if llave_fecha in fechas_validas:
        for caso in casos_covid:
            if caso[llave_fecha] == fecha_busqueda:
                lista_filtrada.append(caso)

    return lista_filtrada

    
def buscar_casos_por_campo_str(casos_covid:list, llave_campo:str, valor_busqueda:str) -> list:
    
    lista_filtrada = []
    campos_validos = ( 
                'ID de caso',
                'Codigo DIVIPOLA',
                'Ciudad de ubicación',
                'Departamento o Distrito ',
                'atención',
                'Edad',
                'Sexo',
                'Tipo',
                'Estado', 
                'País de procedencia')
    
    if llave_campo in campos_validos:
        for caso in casos_covid:
            if caso[llave_campo] == valor_busqueda:
                lista_filtrada.append(caso)
    
    return lista_filtrada

