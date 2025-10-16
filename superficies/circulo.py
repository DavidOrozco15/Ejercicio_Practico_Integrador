# from utils import clear_screen

def perimetro_circulo(radio):
    # clear_screen()
    print("CALCULAR PERIMETRO DE UN CIRCULO (P = 2πr)")
    print("-" * 50)
    radio = float(input("\nIngrese el valor del radio: "))
    per_circulo = 2 * 3.1416 * radio
    print(f"El perimetro del circulo es igual a {per_circulo:.2f}")