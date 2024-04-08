from pyfiglet import Figlet
import random

def seleccionar_fuente():
    figlet = Figlet()
    fuentes_disponibles = figlet.getFonts()
    fuente = input("Ingrese el nombre de la fuente a utilizar (o presione Enter para seleccionar una al azar): ")
    if fuente == "":
        fuente = random.choice(fuentes_disponibles)
    elif fuente not in fuentes_disponibles:
        print("La fuente ingresada no está disponible. Seleccionando una al azar.")
        fuente = random.choice(fuentes_disponibles)
    return fuente

def main():
    fuente = seleccionar_fuente()
    figlet = Figlet(font=fuente)
    texto = input("Ingrese el texto a imprimir: ")
    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()
