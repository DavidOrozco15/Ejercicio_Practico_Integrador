def obtenerDivisores(num):
    # Devuelve la suma de los divisores de un número (sin contar el mismo número)
    suma = 0
    for i in range(1, num):
        if num % i == 0:  # Si i es divisor de num
            suma += i
    return suma

def esPerfecto(num):
    # Verifica si la suma de los divisores de un número es igual al propio número
    return obtenerDivisores(num) == num

# Pedimos al usuario que ingrese un número
num = int(input("Ingresa un número para verificar si es perfecto: "))

# Verificamos si el número es perfecto
if esPerfecto(num):
    print(f"{num} es un número perfecto.")
else:
    print(f"{num} no es un número perfecto.")