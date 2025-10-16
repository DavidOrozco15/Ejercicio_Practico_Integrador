#from utils import clear_screen
def generarFibonacci():
    #clear_screen()
    print("Generador de los primeros 10 números de la serie de Fibonacci")

    a = 0
    b = 1

    cantidad = 10

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


