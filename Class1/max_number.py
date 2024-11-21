import pytest
from unittest.mock import patch
import math

def find_max_number(numbers):
    """
    Recibe una lista de números y devuelve el número mayor.
    :param numbers: Lista de números.
    :return: El número mayor.
    :raises ValueError: Si la lista está vacía.
    """
    # user_input = input("Ingresa una lista de números, separados por espacios: ")
    
   
    # numbers = [float(num) for num in user_input.split()]

    if not numbers:
        raise ValueError("La lista no puede estar vacía.")
    return max(numbers)

#Max number on a list
@pytest.mark.parametrize("numbers, expected_max", [
    ([6, 5, 4, 1, 2, 9], 9),  # Case positive
    ([-1, -4, -2, -8], -1),  # Case negative
    ([0], 0),                # Case with one number
])
def test_find_max_number_valid(numbers, expected_max):
    max_number = find_max_number(numbers)
    assert max_number == expected_max

def test_find_max_number_empty():
    with pytest.raises(ValueError, match="La lista no puede estar vacía."):
        find_max_number([])

