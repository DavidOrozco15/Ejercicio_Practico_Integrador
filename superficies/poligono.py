from modules.utils import clear_screen


def perimetro_poligono(n, lados):
    clear_screen()
    print("CALCULAR EL PERIMETRO DE UN POLÍGONO REGULAR (P = n x L)")
    print("-" * 50)
    n = int(input("\nIngrese el número de lados que tiene el polígono: "))
    lados = float("Ingrese el valor de uno de los lados del polígono: ")
    per_poligono_regular = n * lados
    print(f"El perimetro del polígono es igual a {per_poligono_regular}")