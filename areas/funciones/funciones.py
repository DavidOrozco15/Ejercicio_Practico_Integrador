import math

def area_cuadrado(lado):
    """
    Calcula el área de un cuadrado.

    Parámetros:
    lado (float): La longitud del lado del cuadrado.

    Retorna:
    float: El área del cuadrado.
    """
    return lado ** 2

def area_rectangulo(largo, ancho):
    """
    Calcula el área de un rectángulo.

    Parámetros:
    largo (float): La longitud del rectángulo.
    ancho (float): El ancho del rectángulo.

    Retorna:
    float: El área del rectángulo.
    """
    return largo * ancho

def area_circulo(radio):
    """
    Calcula el área de un círculo.

    Parámetros:
    radio (float): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    return math.pi * radio ** 2

def area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.

    Parámetros:
    base (float): La base del triángulo.
    altura (float): La altura del triángulo.

    Retorna:
    float: El área del triángulo.
    """
    return (base * altura) / 2
