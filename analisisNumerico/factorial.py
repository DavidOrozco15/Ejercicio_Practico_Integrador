def calcularFactorial(num):
    # Inicializamos el resultado como 1
    resultado = 1
    
    # Multiplicamos todos los números desde 1 hasta num
    for i in range(1, num + 1):
        resultado *= i
        
    return resultado

# Pedimos al usuario que ingrese un número
num = int(input("Ingresa un número para calcular su factorial: "))

# Calculamos el factorial
print(f"El factorial de {num} es {calcularFactorial(num)}")