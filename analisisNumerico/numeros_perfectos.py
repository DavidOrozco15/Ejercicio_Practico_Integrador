from modules.utils import pausar, clear_screen
def obtenerDivisores(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:  
            suma += i
    return suma

def esPerfecto(num):
    return obtenerDivisores(num) == num

clear_screen()
num = int(input("Ingresa un número para verificar si es perfecto: "))

if esPerfecto(num):
    print(f"{num} es un número perfecto.")
    pausar()
else:
    print(f"{num} no es un número perfecto.")
    pausar()