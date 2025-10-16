from .cuadrado import area_cuadrado
from .triangulo import area_triangulo
from .poligono import area_poligono
from .circulo import area_circulo

def mostrar_menu_areas():
    """Muestra el menú de cálculo de áreas."""
    print("\n===== CÁLCULO DE ÁREAS =====")
    print("1. Área de un cuadrado")
    print("2. Área de un triángulo")
    print("3. Área de un polígono")
    print("4. Área de un círculo")
    print("5. Volver al menú principal")
    return input("Seleccione una opción (1-5): ")

def menu_areas():
    """Función para manejar el menú de áreas."""
    while True:
        opcion = mostrar_menu_areas()
        if opcion == "1":
            try:
                lado = float(input("Ingrese el lado del cuadrado: "))
                area = area_cuadrado(lado)
                print(f"El área del cuadrado es: {area}")
            except ValueError:
                print("Entrada no válida. Debe ingresar un número.")
        elif opcion == "2":
            try:
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                area = area_triangulo(base, altura)
                print(f"El área del triángulo es: {area}")
            except ValueError:
                print("Entrada no válida. Debe ingresar números.")
        elif opcion == "3":
            try:
                num_vertices = int(input("Ingrese el número de vértices del polígono: "))
                if num_vertices < 3:
                    print("Un polígono debe tener al menos 3 vértices.")
                    continue
                vertices = []
                for i in range(num_vertices):
                    x = float(input(f"Ingrese la coordenada x del vértice {i+1}: "))
                    y = float(input(f"Ingrese la coordenada y del vértice {i+1}: "))
                    vertices.append((x, y))
                area = area_poligono(vertices)
                print(f"El área del polígono es: {area}")
            except ValueError:
                print("Entrada no válida. Debe ingresar números.")
        elif opcion == "4":
            try:
                radio = float(input("Ingrese el radio del círculo: "))
                area = area_circulo(radio)
                print(f"El área del círculo es: {area}")
            except ValueError:
                print("Entrada no válida. Debe ingresar un número.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente nuevamente.")
