""" Este ejercicio tiene una función simple, para multiplicar dos numeros """

import unittest
from calculadora_class6 import multiplicar, sumar, restar, dividir


class TestCalculadora(unittest.TestCase):

    def test_multiplicar_positivos(self):
        self.assertEqual(multiplicar(3, 5), 15)

    def test_multiplicar_negativos(self):
        self.assertEqual(multiplicar(-3, -2), 6)

    def test_sumar_positivos(self):
        self.assertEqual(sumar(3, 5), 8)

    def test_sumar_negativos(self):
        self.assertEqual(sumar(-3, -7), -10)

    # Pruebas de resta
    def test_restando_positivos(self):
        self.assertEqual(restar(10, 3), 7)

    def test_restando_negativos(self):
        self.assertEqual(restar(-5, -10), 5)

    # Pruebas de división
    def test_dividir_positivos(self):
        self.assertEqual(dividir(10, 2), 5)

    def test_dividir_por_cero(self):
        self.assertEqual(dividir(10, 0), "Error: División por cero")

if __name__ == "__main__":
    unittest.main()