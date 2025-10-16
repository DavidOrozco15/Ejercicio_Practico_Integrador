from modules.utils import pausar, clear_screen

def obtenerDivisores(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:
            suma += i
    return suma

def sonAmigos():
    clear_screen()
    print("---IDENTIFICADOR DE NUMEROS AMIGOS---")
    try:
        num1 = int(input("Ingresa el primer número: "))
        num2 = int(input("Ingresa el segundo número: "))
        if obtenerDivisores(num1) == num2 and obtenerDivisores(num2) == num1:
            print(f"{num1} y {num2} son números amigos.")
        else:
            print(f"{num1} y {num2} no son números amigos.")
        pausar()
    except ValueError:
        print("Entrada no válida. Debe ingresar números enteros.")
        pausar()

