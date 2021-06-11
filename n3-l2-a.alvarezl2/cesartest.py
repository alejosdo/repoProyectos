# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 20:06:04 2021

@author: alejo
"""

import cesar

def test_cesar():
    
    test_cesar_caracter = "n"
    corr = 1
    e = cesar.trad_valor(test_cesar_caracter, corr)
    
    assert e == "m"
    
def test_cesar0():
    
    test_cesar_caracter = " "
    corr = 1
    e = cesar.trad_valor(test_cesar_caracter, corr)
    
    assert e == " "
    
def test_cesar1():
    
    test_cesar_caracter = "a"
    corr = 3
    e = cesar.trad_valor(test_cesar_caracter, corr)
    
    assert e == "x"
    
def test_cesar2():
    
    test_cesar_caracter = "["
    corr = 1
    e = cesar.descifrar_codigo_cesar(test_cesar_caracter, corr)
    
    assert e == "["
    
test_cesar()
test_cesar0()
test_cesar1()
test_cesar2()