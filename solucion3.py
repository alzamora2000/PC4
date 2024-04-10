import zipfile
import os

def comprimir_imagen(imagen, nombre_zip):
    with zipfile.ZipFile(nombre_zip, 'w') as archivo_zip:
        archivo_zip.write(imagen)

def descomprimir_zip(nombre_zip, carpeta_destino):
    with zipfile.ZipFile(nombre_zip, 'r') as archivo_zip:
        archivo_zip.extractall(carpeta_destino)

ruta_imagen = 'imagen.jpg'

nombre_zip = 'imagen_comprimida.zip'

comprimir_imagen(ruta_imagen, nombre_zip)

carpeta_destino = 'imagen_descomprimida'


descomprimir_zip(nombre_zip, carpeta_destino)

print("Proceso completado.")
