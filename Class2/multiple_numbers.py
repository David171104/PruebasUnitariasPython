"""
Este módulo contiene una función para multiplicar números y una clase con pruebas
unitarias para verificar su correcto funcionamiento.
"""
import unittest


def multiply_numbers(a, b):
    """
    Multiplica dos números y devuelve el resultado.

    Args:
        a (int o float): Primer número.
        b (int o float): Segundo número.

    Returns:
        int o float: Resultado de multiplicar a y b.
    """
    return a * b


class TestSum(unittest.TestCase):
    """
    Clase que contiene pruebas unitarias para la función multiply_numbers.
    """

    def test_multiply_two_numbers(self):
        """
        Verifica que la función multiply_numbers calcule correctamente el producto de dos números.
        """
        # Arrange: Definir los valores de entrada
        a = 2
        b = 3

        # Act: Ejecutar la función que se va a probar
        result = multiply_numbers(a, b)

        print(f"Probando los números {a} y {b}, el resultado es: {result}")

        # Assert: Verificar que el resultado es el esperado
        self.assertEqual(result, 6, "El producto de 2 y 3 debería ser 6")

if __name__ == '__main__':
    unittest.main()