# Datos de ejemplo de precios de Bitcoin (fecha, precio)
import requests
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
response.raise_for_status()
data = response.json()
#print(data)
datos_bitcoin = [
    #("2024-04-01", 45000),
    #("2024-04-02", 45500),
    #("2024-04-03", 46000),
    data
    # Agrega más datos aquí
]

# Nombre del archivo de texto donde se almacenarán los datos
nombre_archivo = "precios_bitcoin.txt"

# Escribir los datos en el archivo de texto
with open(nombre_archivo, "w") as archivo:
    for data in datos_bitcoin:
        archivo.write(f"{data}: ${data}\n")

print(f"Los datos de precios de Bitcoin se han almacenado en '{nombre_archivo}'")
