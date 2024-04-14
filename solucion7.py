import requests
import sqlite3

def obtenerDatos(token):
    url = "https://api.apis.net.pe/v2/sunat/tipo-cambio"
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error al obtener los datos del tipo de cambio del año 2023.")
        return None

def crear_tabla_sunat_info(cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                        fecha TEXT PRIMARY KEY,
                        precio_compra INT,
                        precio_venta INT
                    )''')
    print("Tabla 'sunat_info' creada correctamente.")

def insertar_datos_sunat_info(cursor, datos):
    cursor.executemany('''INSERT OR IGNORE INTO sunat_info (fecha, precio_compra, precio_venta) 
                           VALUES (?, ?, ?)''', datos)
    print("Datos insertados correctamente.")

def mostrar_contenido_tabla(cursor):
    cursor.execute("SELECT * FROM sunat_info")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    token = "apis-token-8064.24WcKWHvesgGHUSAvvmRqEjZ5igHQvDa"
    datos_dolar_2023 = obtenerDatos(token)

    if datos_dolar_2023:
        conexion = sqlite3.connect('base.db')
        cursor = conexion.cursor()
        crear_tabla_sunat_info(cursor)
        datos_insertar = [(dia[0], dia[1], dia[2]) for dia in datos_dolar_2023]
        insertar_datos_sunat_info(cursor, datos_insertar)

        conexion.commit()
        #conexion.close()
        print("\nContenido de la tabla 'sunat_info':")
        mostrar_contenido_tabla(cursor)
    else:
        print("No se pudieron obtener los datos del tipo de cambio del año 2023.")
