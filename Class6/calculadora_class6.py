""" Este ejercicio tiene una función simple, para multiplicar dos numeros """


def multiplicar(a, b):
    return a * b


def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b


def restar(a, b):
    """Resta dos números y devuelve el resultado."""
    return a - b


def dividir(a, b):
    """Divide dos números y devuelve el resultado. Maneja la división por cero."""
    if b == 0:
        return "Error: División por cero"
    return a / b