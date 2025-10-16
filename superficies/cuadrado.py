from modules.utils import clear_screen

def perimetro_cuadrado(lado):
    clear_screen()
    print("CALCULAR EL PERIMETRO DE UN CUADRADO (P = 4 x L)")
    print("-" * 50)
    lado = float(input("\nIngrese el valor de uno de los lados del cuadrado: "))
    perimetro = 4 * lado
    print(f"El perimetro del cuadrado es igual a {perimetro:.1f}")