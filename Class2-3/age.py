"""
Módulo para probar la función `calculate_age` utilizando pytest y
parámetros de prueba.
"""

import pytest
from datetime import date


def calculate_age(date_of_birth):
    """
    Verifica si una persona es mayor de edad basándose en su fecha de nacimiento.

    Args:
        date_of_birth (datetime.date): Fecha de nacimiento de la persona.

    Returns:
        tuple: Un mensaje indicando si es mayor de edad y la edad calculada.
    """
    current_date = date.today()
    age = current_date.year - date_of_birth.year

    # Verificar si aún no ha llegado el cumpleaños en el año actual
    if (current_date.month, current_date.day) < (date_of_birth.month, date_of_birth.day):
        age -= 1

    if age >= 18:
        return "El usuario es mayor de edad", age
    else:
        return "El usuario es menor de edad", age


@pytest.mark.parametrize(
    "date_of_birth, expected_message, expected_age",
    [
        (date(2000, 1, 1), "El usuario es mayor de edad", 24),  # Caso mayor de edad
        (date(2010, 5, 20), "El usuario es menor de edad", 14), # Caso menor de edad
        (date(2005, 11, 21), "El usuario es mayor de edad", 19), # Recién cumplió 18
        (date(2006, 11, 22), "El usuario es menor de edad", 17), # Cumple en el futuro este año
    ],
)
def test_calculate_age(date_of_birth, expected_message, expected_age):
    """
    Prueba la función calculate_age con varios casos usando pytest.mark.parametrize.
    """
    result_message, result_age = calculate_age(date_of_birth)

    # Verifica que el mensaje sea el esperado
    assert result_message == expected_message, f"Esperado: {expected_message}, obtenido: {result_message}"
    # Verifica que la edad sea correcta
    assert result_age == expected_age, f"Esperado: {expected_age}, obtenido: {result_age}"