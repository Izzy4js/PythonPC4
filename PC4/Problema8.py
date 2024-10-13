import requests
import sqlite3
from datetime import date

def obtener_precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        precio_usd = float(data["bpi"]["USD"]["rate_float"])
        precio_gbp = float(data["bpi"]["GBP"]["rate_float"])
        precio_eur = float(data["bpi"]["EUR"]["rate_float"])
        return precio_usd, precio_gbp, precio_eur
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None, None, None

def crear_tabla_bitcoin(conn):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS bitcoin (
                fecha TEXT PRIMARY KEY,
                precio_usd REAL,
                precio_gbp REAL,
                precio_eur REAL,
                precio_pen REAL
            )
        """)
        conn.commit()
        print("Tabla 'bitcoin' creada correctamente.")
    except sqlite3.Error as e:
        print(f"Error al crear la tabla 'bitcoin': {e}")

def insertar_datos_bitcoin(conn, precios):
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO bitcoin (fecha, precio_usd, precio_gbp, precio_eur, precio_pen)
            VALUES (?, ?, ?, ?, ?)
        """, (date.today(), *precios))
        conn.commit()
        print("Datos insertados correctamente en la tabla 'bitcoin'.")
    except sqlite3.Error as e:
        print(f"Error al insertar datos en la tabla 'bitcoin': {e}")

def main():
    precio_usd, precio_gbp, precio_eur = obtener_precio_bitcoin()
    tipo_cambio_pen = 3.8
    precio_pen = precio_usd * tipo_cambio_pen
    
    if precio_usd is not None:
        conn = sqlite3.connect("base.db")
        crear_tabla_bitcoin(conn)
        insertar_datos_bitcoin(conn, (precio_usd, precio_gbp, precio_eur, precio_pen))
        conn.close()

        conn = sqlite3.connect("base.db")
        cursor = conn.cursor()
        cursor.execute("SELECT precio_pen, precio_eur FROM bitcoin WHERE fecha = ?", (date.today(),))
        row = cursor.fetchone()
        if row:
            precio_pen_hoy, precio_eur_hoy = row
            costo_pen = 10 * precio_pen_hoy
            costo_eur = 10 * precio_eur_hoy
            print(f"El costo de comprar 10 bitcoins en PEN hoy es: {costo_pen:.2f} PEN")
            print(f"El costo de comprar 10 bitcoins en EUR hoy es: {costo_eur:.2f} EUR")
        else:
            print("No se encontraron datos para hoy en la tabla 'bitcoin'.")

        conn.close()
    else:
        print("No se pudo obtener el precio de Bitcoin.")

if __name__ == "__main__":
    main()