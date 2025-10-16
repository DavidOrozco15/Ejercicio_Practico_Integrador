from analisisNumerico.fibonacci import generarFibonacci
def menuAnalisis():
    while True:
        print("---ANALISIS NUMERICO---")
        print("\n1. Factorial")
        print("2. Fibonacci")
        print("3. Numeros Amigos")
        print("4. Numeros Perfectos")
        print("0. Volver")
        
        opcion = int(input("\nIngrese una opcion: "))
        match opcion:
            case 1:
                pass
            case 2:
                generarFibonacci()
            case 3:
                pass
            case 4:
                pass
            case 0:
                pass
            case _:
                pass