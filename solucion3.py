import zipfile
import os

# Función para comprimir una imagen en un archivo zip
def comprimir_imagen(imagen, nombre_zip):
    with zipfile.ZipFile(nombre_zip, 'w') as archivo_zip:
        archivo_zip.write(imagen)

# Función para descomprimir un archivo zip
def descomprimir_zip(nombre_zip, carpeta_destino):
    with zipfile.ZipFile(nombre_zip, 'r') as archivo_zip:
        archivo_zip.extractall(carpeta_destino)

# Ruta de la imagen que quieres comprimir
ruta_imagen = 'imagen.jpg'

# Nombre del archivo zip
nombre_zip = 'imagen_comprimida.zip'

# Comprimir la imagen en un archivo zip
comprimir_imagen(ruta_imagen, nombre_zip)

# Carpeta donde se descomprimirá el archivo zip
carpeta_destino = 'imagen_descomprimida'

# Descomprimir el archivo zip
descomprimir_zip(nombre_zip, carpeta_destino)

print("Proceso completado.")
