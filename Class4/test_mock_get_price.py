"""
Este módulo contiene una función que obtiene el precio de un producto llamando a un servicio web
y una clase con pruebas unitarias para verificar su correcto funcionamiento.
"""

import unittest
from unittest.mock import patch


# Class representing a service to fetch the price of a product.
class PriceService:

    def get_price(self, product_id):
        """
        Simula la llamada al servicio web para obtener el precio de un producto.

        :param product_id: ID del producto.
        :return: Precio del producto o `None` si no existe.
        """
        
        print(f"Llamando al servicio web para obtener el precio del producto N°{product_id}...")
        return None


# Unit test class to verify the behavior of `PriceService`.
class TestPriceService(unittest.TestCase):
    """
    Pruebas unitarias para verificar que `get_price` retorna los valores correctos
    con base en la lógica interna de `PriceService`.
    """

    def setUp(self):
        self.service = PriceService()


    @patch.object(PriceService, 'get_price', return_value=49.99)  
    def test_get_price_with_existing_product(self, mock_get_price):
        """
        Verifica que el precio se obtiene correctamente para un producto existente.
        """
        product_id = 101
        expected_price = 49.99
        price = self.service.get_price(product_id)

        print(f"Probando función que verifica si se obtiene el precio correcto del producto N°{product_id}, el resultado es: {price}")
        self.assertEqual(price, expected_price)
        mock_get_price.assert_called_once_with(product_id)


    @patch.object(PriceService, 'get_price', return_value=75.50)  
    def test_get_price_with_another_existing_product(self, mock_get_price):
        """
        Verifica que el precio se obtiene correctamente para otro producto existente.
        """
        product_id = 202
        expected_price = 75.50
        price = self.service.get_price(product_id)

        print(f"Probando función que verifica si se obtiene el precio correcto del segundo producto N°{product_id}, el resultado es: {price}")
        self.assertEqual(price, expected_price)
        mock_get_price.assert_called_once_with(product_id)


    @patch.object(PriceService, 'get_price', return_value=None)  
    def test_get_price_with_nonexistent_product(self, mock_get_price):
        """
        Verifica que el método retorna `None` si el producto no existe.
        """
        product_id = 1000
        price = self.service.get_price(product_id)

        print(f"Probando función que verifica si el producto N°{product_id} no existe, el resultado es: {price}")
        self.assertIsNone(price)
        mock_get_price.assert_called_once_with(product_id)


if __name__ == "__main__":
    unittest.main()
