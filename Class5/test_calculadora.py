"""
Este módulo contiene una clase con pruebas unitarias para verificar su correcto funcionamiento.
"""

import unittest
from calculadora import suma, resta, multiplicacion, division, exponente


class TestCalculadora(unittest.TestCase):

   
    def test_suma_positivos(self):
        self.assertEqual(suma(3, 5), 8)


    def test_suma_negativos(self):
        self.assertEqual(suma(-3, -7), -10)


    def test_suma_positivo_negativo(self):
        self.assertEqual(suma(10, -5), 5)


    def test_suma_ceros(self):
        self.assertEqual(suma(0, 0), 0)


    def test_suma_decimales(self):
        self.assertEqual(suma(2.5, 3.5), 6.0)

   

    def test_resta_positivos(self):
        self.assertEqual(resta(10, 3), 7)


    def test_resta_negativos(self):
        self.assertEqual(resta(-10, -5), -5)


    def test_resta_positivo_negativo(self):
        self.assertEqual(resta(10, -5), 15)



    def test_multiplicacion(self):
        self.assertEqual(multiplicacion(4, 5), 20)
        self.assertEqual(multiplicacion(-4, 5), -20)
        self.assertEqual(multiplicacion(0, 5), 0)


    def test_division_por_cero(self):
        self.assertEqual(division(10, 0), "Error: División por cero")


    def test_division_positiva(self):
        self.assertEqual(division(10, 2), 5.0)


    def test_division_negativa(self):
        self.assertEqual(division(10, -2), 5.0)

    def test_division_invalidos(self):
        with self.assertRaises(TypeError):
            division("10", 2)
        with self.assertRaises(TypeError):
            division(10, "2")
        with self.assertRaises(TypeError):
            division(None, 2)


    def test_division_negativo(self):
        self.assertEqual(division(-10, 2), -5.0)



    def test_exponente(self):
        self.assertEqual(exponente(2, 3), 8)
        self.assertEqual(exponente(5, 0), 1)
        self.assertEqual(exponente(2, -2), 0.25)

if __name__ == "__main__":
    unittest.main()


