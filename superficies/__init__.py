from superficies.cuadrado import perimetro_cuadrado
from superficies.circulo import perimetro_circulo
from superficies.poligono import perimetro_poligono
from superficies.triangulo import perimetro_triangulo
from modules.utils import pausar, clear_screen

def menu_perimetros():
    clear_screen()
    print("CALCULADORA DE PERIMETROS")
    print("-" * 50)
    print("\n1. Cuadrados")
    print("2. Circulos")
    print("3. Polígonos")
    print("4. Triangulos")
    print("0. Volver al menú principal")
    opcion = input("Ingrese una opción (0-4)")
    
    while True:
        match opcion:
            case "1":
                perimetro_cuadrado()
                pausar()
            case "2":
                perimetro_circulo()
                pausar()
            case "3":
                perimetro_poligono()
                pausar()
            case "4":
                perimetro_triangulo()
                pausar()
            case "0":
                break
            case _:
                print("\nOpción no válida. Intente nuevamente.\n")
                pausar()