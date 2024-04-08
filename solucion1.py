import requests

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()
        data = response.json()
        #print(data)
        return float(data["bpi"]["USD"]["rate"].replace(",", ""))
    except requests.RequestException as e:
        print("Error al realizar la solicitud:", e)
        return None
    except KeyError:
        print("Error: No se pudo encontrar el precio en la respuesta JSON.")
        return None

def main():
    bitcoins = input("Ingrese la cantidad de bitcoins que posee: ")
    try:
        bitcoins = float(bitcoins)
    except ValueError:
        print("Error: Por favor, ingrese un número válido de bitcoins.")
        return

    precio_bitcoin = obtener_precio_bitcoin()
    if precio_bitcoin is not None:
        costo_en_usd = bitcoins * precio_bitcoin
        print(f"El costo actual de {bitcoins} bitcoins es: ${costo_en_usd:,.4f}")

if __name__ == "__main__":
    main()
