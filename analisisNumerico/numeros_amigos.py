def obtenerDivisores(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:  
            suma += i
    return suma

def sonAmigos(num1, num2):
    # Compara 
    return obtenerDivisores(num1) == num2 and obtenerDivisores(num2) == num1

print("---IDENTIFICADOR DE NUMEROS PRIMOS---")
num1 = int(input("Ingresa el primer número: "))
num2 = int(input("Ingresa el segundo número: "))

if sonAmigos(num1, num2):
    print(f"{num1} y {num2} son números amigos.")
else:
    print(f"{num1} y {num2} no son números amigos.")

