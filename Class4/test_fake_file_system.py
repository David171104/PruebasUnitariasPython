"""
Este módulo contiene simular un sistema de archivos que lee y escribe en los mismos y una clase con pruebas
unitarias para verificar su correcto funcionamiento.
"""

import unittest


class FakeFileSystem:
    def __init__(self):
        self.files = {}

    def write(self, filename, content):
        self.files[filename] = content

    def read(self, filename):
        if filename not in self.files:
            raise FileNotFoundError(f"Archivo '{filename}' no encontrado.")
        return self.files[filename]



class FileService:
    """
    Esta clase actúa como una capa de abstracción para interactuar con el sistema de archivos.
    This class acts as an abstraction layer to interact with the file system.
    """

    def __init__(self, file_system):
        """
        Inicializa el servicio de archivos con un sistema de archivos específico.

        :param file_system: Sistema de archivos a utilizar (puede ser real o falso).

        Initializes the file service with a specific file system.
        :param file_system: File system to use (can be real or fake).
        """
        self.file_system = file_system

    def save_file(self, filename, content):
        """
        Guarda contenido en un archivo.

        :param filename: Nombre del archivo.
        :param content: Contenido a guardar.

        Save content to a file.

        :param filename: Name of the file.
        :param content: Content to be saved.
        """
        self.file_system.write(filename, content)

    def load_file(self, filename):
        """
        Carga el contenido de un archivo.

        :param filename: Nombre del archivo.
        :return: Contenido del archivo.

        Upload the contents of a file.

        :param filename: Name of the file.
        :return: File contents.
        """
        return self.file_system.read(filename)

 

class TestFakeFileSystem(unittest.TestCase):
    """
    Clase de pruebas unitarias para verificar el funcionamiento del sistema de archivos falso y el servicio de archivos.
    """

    def setUp(self):
        self.fake_fs = FakeFileSystem()
        self.file_service = FileService(self.fake_fs)


    def test_write_and_read_file(self):
        """
        Verifica que se pueda escribir y leer un archivo correctamente.
        """
        filename = "test.txt"
        content = "Esta es una prueba de escritura en el nuevo archivo"
        self.file_service.save_file(filename, content)

        result = self.file_service.load_file(filename)
        print(f"Probando que se pueda escribir correctamente el contenido {content} en el archivo {filename}, el resultado es: {result}")
        self.assertEqual(result, content)


    def test_read_nonexistent_file(self):
        """
        Verifica que intentar leer un archivo inexistente lance una excepción.
        """
        filename = "no_existe.txt"
        with self.assertRaises(FileNotFoundError):
            self.file_service.load_file(filename)


    def test_overwrite_file(self):
        """
        Verifica que se pueda sobrescribir un archivo existente.
        """
        filename = "test.txt"
        initial_content = "Initial Content"
        updated_content = "Updated Content"

        self.file_service.save_file(filename, initial_content)
        self.file_service.save_file(filename, updated_content)

        result = self.file_service.load_file(filename)
        print(f"Probando que se pueda actualizar o sobreescribir  en el archivo {filename}, el resultado es: {result}")
        self.assertEqual(result, updated_content)



if __name__ == "__main__":
    unittest.main()
