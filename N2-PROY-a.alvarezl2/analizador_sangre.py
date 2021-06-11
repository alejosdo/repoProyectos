# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 22:09:20 2021

@author: Alejandro
"""

def crear_paciente(identidad: int, genero: str, edad: int, PPM: int,
                   Hb: int, CGB: float, glicemia: int, LDL: float, HDL: float, trigliceridos: float, CT: float,
                   CL: float, CP: float, tiempo: int, GCH: int) -> dict:

    paciente = {
        "id" : identidad,
        "genero" : genero,
        "edad" : edad,
        "PPM" : PPM,
        "Hb" : Hb,
        "CGB" : CGB,
        "glicemia" : glicemia,
        "LDL" : LDL,
        "HDL" : HDL,
        "trigliceridos" : trigliceridos,
        "CT" : CT,
        "CL" : CL,
        "CP" : CP,
        "tiempo" : tiempo,
        "GCH" : GCH
        }
    
    resultado = paciente
    
    print(resultado)
    
    return resultado

def buscar_examen(identidad:int, e1:dict,e2:dict, e3:dict, e4:dict)->dict:
    
    for v in e1,e2,e3,e4:
        if identidad == v['id']:
            return v
        
    return None
    
def confirmar_embarazo(examen:dict)->bool:
    
    if examen["GCH"] < 9:
        return False
    return True
        
def validar_pulsaciones(examen:dict)->str:
    
    if examen["genero"] == "femenino":
        if examen["edad"] >= 20 and examen["edad"] <= 29:
            if examen["PPM"] <= 70:
                print("El paciente presenta bradicardia")
            if examen["PPM"] >= 72 and examen["PPM"] <= 94:
                print("El paciente no presenta ninguna anormalidad en su pulso.")
            if examen["PPM"] >= 96:
                print("El paciente presenta taquicardia")
        if examen["edad"] >= 30 and examen["edad"] <= 39:
            if examen["PPM"] <= 70:
                print("El paciente presenta bradicardia")
            if examen["PPM"] >= 72 and examen["PPM"] <= 96:
                print("El paciente no presenta ninguna anormalidad en su pulso.")
            if examen["PPM"] >= 98:
                print("El paciente presenta taquicardia")
        if examen["edad"] >= 40 and examen["edad"] <= 49:
            if examen["PPM"] <= 72:
                print("El paciente presenta bradicardia")
            if examen["PPM"] >= 74 and examen["PPM"] <= 89:
                print("El paciente no presenta ninguna anormalidad en su pulso.")
            if examen["PPM"] >= 100:
                print("El paciente presenta taquicardia")
        if examen["edad"] >= 50:
            if examen["PPM"] <= 74:
                print("El paciente presenta bradicardia")
            if examen["PPM"] >= 76 and examen["PPM"] <= 102:
                print("El paciente no presenta ninguna anormalidad en su pulso.")
            if examen["PPM"] >= 104:
                print("El paciente presenta taquicardia")
    
    if examen["genero"] == "masculino":
        if examen["edad"] >= 20 and examen["edad"] <= 29:
            if examen["PPM"] <= 60:
                print("El paciente presenta bradicardia")
            if examen["PPM"] >= 62 and examen["PPM"] <= 84:
                print("El paciente no presenta ninguna anormalidad en su pulso.")
            if examen["PPM"] >= 86:
                print("El paciente presenta taquicardia")
        if examen["edad"] >= 30 and examen["edad"] <= 39:
            if examen["PPM"] <= 62:
                print("El paciente presenta bradicardia")
            if examen["PPM"] >= 64 and examen["PPM"] <= 84:
                print("El paciente no presenta ninguna anormalidad en su pulso.")
            if examen["PPM"] >= 86:
                print("El paciente presenta taquicardia")
        if examen["edad"] >= 40 and examen["edad"] <= 49:
            if examen["PPM"] <= 64:
                print("El paciente presenta bradicardia")
            if examen["PPM"] >= 66 and examen["PPM"] <= 88:
                print("El paciente no presenta ninguna anormalidad en su pulso.")
            if examen["PPM"] >= 90:
                print("El paciente presenta taquicardia")
        if examen["edad"] >= 50:
            if examen["PPM"] <= 66:
                print("El paciente presenta bradicardia")
            if examen["PPM"] >= 68 and examen["PPM"] <= 88:
                print("El paciente no presenta ninguna anormalidad en su pulso.")
            if examen["PPM"] >= 90:
                print("El paciente presenta taquicardia")

def confirmar_anemia(examen:dict) -> bool:
    
    hto = examen["Hb"] * 3.1
    
    if examen["edad"] < 5 and hto >= 33:
        return True
    if examen["edad"] >= 5 and examen["edad"] <= 11 and hto >= 34:
        return True
    if examen["edad"] >= 12 and examen["edad"] <=14  and hto >= 36:
        return True
    if examen["edad"] >= 15 and examen["genero"] == "femenino" and confirmar_embarazo(examen) == False and hto >= 36:
        return True
    if examen["edad"] >= 15 and examen["genero"] == "femenino" and confirmar_embarazo(examen) == True and hto >= 33:
        return True
    if examen["edad"] >= 15 and examen["genero"] == "masculino" and hto >= 39:
        return True
    
    return False

def contar_hipoglicemicos(e1:dict,e2:dict, e3:dict, e4:dict)->int:
    
    resultado = 0
    
    if e1["glicemia"] < 70:
        resultado += 1
    if e2["glicemia"] < 70:
        resultado += 1
    if e3["glicemia"] < 70:
        resultado += 1
    if e4["glicemia"] < 70:
        resultado += 1
    
    return resultado

def validar_infecciones(e1:dict,e2:dict, e3:dict, e4:dict)-> str:
    
    resultado = ""
    
    if e1["CGB"] > 11:
        resultado += str(e1["id"])
    if e2["CGB"] > 11:
        if resultado != "":
            resultado += ", " 
        resultado += str(e2["id"])
    if e3["CGB"] > 11:
        if resultado != "":
            resultado += ", " 
        resultado += str(e3["id"])
    if e4["CGB"] > 11:
        if resultado != "":
            resultado += ", "
        resultado += str(e4["id"])
    
    return resultado

def calcular_promedio(e1:dict,e2:dict, e3:dict, e4:dict)->float:
    
    resultado = (e1["tiempo"] + e2["tiempo"] + e3["tiempo"] + e4["tiempo"]) / 4
    
    return round(resultado)

def actualizar_glicemia(tipo:int, objetivo:int, examen:dict)-> int:
    
    if tipo == 1:
        correccion = 40
        
    if tipo == 2:
        correccion = 50
    
    if examen["glicemia"] < 250:
        return 0
    else:
        return (examen["glicemia"] - objetivo) / correccion
        
def validar_diabetes(examen:dict)->str:
    
    resultado = "El paciente presenta "
    
    if examen["glicemia"] >= 126:
        return resultado + "diabetes"
    elif examen["glicemia"] >= 100 and examen["glicemia"] <= 125:
        return resultado + "prediabetes"
    else:
        return "El paciente no presenta ninguna anormalidad"

def calcular_riesgo_cardiaco(examen:dict)->int:
    
    resultado = 0
    
    if examen["CT"] > 239:
        resultado += 1
    
    if examen["glicemia"] >= 126:
        if examen["LDL"] >= 100:
            resultado += 1
    else :
        if examen["LDL"] >= 130:
            resultado += 1

    if examen["genero"] == "masculino" and examen["HDL"] < 40:
        resultado += 1
    elif examen["genero"] == "femenino" and examen["HDL"] < 50:
        resultado += 1
    if examen["trigliceridos"] >= 150:
        resultado += 2
    
    return resultado

def evaluar_prioridad(e1:dict, e2:dict, e3:dict, e4:dict)->dict:
    
    valores = [e1, e2, e3, e4]
    
    i = 0
    
    for v in valores:
        prio = calcular_riesgo_cardiaco(v)
        if prio > i:
            i = prio
            resultado = v
     
    return resultado

def validar_CLL(examen:dict, frotis:bool) -> int:
    
    if examen["CL"] >= 10:
        resultado = 1
    elif examen["CL"] >= 8 and examen["CL"] <= 9.999:
        if examen["CP"] < 145:
            resultado = 1
    elif examen["CP"] < 8:
        if frotis:
            resultado = -1
        else :
            resultado = 0
    
    return resultado



