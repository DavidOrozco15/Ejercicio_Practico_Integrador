from analisisNumerico.fibonacci import generarFibonacci
from analisisNumerico.factorial import calcularFactorial
from analisisNumerico.numeros_amigos import sonAmigos
from analisisNumerico.numeros_perfectos import esPerfecto
from analisisNumerico.pi import valorPi

def menuAnalisis():
    while True:
        print("---ANALISIS NUMERICO---")
        print("\n1. Factorial")
        print("2. Fibonacci")
        print("3. Numeros Amigos")
        print("4. Numeros Perfectos")
        print("5. Pi")
        print("0. Volver")
        
        opcion = int(input("\nIngrese una opcion: "))
        match opcion:
            case 1:
                calcularFactorial()
            case 2:
                generarFibonacci()
            case 3:
                sonAmigos()
            case 4:
                esPerfecto()
            case 5:
                valorPi()
            case 0:
                pass
            case _:
                pass