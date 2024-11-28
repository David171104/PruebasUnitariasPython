
import pytest
from calculadora_class6 import multiplicar, sumar


@pytest.mark.parametrize("a, b, resultado", [
    (3, 5, 15),      
    (-3, -2, 6),     
    (0, 5, 0),      
    (5, 0, 0)        
])


def test_multiplicar(a, b, resultado):
    assert multiplicar(a, b) == resultado


@pytest.mark.parametrize("a, b, resultado", [
    (10, 5, 15),     
    (-3, -7, -10),   
    (10, -5, 5),    
])


def test_sumar(a, b, resultado):
    assert sumar(a, b) == resultado
