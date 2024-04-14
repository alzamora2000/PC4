import requests
import sqlite3
from datetime import date

def obtener_datos_bitcoin():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()["bpi"]
    else:
        print("Error al obtener los datos del precio de Bitcoin.")
        return None

def obtener_tipo_cambio_pen(moneda):
    url = f"https://api.apis.net.pe/v1/tipo-cambio/{date.today().year}"
    response = requests.get(url)
    if response.status_code == 200:
        datos = response.json()
        if moneda in datos:
            return datos[moneda]["venta"]
        else:
            print(f"No se encontró el tipo de cambio para la moneda {moneda}.")
            return None
    else:
        print("Error al obtener los datos del tipo de cambio del PEN.")
        return None

def crear_tabla_bitcoin(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS bitcoin (
                        fecha DATE PRIMARY KEY,
                        precio_usd REAL,
                        precio_gbp REAL,
                        precio_eur REAL,
                        precio_pen REAL
                    )''')
    print("Tabla 'bitcoin' creada correctamente.")

def insertar_datos_bitcoin(cursor, datos):
    cursor.execute('''INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen) 
                      VALUES (?, ?, ?, ?, ?)''', datos)
    print("Datos insertados correctamente.")

def consultar_precio_bitcoin(cursor, moneda):
    cursor.execute(f"SELECT precio_{moneda.lower()} FROM bitcoin ORDER BY fecha DESC LIMIT 1")
    precio_bitcoin = cursor.fetchone()[0]
    return precio_bitcoin

if __name__ == "__main__":
    # Obtener datos del precio de Bitcoin
    datos_bitcoin = obtener_datos_bitcoin()

    if datos_bitcoin:
        # Obtener tipo de cambio PEN para USD, GBP y EUR
        tipo_cambio_usd = obtener_tipo_cambio_pen("USD")
        tipo_cambio_gbp = obtener_tipo_cambio_pen("GBP")
        tipo_cambio_eur = obtener_tipo_cambio_pen("EUR")

        if tipo_cambio_usd and tipo_cambio_gbp and tipo_cambio_eur:
            # Conectar a la base de datos
            conexion = sqlite3.connect('base.db')
            cursor = conexion.cursor()

            # Crear tabla 'bitcoin'
            crear_tabla_bitcoin(cursor)

            # Obtener fecha actual
            fecha_actual = date.today()

            # Insertar datos en la tabla 'bitcoin'
            insertar_datos_bitcoin(cursor, (fecha_actual, 
                                             datos_bitcoin["USD"]["rate_float"], 
                                             datos_bitcoin["GBP"]["rate_float"], 
                                             datos_bitcoin["EUR"]["rate_float"], 
                                             datos_bitcoin["USD"]["rate_float"] / tipo_cambio_usd))

            # Guardar cambios y cerrar conexión
            conexion.commit()
            conexion.close()

            # Consultar el precio de Bitcoin en PEN y EUR
            precio_bitcoin_pen = consultar_precio_bitcoin(cursor, "pen")
            precio_bitcoin_eur = consultar_precio_bitcoin(cursor, "eur")

            # Calcular precio de comprar 10 bitcoins en PEN y EUR
            precio_compra_10_bitcoins_pen = precio_bitcoin_pen * 10
            precio_compra_10_bitcoins_eur = precio_bitcoin_eur * 10

            print(f"Precio de comprar 10 bitcoins en PEN: {precio_compra_10_bitcoins_pen:.2f} PEN")
            print(f"Precio de comprar 10 bitcoins en EUR: {precio_compra_10_bitcoins_eur:.2f} EUR")
        else:
            print("No se pudieron obtener los tipos de cambio del PEN para USD, GBP y EUR.")
    else:
        print("No se pudieron obtener los datos del precio de Bitcoin.")
