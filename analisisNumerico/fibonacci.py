from modules.utils import pausar, clear_screen

def generarFibonacci():
    clear_screen()
    try:
        cantidad = int(input("Ingresa la cantidad de números de Fibonacci a generar: "))
        if cantidad <= 0:
            print("La cantidad debe ser un número positivo.")
            pausar()
            return
        print("Generador de la serie de Fibonacci")

        a = 0
        b = 1

        print("La serie de Fibonacci es: ", end="")

        for i in range(cantidad):
            if i == 0:
                print(a, end="")
            elif i == 1:
                print(f", {b}", end="")
            else:
                siguiente = a + b
                print(f", {siguiente}", end="")
                a = b
                b = siguiente

        print()  # New line
        pausar()
    except ValueError:
        print("Entrada no válida. Debe ingresar un número entero.")
        pausar()

