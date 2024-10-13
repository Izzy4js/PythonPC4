import requests
import sqlite3

def obtener_datos_mes(mes):
    url = f"https://api.apis.net.pe/v2/tipo-cambio-sunat?month={mes}&year=2023"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data
        else:
            print(f"No se encontraron datos para el mes {mes} del año 2023.")
            return None
    else:
        print(f"No se pudo obtener la información para el mes {mes} del año 2023.")
        return None

def crear_tabla():
    try:
        with sqlite3.connect('base.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS sunat_info (
                                fecha TEXT PRIMARY KEY,
                                compra FLOAT,
                                venta FLOAT
                                )''')
            conn.commit()
        print("Tabla 'sunat_info' creada correctamente.")
    except sqlite3.Error as e:
        print("Error al crear la tabla:", e)

def insertar_datos_mes(mes, datos_mes):
    try:
        with sqlite3.connect('base.db') as conn:
            cursor = conn.cursor()
            for registro in datos_mes:
                fecha = registro['fecha']
                compra = registro['compra']
                venta = registro['venta']
                cursor.execute('''INSERT OR IGNORE INTO sunat_info (fecha, compra, venta) VALUES (?, ?, ?)''', (fecha, compra, venta))
            conn.commit()
        print(f"Datos del mes {mes} insertados correctamente en la tabla 'sunat_info'.")
    except sqlite3.Error as e:
        print("Error al insertar datos en la tabla:", e)

def mostrar_contenido_tabla():
    try:
        with sqlite3.connect('base.db') as conn:
            cursor = conn.cursor()
            cursor.execute('''SELECT * FROM sunat_info''')
            rows = cursor.fetchall()
            print("Contenido de la tabla 'sunat_info':")
            for row in rows:
                print(row)
    except sqlite3.Error as e:
        print("Error al mostrar contenido de la tabla:", e)

crear_tabla()

for mes in range(1, 13):
    datos_mes = obtener_datos_mes(mes)
    if datos_mes:
        insertar_datos_mes(mes, datos_mes)

mostrar_contenido_tabla()