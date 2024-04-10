import requests
response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
response.raise_for_status()
data = response.json()
#print(data)
datos_bitcoin = [
    data
]

nombre_archivo = "precios_bitcoin.txt"


with open(nombre_archivo, "w") as archivo:
    for data in datos_bitcoin:
        archivo.write(f"{data}: ${data}\n")

print(f"Los datos de precios de Bitcoin se han almacenado en '{nombre_archivo}'")
