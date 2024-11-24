"""
Este módulo contiene una verificacion de una función que envía un correo electrónico con los parametros
adecuados y una clase con pruebas unitarias para verificar su correcto funcionamiento.
"""

import unittest
from unittest.mock import MagicMock


class MyService:
    def verified_data_parameters_from_api(self, email, message):
        if email is not None and message is not None:
            print("Datos correctos")
            return True 
        else:
            print("Datos incorrectos")
            return False 
    
        




class TestMyService(unittest.TestCase):
    def test_verified_data_parameters_from_api_called(self):
        # Mock: simulate the answer and verify the call
        email = "user@mail.com"
        message = "prueba correos"

        service = MyService()
        service.verified_data_parameters_from_api = MagicMock(return_value=True)

        result = service.verified_data_parameters_from_api(email, message)
        service.verified_data_parameters_from_api.assert_called_once_with(email, message)
        print(f"Probando que los parametros de {email} y {message} sean correctos, el resultado es: {result}")
        self.assertTrue(result)

       
    def test_verified_data_parameters_from_api_invalid(self):
        # Mock: simulate the answer and verify the call
        email = None
        message = None

        service = MyService()
        service.verified_data_parameters_from_api = MagicMock(return_value=False)

        result = service.verified_data_parameters_from_api(email, message)
        service.verified_data_parameters_from_api.assert_called_once_with(email, message)
        print(f"Probando que los parametros de {email} y {message} sean incorrectos, el resultado es: {result}")
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
