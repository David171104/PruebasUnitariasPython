import pytest
from unittest.mock import patch
import math

def sort_words(text):
    """
    Reciba una cadena de texto y devuelva la misma con las palabras ordenadas
    """
    #text = input("Por favor, introduce una cadena de texto o varias separadas por un espacio: ")
    words = text.split()
    words.sort()
    return ' '.join(words)

@pytest.mark.parametrize("text, expected_output", [
    ("things rocket pride", "pride rocket things"),  #random order
    ("wolfs football rocket", "football rocket wolfs")  
])
def test_sort_words_random_order(text, expected_output):
    assert sort_words(text) == expected_output


@pytest.mark.parametrize("text, expected_output", [
    ("rocket things rocket", "rocket rocket things"),  
    ("football football wolfs wolfs", "football football wolfs wolfs")  
])
def test_sort_words_with_duplicates(text, expected_output):
    assert sort_words(text) == expected_output

def test_sort_words_empty():
    assert sort_words("") == ""

