from modules.utils import pausar, clear_screen

def obtenerDivisores(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    return suma

def esPerfecto():
    clear_screen()
    try:
        num = int(input("Ingresa un número para verificar si es perfecto: "))
        if obtenerDivisores(num) == num:
            print(f"{num} es un número perfecto.")
        else:
            print(f"{num} no es un número perfecto.")
        pausar()
    except ValueError:
        print("Entrada no válida. Debe ingresar un número entero.")
        pausar()
