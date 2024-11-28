#Operaciones de la calculadora

def suma(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b


def resta(a, b):
    return a - b


def multiplicacion(a, b):
    return a * b


def division(dividendo, divisor):
   
    if divisor == 0:
        return "Error: División por cero"
    elif divisor < 0:
        return -dividendo / divisor
    else:
        return dividendo / divisor


def exponente(base, potencia):
    
    return base ** potencia
