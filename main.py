def mostrar_menu_principal():
    """Muestra el menú principal de la calculadora."""
    from modules.utils import clear_screen
    clear_screen()
    print("\n===== CALCULADORA MATEMÁTICA =====")
    print("1. Cálculo de áreas")
    print("2. Cálculo de superficies")
    print("3. Análisis numérico")
    print("4. Salir")

    return input("Seleccione una opción (1-4): ")

def main():
    """Función principal del programa."""
    while True:
        opcion = mostrar_menu_principal()
        if opcion == "1":
            from areas.menu import menu_areas
            menu_areas()
        elif opcion == "2":
            from superficies import menu_perimetros
            menu_perimetros()
        elif opcion == "3":
            from analisisNumerico import menuAnalisis
            menuAnalisis()
        elif opcion == "4":
            print("¡Gracias por usar la calculadora matemática!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()