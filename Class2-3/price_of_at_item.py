"""
Este módulo contiene una función para calcular el precio de un articulo con descuento y una clase con pruebas
unitarias para verificar su correcto funcionamiento.
"""
import unittest


def calculate_discount(base_price, discount):
    """
    Encuentra el descuento de un producto y devuelve el resultado.

    Args:
        base_price (int o float): Precio.
        discount (int o float): Descuento.
    Returns:
        int o float: Resultado de aplicar el descuento al producto.
    """
    return (base_price * discount) / 100


class TestSum(unittest.TestCase):
    """
    Clase que contiene pruebas unitarias para la función calculate_discount.
    """

    def test_discount_0_percent(self):
        """
        Verifica que la función calculate_discount calcule correctamente el descuento de un producto.
        """
        # Arrange: Definir los valores de entrada
        price = 100
        discount = 0

        # Act: Ejecutar la función que se va a probar
        result = calculate_discount(price, discount)

        print(f"Probando el descuento  {discount}% en el producto ${price}, el resultado es: ${result}")

        # Assert: Verificar que el resultado es el esperado
        self.assertEqual(result, 0, "El descuento debería ser 0")

    def test_discount_10_percent(self):
        """
        Verifica que la función calculate_discount calcule correctamente el descuento de un producto.
        """
        # Arrange: Definir los valores de entrada
        price = 100
        discount = 10

        # Act: Ejecutar la función que se va a probar
        result = calculate_discount(price, discount)

        print(f"Probando el descuento  {discount}% en el producto ${price}, el resultado es: ${result}")

        # Assert: Verificar que el resultado es el esperado
        self.assertEqual(result, 10, "El descuento debería ser 10")


    def test_discount_50_percent(self):
        """
        Verifica que la función calculate_discount calcule correctamente el descuento de un producto.
        """
        # Arrange: Definir los valores de entrada
        price = 100
        discount = 50

        # Act: Ejecutar la función que se va a probar
        result = calculate_discount(price, discount)

        print(f"Probando el descuento  {discount}% en el producto ${price}, el resultado es: ${result}")

        # Assert: Verificar que el resultado es el esperado
        self.assertEqual(result, 50, "El descuento debería ser 50")

if __name__ == '__main__':
    unittest.main()