def contarLineas(archivo):
    try:
        if not archivo.endswith(".py"):
            print("El archivo no es un archivo de Python (.py)")
            return

        with open(archivo, "r") as f:
            lineas_codigo = 0
            for linea in f:
                linea = linea.strip()
                if linea and not linea.startswith("#"):
                    lineas_codigo += 1
        print(f"El archivo '{archivo}' tiene {lineas_codigo} líneas de código.")

    except FileNotFoundError:
        print("Ruta de archivo inválida.")


if __name__ == "__main__":
    ruta_archivo = input("Ingrese la ruta del archivo .py: ")
    contarLineas(ruta_archivo)
