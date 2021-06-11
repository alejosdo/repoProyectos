# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 22:09:20 2021

@author: Alejandro
"""

import analizador_sangre as mod

def mostrar_paciente(examen: dict) -> None:

    identidad = examen["id"]
    genero = examen["genero"]
    edad = examen["edad"]
    PPM = examen["PPM"]
    Hb = examen["Hb"]
    CGB = examen["CGB"]
    glicemia = examen["glicemia"]
    LDL = examen["LDL"]
    HDL = examen["HDL"]
    trigliceridos = examen["trigliceridos"]
    CT = examen["CT"]
    CL = examen["CL"]
    CP = examen["CP"]
    tiempo = examen["tiempo"]
    GCH = examen["GCH"]

    print("identidad: " + str(identidad) + " - Género: " + str(genero) + " - Edad: " + str(edad) +
          "\nPPM: " + str(PPM) + " - Hb: " + str(Hb) + " - CGB: " + str(CGB) + " - Glicemia: " + str(glicemia) +
          "\nLDL: " + str(LDL) + " - HDL: " + str(HDL) + "Triglicéridos: " + str(trigliceridos) + " - CT: " + str(CT) +
          "\nCL: " + str(CL) + " - CP: " + str(CP) + " Tiempo: " + str(tiempo) + "GCH: " + str(GCH))


def ejecutar_confirmar_embarazo(e1: dict, e2: dict, e3: dict, e4: dict) -> None:

    identidad = solicitar_identidad()
    
    salida = mod.buscar_examen(identidad, e1, e2, e3, e4)
    
    resultado = mod.confirmar_embarazo(salida)
    
    if salida["genero"] != "femenino":
        print("Genero inválido")
    
    if resultado == True:
        print("Los resultados del exámen sugieren que la paciente está embarazada.")
    else :
        print("Los resultados del exámen sugieren que la paciente NO está embarazada.")


def ejecutar_validar_pulsaciones(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    
    identidad = solicitar_identidad()

    salida = mod.buscar_examen(identidad, e1, e2, e3, e4)
    
    resultado = mod.validar_pulsaciones(salida)
    
    return resultado

def ejecutar_confirmar_anemia(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    
    identidad = solicitar_identidad()
    
    salida = mod.buscar_examen(identidad, e1, e2, e3, e4)
    
    resultado = mod.confirmar_anemia(salida)
    
    if resultado == True:
        print("El paciente presenta indicaciones de sufir anemia.")
    if resultado == False:
        print("El paciente NO presenta indicaciones de sufir anemia.")

def ejecutar_contar_hipoglicemicos(e1: dict, e2: dict, e3: dict, e4: dict) -> None:

    resultado = mod.contar_hipoglicemicos(e1, e2, e3, e4)
    
    print("Hay " + str(resultado) + " pacientes hipoglicémicos.")

def ejecutar_validar_infecciones(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    
    salida = mod.validar_infecciones(e1, e2, e3, e4)
    
    resultado = "Los siguientes pacientes presentan riesgo de tener infecciones: " + salida
    
    print(resultado)
    

def ejecutar_calcular_promedio(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    
    resultado = mod.calcular_promedio(e1, e2, e3, e4)
    
    print("El tiempo promedio en que las muestras tardan en procesarse es " + str(resultado))
    
    return resultado

def ejecutar_actualizar_glicemia(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    
    identidad = solicitar_identidad()
    
    tipo = int(input("Ingrese el tipo de ampolla: "))
    
    objetivo = int(input("Ingrese el nivel de azucar objetivo: "))
    
    salida = mod.buscar_examen(identidad, e1, e2, e3, e4)
    
    resultado = mod.actualizar_glicemia(tipo, objetivo, salida)
    
    print(str(round(resultado)) + " unidades de insulina deben ser administradas al paciente.")

def ejecutar_validar_diabetes(e1: dict, e2: dict, e3: dict, e4: dict) -> None:
    
    identidad = solicitar_identidad()
    
    salida = mod.buscar_examen(identidad, e1, e2, e3, e4)
    
    resultado = mod.validar_diabetes(salida)
    
    print(resultado)

def ejecutar_evaluar_prioridad(e1: dict, e2: dict, e3: dict, e4: dict) -> dict:

    x = mod.evaluar_prioridad(e1, e2, e3, e4)
    
    print("El paciente con ID " + str(x["id"]) + " debe ser atendido con prioridad.")
    
    return x

def solicitar_identidad() ->int:
    
    identidad = int(input("Ingrese el identificador del paciente que quiere buscar: "))
    
    return identidad

def ejecutar_validar_CLL(e1: dict, e2: dict, e3: dict, e4: dict) -> int:

    identidad = solicitar_identidad()
    frotis = bool(int(input("Ingresa 1 si el examen de Frotis salió positivo, 0 de lo contrario: ")))
    
    salida = mod.buscar_examen(identidad, e1, e2, e3, e4)
    
    resultado = mod.validar_CLL(salida, frotis)
    
    if resultado == 1:
        print("Los resultados sugieren que el paciente es positivo para CLL")
    
    elif resultado == -1:
        print("Se debe realizar una biopsia de médula para confirmar el diagnóstico de CLL")
        
    elif resultado == 0:
        print("El paciente no presenta indicaciones de CLL")
    
    return resultado

def iniciar_aplicacion():
    """Inicia la ejecucion de la aplicacion por consola.
    Esta funcion primero crea cuatro resultados de exámenes de sangre.
    Luego la funcion le muestra el menu al usuario y espera a que seleccione una opcion.
    Esta operacion se repite hasta que el usuario seleccione la opcion de salir.
    """
    examen1 = mod.crear_paciente(
    1, "masculino", 20, 88, 20, 11.5, 280, 89.7, 50, 120.8, 240, 7.9, 150, 25, 0)
    examen2 = mod.crear_paciente(
        2, "femenino", 30, 90, 9, 10.5, 69, 98.3, 60, 100.9, 225, 9.8, 141, 35, 10)
    examen3 = mod.crear_paciente(
        3, "femenino", 69, 70, 15, 12.5, 115, 138.6, 40, 150.3, 260, 8.2, 160, 15, 2)
    examen4 = mod.crear_paciente(
        4, "masculino", 33, 60, 10, 9.9, 65, 102.5, 55, 120.8, 236, 10.6, 167, 43, 0)

    ejecutando = True
    while ejecutando:
        print("\n\nResultado de los exámenes" + ("-"*50))
        print("Examen de Sangre 1")
        mostrar_paciente(examen1)
        print("-"*50)

        print("Examen de Sangre 2")
        mostrar_paciente(examen2)
        print("-"*50)

        print("Examen de Sangre 3")
        mostrar_paciente(examen3)
        print("-"*50)

        print("Examen de Sangre 4")
        mostrar_paciente(examen4)
        print("-"*50)

        ejecutando = mostrar_menu_aplicacion(
            examen1, examen2, examen3, examen4)

        if ejecutando:
            input("Presione cualquier tecla para continuar... ")

def mostrar_menu_aplicacion(e1: dict, e2: dict, e3: dict, e4: dict) -> bool:
    """Le muestra al usuario las opciones de ejecucion disponibles.
    Parametros:
        e1 (dict): Diccionario que contiene la informacion del examen 1.
        e2 (dict): Diccionario que contiene la informacion del examen 2.
        e3 (dict): Diccionario que contiene la informacion del examen 3.
        e4 (dict): Diccionario que contiene la informacion del examen 4.
    Retorno:
        Esta funcion retorna True si el usuario selecciono una opcion diferente
        a la opcion que le permite salir de la aplicacion.
        Esta funcion retorna False si el usuario selecciono la opcion para salir
        de la aplicacion.

    """
    print("Menu de opciones")
    print(" 1 - Confirmar embarazo")
    print(" 2 - Validar PPM")
    print(" 3 - Confirmar Anémia")
    print(" 4 - Contar hipoglicémicos")
    print(" 5 - Validar infecciones")
    print(" 6 - Promedio de exámenes")
    print(" 7 - Actualizar Glicemia")
    print(" 8 - Validar diabetes")
    print(" 9 - Evaluar prioridad")
    print(" 10 - Validar CLL")
    print(" 11 - Salir de la aplicacion.")

    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()

    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_confirmar_embarazo(e1, e2, e3, e4)
    elif opcion_elegida == "2":
        ejecutar_validar_pulsaciones(e1, e2, e3, e4)
    elif opcion_elegida == "3":
        ejecutar_confirmar_anemia(e1, e2, e3, e4)
    elif opcion_elegida == "4":
        ejecutar_contar_hipoglicemicos(e1, e2, e3, e4)
    elif opcion_elegida == "5":
        ejecutar_validar_infecciones(e1, e2, e3, e4)
    elif opcion_elegida == "6":
        ejecutar_calcular_promedio(e1, e2, e3, e4)
    elif opcion_elegida == "7":
        ejecutar_actualizar_glicemia(e1, e2, e3, e4)
    elif opcion_elegida == "8":
        ejecutar_validar_diabetes(e1, e2, e3, e4)
    elif opcion_elegida == "9":
        ejecutar_evaluar_prioridad(e1, e2, e3, e4)
    elif opcion_elegida == "10":
        ejecutar_validar_CLL(e1, e2, e3, e4)
    elif opcion_elegida == "11":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    return continuar_ejecutando

iniciar_aplicacion()
