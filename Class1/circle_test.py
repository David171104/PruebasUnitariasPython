import pytest
from unittest.mock import patch
import math

def circle_area(radio):
    """
    Calcule el area de un circulo mediante este algoritmo.
    :return: El área del círculo.
    :raises ValueError: Si el radio ingresado no es válido (negativo o no numérico).
    """
    # radio = float(input("Por favor, introduce el radio del círculo: "))
    if radio < 0:
        raise ValueError("El radio no puede ser negativo.")
    return math.pi * radio ** 2



#Circle area
@pytest.mark.parametrize("radio, expected_value", [
    (3, math.pi * 3 ** 2),  # Case positive
    (0, 0),                 # Case zero
])
def test_circle_area_valid(radio, expected_value):
    area = circle_area(radio)
    print(f"Radio: {radio}, Área calculada: {area}")
    assert area == pytest.approx(expected_value, rel=1e-6)

def test_circle_area_invalid():
    with pytest.raises(ValueError, match="El radio no puede ser negativo."):
        print("Probando radio negativo...")
        circle_area(-5)




# if __name__ == "__main__":
#     pytest.main()
