import zipfile
import os

def comprimirImagen(imagen, nombre_zip):
    with zipfile.ZipFile(nombre_zip, 'w') as archivo_zip:
        archivo_zip.write(imagen)

def descomprimirZip(nombre_zip, carpeta_destino):
    with zipfile.ZipFile(nombre_zip, 'r') as archivo_zip:
        archivo_zip.extractall(carpeta_destino)

ruta_imagen = 'imagen.jpg'

nombre_zip = 'imagen_comprimida.zip'

comprimirImagen(ruta_imagen, nombre_zip)

carpeta_destino = 'imagen_descomprimida'


descomprimirZip(nombre_zip, carpeta_destino)

print("Proceso completado.")
