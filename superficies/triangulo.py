# from utils import clear_screen

def perimetro_triangulo(lado1, lado2, lado3):
    # clear_screen()
    print("CALCULAR EL PERIMETRO DE UN TRIANGULO (P = L1 + L2 + L3)")
    print("-" * 50)
    lado1 = float(input("Ingrese el valor del primer lado: "))
    lado2 = float(input("Ingrese el valor del segundo lado: "))
    lado3 = float(input("Ingrese el valor del tercer lado: "))
    per_triangulo = lado1 + lado2 + lado3
    print(f"El perimetro del triangulo es igual a {per_triangulo}")