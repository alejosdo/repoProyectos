
import asistencia_congreso as asis


def ejecutar_cargar_datos() -> list:

    asistencia = None
    archivo = input("Por favor ingrese el nombre del archivo CSV con la asistencia: ")
    asistencia = asis.cargar_datos(archivo)
    if len(asistencia)==0:
        print("El archivo seleccionado no es válido. No se pudo cargar la información de la asistencia.")
    else:
        print("Se cargaron las asistencias de los siguientes congresistas a partir del archivo.")
        for elemento in asistencia:
            print(elemento)
    return asistencia

def ejecutar_mas_inasistencias(asistencias:list) -> None:

    resultado = asis.mas_inasistencias(asistencias)
    
    print(resultado)

def ejecutar_mas_asistencias(asistencias:list) -> None:

    resultado = asis.mas_asistencias(asistencias)

    print(resultado)

def ejecutar_porcentaje_asistencias(asistencias:list) -> None:

    resultado = asis.porcentaje_asistencias(asistencias)

    print(resultado)

def ejecutar_circunscripcion_mas_inasistencias(asistencias:list) -> None:

    resultado = asis.circunscripcion_mas_inasistencias(asistencias)

    print(resultado)

def ejecutar_mas_inasistencias_excusa(asistencias:list) -> None:

    resultado = asis.mas_inasistencias_excusa(asistencias)

    print(resultado)

def ejecutar_mas_X_inasistencias(asistencias:list) -> None:

    numero_fallas = int(input("Por favor ingrese un número de fallas determinado: "))

    resultado = asis.mas_X_inasistencias(asistencias, numero_fallas)

    print(resultado)

def ejecutar_asistencias_partido(asistencias:list) -> None:

    resultado = asis.asistencias_partido(asistencias)

    print(resultado)

def ejecutar_fecha_mas_inasistencias(asistencias:list) -> None:

    resultado = asis.fecha_mas_inasistencias(asistencias)

    print(resultado)

def ejecutar_mes_mayor_sesiones(asistencias:list) -> None:

    resultado = asis.mes_mayor_sesiones(asistencias)

    print(resultado)

def ejecutar_asistio_fecha(asistencias:list):

    nombre = int(input("Por favor ingrese el nombre del congresista que desea buscar: "))
    anio = int(input("Por favor ingrese el año en el que desea buscar: "))
    mes = int(input("Por favor ingrese el mes en el que desea buscar: "))
    dia = int(input("Por favor ingrese el día en el que desea buscar: "))

    resultado = asis.asistio_fecha(asistencias, nombre, dia, mes, anio)

    if resultado == True:
        print("El congresista {0} asisitió a la sesión de la fecha {1}/{2}/{3}".format(nombre, dia, mes, anio))
    else:
        print("El congresista no asistió o no hubo sesión ese día")

def ejecutar_asistencia_circunscripcion_fecha(asistencia:list) -> None:

    mes = int(input("Por favor ingrese el mes en el que desea buscar: "))
    anio = int(input("Por favor ingrese el año en el que desea buscar: "))
    resultado = asis.asistencia_circunscripcion_fecha(asistencia, mes, anio)

    print(resultado)

def mostrar_menu():
    print("\nOpciones")
    print("1. Cargar el archivo con la asistencia al congreso")
    print("2. Consultar congresista con más inasistencias injustificadas")
    print("3. Consultar congresista con más asistencias")
    print("4. Calcular porcentaje de asistencia de los congresistas")
    print("5. Consultar la circunscripcion con mas inasistencias")
    print("6. Consultar el congresista con más inasistencias con excusa médica")
    print("7. Consultar congresistas que fallan más de un número determinado de veces")
    print("8. Consultar porcentaje de asistencias por partido político")
    print("9. Consultar fecha con más fallas")
    print("10. Consutlar mes y año con mayor número de sesiones realizadas")
    print("11. Consultar asistencias de congresista por fecha")
    print("12. Consultar asistencia por circunscripcion por mes y año")
    print("13. Salir de la aplicacion")

def iniciar_aplicacion():

    continuar  = True
    asistencia = None

    while continuar:
        mostrar_menu()
        opcion_seleccionada = int(input("Por favor seleccione una opción: "))
        if opcion_seleccionada == 1:
            asistencia = ejecutar_cargar_datos()
        elif opcion_seleccionada == 2:
            ejecutar_mas_inasistencias(asistencia)
        elif opcion_seleccionada == 3:
            ejecutar_mas_asistencias(asistencia)
        elif opcion_seleccionada == 4:
            ejecutar_porcentaje_asistencias(asistencia)
        elif opcion_seleccionada == 5:
            ejecutar_circunscripcion_mas_inasistencias(asistencia)
        elif opcion_seleccionada == 6:
            ejecutar_mas_inasistencias_excusa(asistencia)
        elif opcion_seleccionada == 7:
            ejecutar_mas_X_inasistencias(asistencia)
        elif opcion_seleccionada == 8:
            ejecutar_asistencias_partido(asistencia)
        elif opcion_seleccionada == 9:
            ejecutar_fecha_mas_inasistencias(asistencia)
        elif opcion_seleccionada == 10:
            ejecutar_mes_mayor_sesiones(asistencia)
        elif opcion_seleccionada == 11:
            ejecutar_asistio_fecha(asistencia)
        elif opcion_seleccionada == 12:
            ejecutar_asistencia_circunscripcion_fecha(asistencia)
        elif opcion_seleccionada == 13:
            continuar = False
        else:
            print("Por favor ingrese una opcion válida")

iniciar_aplicacion()