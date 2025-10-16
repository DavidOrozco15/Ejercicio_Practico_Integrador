def obtenerDivisores(num):
    suma = 0
    for i in range(1, num):
        if num % i == 0:  
            suma += i
    return suma

def esPerfecto(num):
    return obtenerDivisores(num) == num

num = int(input("Ingresa un número para verificar si es perfecto: "))

if esPerfecto(num):
    print(f"{num} es un número perfecto.")
else:
    print(f"{num} no es un número perfecto.")