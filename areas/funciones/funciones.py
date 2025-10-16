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

def area_poligono(vertices):
    """
    Calcula el área de un polígono usando la fórmula de Gauss (shoelace).

    Parámetros:
    vertices (list of tuples): Lista de tuplas (x, y) representando los vértices del polígono en orden.

    Retorna:
    float: El área del polígono.
    """
    if len(vertices) < 3:
        raise ValueError("Un polígono debe tener al menos 3 vértices.")
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0
