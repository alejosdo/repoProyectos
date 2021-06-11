# -*- coding: utf-8 -*-


def cargar_datos(informacion: str) -> list:

    archivo = open(informacion, "r", encoding="utf-8")
    linea = archivo.readline()
    linea = archivo.readline()
    lista_congresistas = []

    while len(linea) > 0:
        datos = linea.split(",")
        nombre = datos[0]
        movimiento = datos[1]
        circunscripcion = datos[2]
        fecha = datos[3]
        dato_asistencia = datos[4].replace("\n", "")
        congresista_encontrado = encontrar_congresista(lista_congresistas, nombre)

        if congresista_encontrado is None:
            congresista = {}
            asistencia = {}
            congresista["nombre"] = nombre
            congresista["movimiento"] = movimiento
            congresista["circunscripcion"] = circunscripcion
            asistencia[fecha] = dato_asistencia
            congresista["asistencia"] = asistencia
            lista_congresistas.append(congresista)
        else:
            asistencia = congresista_encontrado["asistencia"]
            asistencia[fecha] = dato_asistencia
            congresista_encontrado["asistencia"] = asistencia

        linea = archivo.readline()

    archivo.close()

    return lista_congresistas


def encontrar_congresista(lista_congresistas: list, nombre: str) -> dict:
    for cong_actual in lista_congresistas:
        if cong_actual["nombre"] == nombre:
            return cong_actual


def analizar_asis(informacion: dict) -> dict:

    salida = {"asistio": 0, "ex_medica": 0, "otra_excusa": 0, "silla_vacia": 0, "sin_excusa": 0, "suspension": 0,
              "sesiones": 0}

    for i in informacion.keys():
        if informacion[i] == "ASISTIÓ":
            salida["asistio"] += 1
        if informacion[i] == "EX. MÉDICA":
            salida["ex_medica"] += 1
        if informacion[i] == "OTRA EXCUSA":
            salida["otra_excusa"] += 1
        if informacion[i] == "SILLA VACÍA":
            salida["silla_vacia"] += 1
        if informacion[i] == "SIN EXCUSA":
            salida["sin_excusa"] += 1
        if informacion[i] == "SUSPENSIÓN":
            salida["suspension"] += 1
        salida["sesiones"] += 1

    return salida


def mas_inasistencias(informacion: list) -> str:
    nombre = None
    numero_de_fallas = 0

    for i in informacion:
        asistencia = i["asistencia"]
        ejecucion = analizar_asis(asistencia)
        if ejecucion["sin_excusa"] > numero_de_fallas:
            numero_de_fallas = ejecucion["sin_excusa"]
            nombre = i["nombre"]

    return "El congresista " + nombre + " faltó " + str(numero_de_fallas) + " veces a sesiones de forma injustificada"


def mas_asistencias(informacion: list) -> str:

    nombre = None
    asistencias = 0

    for i in informacion:
        asistencia = i["asistencia"]
        ejecucion = analizar_asis(asistencia)
        if ejecucion["asistio"] > asistencias:
            asistencias = ejecucion["asistio"]
            nombre = i["nombre"]

    return "El congresista " + nombre + " asistió " + str(asistencias) + " veces a sesiones del congreso"


def porcentaje_asistencias(informacion: list) -> list:
    lista_congre = []

    for i in informacion:
        ejecucion = analizar_asis(i["asistencia"])
        congresista_asis = {}
        asistencias = ejecucion["asistio"]
        total = ejecucion["sesiones"]
        congresista_asis["nombre"] = i["nombre"]
        congresista_asis["porcentaje_asistencia"] = round(asistencias / total, 2)
        lista_congre.append(congresista_asis)

    return lista_congre


def circunscripcion_mas_inasistencias(informacion: list) -> str:

    numero_de_fallas = 0
    circunscripcion = None

    for i in informacion:
        ejecucion = analizar_asis(i["asistencia"])
        fallas = ejecucion["sin_excusa"] + ejecucion["otra_excusa"] + ejecucion["ex_medica"]
        if fallas > numero_de_fallas:
            numero_de_fallas = ejecucion["sin_excusa"]
            circunscripcion = i["circunscripcion"]

    return "La circunscripción " + circunscripcion + " acumuló " + str(numero_de_fallas) + " fallas"


def mas_inasistencias_excusa(informacion: list) -> str:
    nombre = None
    excusados = 0

    for i in informacion:
        asistencia = i["asistencia"]
        ejecucion = analizar_asis(asistencia)
        if ejecucion["ex_medica"] > excusados:
            excusados = ejecucion["ex_medica"]
            nombre = i["nombre"]

    return "El congresista " + nombre + " falló " + str(excusados) + " veces con excusa médica"


def mas_X_inasistencias(informacion: list, numero_fallas: int):

    ausentes = {}

    for congre in informacion:
        ejecucion = analizar_asis(congre["asistencia"])
        inasistencias = ejecucion["sesiones"] - ejecucion["asistio"] - ejecucion["suspension"] - ejecucion[
            "silla_vacia"]
        if inasistencias > numero_fallas:
            ausentes[congre["nombre"]] = inasistencias

    if len(ausentes) == 0:
        return "Ningún congresista supera el limite establecido"
    else:
        return ausentes


