"""
Este módulo contiene una clase con pruebas unitarias para verificar su correcto funcionamiento.
"""

from calculadora import suma


def test_suma_positivos():
    assert suma(3, 5) == 8

def test_suma_negativos():
    assert suma(-3, -7) == -10

def test_suma_positivo_negativo():
    assert suma(10, -5) == 5

def test_suma_ceros():
    assert suma(0, 0) == 0

def test_suma_decimales():
    assert suma(2.5, 3.5) == 6.0
