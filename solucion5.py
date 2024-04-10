import os

def registrarTabla(numero):
    if numero < 1 or numero > 10:
        print("El número debe estar entre 1 y 10.")
        return

    with open(f"tabla-{numero}.txt", "w") as archivo:
        for i in range(1, 11):
            archivo.write(f"{numero} x {i} = {numero*i}\n")
    print(f"La tabla de multiplicar del {numero} ha sido guardada en 'tabla-{numero}.txt'")

def mostrarTabla(numero):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            print(f"Tabla de multiplicar del {numero}:")
            for linea in archivo:
                print(linea, end='')
    except FileNotFoundError:
        print(f"El archivo 'tabla-{numero}.txt' no existe.")

def mostrarLineaTabla(numero, linea):
    try:
        with open(f"tabla-{numero}.txt", "r") as archivo:
            lineas = archivo.readlines()
            if len(lineas) >= linea:
                print(lineas[linea - 1], end='')
            else:
                print(f"La línea {linea} no existe en 'tabla-{numero}.txt'.")
    except FileNotFoundError:
        print(f"El archivo 'tabla-{numero}.txt' no existe.")

def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Registrar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de la tabla de multiplicar")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            registrarTabla(numero)
        elif opcion == "2":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            mostrarTabla(numero)
        elif opcion == "3":
            numero = int(input("Ingrese un número entre 1 y 10: "))
            linea = int(input("Ingrese el número de línea a mostrar: "))
            mostrarLineaTabla(numero, linea)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")


if __name__ == "__main__":
    menu()