def asistencias_partido(informacion: list) -> dict:

    porcentaje_partido = {}

    for i in informacion:
        ejecucion = analizar_asis(i["asistencia"])
        if i["movimiento"] in porcentaje_partido.keys():
            asistencias = ejecucion["asistio"]
            total = ejecucion["sesiones"]
            porcentaje_partido[i["movimiento"]]["asistencia"] += asistencias
            porcentaje_partido[i["movimiento"]]["total"] += total
        else:
            dict_movimiento = {"asistencia": 0, "total": 0}
            dict_movimiento["asistencia"] = ejecucion["asistio"]
            dict_movimiento["total"] = ejecucion["sesiones"]
            porcentaje_partido[i["movimiento"]] = dict_movimiento
    for movimiento in porcentaje_partido:
        porcentaje_partido[movimiento] = round(
            porcentaje_partido[movimiento]["asistencia"] / porcentaje_partido[movimiento]["total"], 2)

    return porcentaje_partido


def analizar_fecha(fecha: str) -> list:

    datos = fecha.split("/")

    return datos


def fecha_mas_inasistencias(informacion: list) -> str:

    fechas = {}

    for congre in informacion:
        asistencias = congre["asistencia"]
        for fecha in asistencias:
            if fechas[fecha] != "ASISTIÓ":
                if fecha in asistencias:
                    fechas[fecha] += 1
                else:
                    fechas[fecha] = 1

    fecha_max = ""
    inasistencias = 0

    for fecha in fechas.keys():
        if fecha in fechas:
            fecha_max = fecha
            inasistencias = fechas[fecha]

    return "En la fecha {0} hubo {1} fallas".format(fecha_max, inasistencias)


def mes_mayor_sesiones(informacion: list) -> str:

    fecha = None
    sesiones = 0
    fechas = {}

    for congre in informacion:
        asistencias = congre["asistencia"]
        for elemento in asistencias:
            datos = analizar_fecha(elemento)
            fecha = str(datos[1]) + "/" + str(datos[2])
            if fecha in fechas.keys():
                fechas[fecha] += 1
            else:
                fechas[fecha] = 1

    for sesion in fechas.keys():
        if fechas[sesion] > sesiones:
            fecha = sesion
            sesiones = fechas[sesion]

    return "En el mes {0} hubo {1} sesiones".format(fecha, sesiones)


def format_fecha(n: int) -> str:

    if n < 10:
        return "0" + str(n)
    else:
        return str(n)


def asistio_fecha(informacion: list, nombre: str, dia: int, mes: int, anio: int) -> bool:

    fecha_dada = "{0}/{1}/{2}".format(format_fecha(dia), format_fecha(mes), anio)

    for i in informacion:
        if nombre == i["nombre"]:
            asistencias = i["asistencia"]
            if asistencias[fecha_dada] == "ASISTIÓ":
                return True
            else:
                return False


def asistencia_circunscripcion_fecha(informacion: list, mes: int, anio: int) -> dict:

    salida = {}

    for i in informacion:
        asistencia = i["asistencia"]
        cir = i["circunscripcion"]
        for elemento in asistencia:
            datos = analizar_fecha(elemento)
            if datos[1] == format_fecha(mes) and datos[2] == str(anio) and asistencia[elemento] == "ASISTIÓ":
                if cir in salida.keys():
                    salida[cir] += 1
                else:
                    salida[cir] = 1

    return salida

def generar_resumen_congresistas(informacion: list, movimiento: str) -> list:

    salida = []
    congresista = {}

    for i in informacion:
        partido = i["movimiento"]
        if partido == movimiento:
            ejecucion = analizar_asis(i["asistencia"])
            congresista["nombre"] = i["nombre"]
            congresista["ASISTIÓ"] = ejecucion["asistio"]
            congresista["EX. MÉDICA"] = ejecucion["ex_medica"]
            congresista["OTRAS EXCUSAS"] = ejecucion["otra_excusa"]
            congresista["SUSPENSIÓN"] = ejecucion["suspension"]
            congresista["SILLA VACÍA"] = ejecucion["silla_vacia"]
            congresista["SIN EXCUSA"] = ejecucion["sin_excusa"]
            congresista["TOTAL"] = ejecucion["sesiones"]
            salida = salida.append(congresista)

    return salida


def exportar_resumen_asistencias_movimiento(informacion:list, movimiento: str):

    for i in informacion:
        partido = i["movimiento"]
        if movimiento == partido:
            ejecucion = analizar_asis(i["asistencia"])
            nombre = "{}\n"
            titulo = "ASISTIÓ|EX. MÉDICA|OTRAS EXCUSA|SIN EXCUSA|SUSPENSIÓN|SILLA VACÍA|TOTAL"
            texto = "{0}\t\t{1}\t\t{2}\t\t{3}\t\t{4}\t\t{5}\t\t{6}"
            intro = nombre.format(i["nombre"])
            archivo = open("resumen_asistencia_{}.txt".format(i["movimiento"]), "w", encoding = "utf-8")
            linea = archivo.write("__________________________________________\n")
            linea = archivo.write("------------------------------------------\n")
            linea = archivo.write("Resumen de asistencias para el movimiento {}\n".format(i["movimiento"]))
            linea = archivo.write("__________________________________________\n")
            linea = archivo.write("------------------------------------------\n")
            linea = archivo.write("")
            linea = archivo.write(intro)
            linea = archivo.write("")
            linea = archivo.write(texto.format(ejecucion["asistio"], ejecucion["ex_medica"], ejecucion["otra_excusa"], ejecucion["sin_excusa"], ejecucion["suspension"], ejecucion["silla_vacia"], ejecucion["sesiones"]))
            archivo.close()