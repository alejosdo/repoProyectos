


# -*- coding: utf-8 -*-


def cargar_vuelos(ruta_archivo: str)->dict:
    
    vuelos = {}
    archivo = open(ruta_archivo)
    linea = archivo.readline()
    
    while len(linea) > 0:
        datos = linea.split(",")
        codigo_vuelo = datos[1]
        vuelo = {}
        vuelo["aerolinea"] = datos[0]
        vuelo["origen"] = datos[2]
        vuelo["destino"] = datos[3]
        vuelo["distancia"] = datos[4]
        vuelo["salida"] = datos[5]
        vuelo["duracion"] = int(datos[6])
        vuelo["retraso"] = float(datos[7].replace("\n", ""))
        vuelos[codigo_vuelo] = vuelo
        linea = archivo.readline()

    archivo.close()
    return vuelos

    
def vuelos_directos(vuelos: dict, origen: str, destino: str)->list:

    lista = []
    retorno = {}
    
    for vuelo in vuelos.keys():
        if origen == vuelos[vuelo]["origen"] and destino == vuelos[vuelo]["destino"]:
            retorno = {vuelo : vuelos[vuelo]}
            lista.append(retorno)
       
    return lista

def vuelos_con_una_escala(vuelos: dict, origen: str, destino: str)->list:

    lista = []
    escala_encontrada = []
    
    for vuelo in vuelos.keys():
        if origen == vuelos[vuelo]["origen"]:
            for escala in vuelo.keys():
                if vuelos[vuelo]["destino"] == vuelos[escala]["origen"] and vuelos[escala]["destino"] == destino:
                    escala_encontrada.append(vuelo)
                    escala_encontrada.append(escala)
                    lista.append(escala)
    return lista

def sugerir_aerolinea(vuelos: dict, origen: str, destino: str)->str:
    
    aerolinea = None
    i = 0
    
    for vuelo in vuelos.keys():
        if vuelos[vuelo]["origen"] == origen and vuelos[vuelo]["destino"] == destino:
            if i == 0:
                i = vuelos[vuelo]["retraso"]
                
            if vuelos[vuelo]["retraso"] <= i:
                aerolinea = vuelos[vuelo]["aerolinea"]
                
    return aerolinea