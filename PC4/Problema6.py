def contar_lineas_codigo(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            lineas_codigo = 0
            for linea in archivo:
                linea = linea.strip()
                if linea and not linea.startswith('#'):
                    lineas_codigo += 1
            return lineas_codigo
    except FileNotFoundError:
        print(f"El archivo '{ruta_archivo}' no se encontró.")
        return None
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return None

def main():
    ruta_archivo = input("Ingrese la ruta del archivo de código: ")
    loc = contar_lineas_codigo(ruta_archivo)
    if loc is not None:
        print(f"Número de líneas de código (LOC) en '{ruta_archivo}': {loc}")

if __name__ == "__main__":
    main()
