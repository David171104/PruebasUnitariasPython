"""
Este módulo contiene una función para calcular el numero mayor entre dos numeros y una clase con pruebas
unitarias para verificar su correcto funcionamiento.
"""
import unittest


def calculate_higher_number(a, b):
    """
    Encuentra el numero mayor entre dos numeros y devuelve el resultado.

    Args:
        a (int o float): Primer numero.
        b (int o float): Segundo numero.
    Returns:
        int o float: Resultado de comparar ambos numeros para saber cual es mayor.
    """
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "Ambos números son iguales"



class TestSum(unittest.TestCase):
    """
    Clase que contiene pruebas unitarias para la función calculate_higher_number.
    """

    def test_calculate_higher_number_5(self):
        """
        Verifica que la función calculate_higher_number calcule correctamente el numero mayor.
        """
        # Arrange: Definir los valores de entrada
        a = 5
        b = 3

        # Act: Ejecutar la función que se va a probar
        result = calculate_higher_number(a, b)

        print(f"Probando la funcion para calcular el numero mayor entre {a} y {b}, el resultado es que el numero mayor es: {result}")

        # Assert: Verificar que el resultado es el esperado
        self.assertEqual(result, 5, "El numero mayor debería ser 5")


    def test_calculate_higher_number_7(self):
        """
        Verifica que la función calculate_higher_number calcule correctamente el numero mayor.
        """
        # Arrange: Definir los valores de entrada
        a = 2
        b = 7

        # Act: Ejecutar la función que se va a probar
        result = calculate_higher_number(a, b)

        print(f"Probando la funcion para calcular el numero mayor entre {a} y {b}, el resultado es que el numero mayor es: {result}")

        # Assert: Verificar que el resultado es el esperado
        self.assertEqual(result, 7, "El numero mayor debería ser 7")


    def test_calculate_higher_number_equal(self):
        """
        Verifica que la función calculate_higher_number maneje correctamente cuando ambos números son iguales.
        """
        # Arrange: Definir los valores de entrada
        a = 7
        b = 7

        # Act: Ejecutar la función que se va a probar
        result = calculate_higher_number(a, b)

        print(f"Probando la función para calcular el número mayor entre {a} y {b}, el resultado es: {result}")

        # Assert: Verificar que el resultado es el esperado
        self.assertEqual(result, "Ambos números son iguales", "Debería indicar que ambos números son iguales")

   

if __name__ == '__main__':
    unittest.main()