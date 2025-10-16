import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def pausar():
    input("\nPresiona enter para continuar......")