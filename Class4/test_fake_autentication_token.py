"""
Este módulo contiene simular la respuesta de un servicio de autenticación y una clase con pruebas
unitarias para verificar su correcto funcionamiento.
"""

import unittest


class FakeDatabase:
    def __init__(self):
        self.data = {}

    def insert(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)


def authenticate(username, password, fake_db):
    # Verify credentials 
    stored_password = fake_db.get(username)

    if stored_password == password:
        # Return a token if the credentials are correct
        return "token1"
    return None  

class TestAuthenticationStub(unittest.TestCase):

    def setUp(self):
        self.fake_db = FakeDatabase()
        self.fake_db.insert("user", "secret")

    def test_authenticate_valid_credentials(self):
        # Test case for valid credentials
        username = "user"
        password = "secret"
       
        token = authenticate(username, password, self.fake_db)
        print(f"Probando que la autenticacion de el usuario {username} sea correcta, el resultado es: {token}")
        self.assertEqual(token, "token1")

    def test_authenticate_invalid_credentials(self):
        # Test case for invalid credentials
        username = "user"
        password = "secret_incorrect"
       
        token = authenticate(username, password, self.fake_db)
        self.assertIsNone(token)

    def test_authenticate_nonexistent_user(self):
        # Test case for a non-existent user
        username = "user2"
        password = "secret"
        
        token = authenticate(username, password, self.fake_db)
        print(f"Probando que el usuario  {username} exista, el resultado es: {token}")
        self.assertIsNone(token)


if __name__ == "__main__":
    unittest.main()
