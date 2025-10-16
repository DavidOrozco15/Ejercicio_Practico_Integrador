from modules.utils import pausar, clear_screen

def calcularFactorial():
    clear_screen()
    try:
        num = int(input("Ingresa un número para calcular su factorial: "))
        if num < 0:
            print("El factorial no está definido para números negativos.")
            pausar()
            return
        resultado = 1
        # Multiplicamos todos los números desde 1 hasta num
        for i in range(1, num + 1):
            resultado *= i
        print(f"El factorial de {num} es {resultado}")
        pausar()
    except ValueError:
        print("Entrada no válida. Debe ingresar un número entero.")
        pausar()
