import requests

def descargar_fichero(url, nombre_archivo):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(nombre_archivo, 'w') as file:
                file.write(response.text)
            print(f"Fichero '{nombre_archivo}' descargado correctamente.")
        else:
            print(f"Error al descargar el fichero: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error al descargar el fichero: {e}")

def procesar_temperaturas(nombre_fichero):
    temperaturas = []

    try:
        with open(nombre_fichero, 'r') as file:
            for linea in file:
                fecha, temp = linea.strip().split(',')
                temperaturas.append(float(temp))

        temp_max = max(temperaturas)
        temp_min = min(temperaturas)
        temp_promedio = sum(temperaturas) / len(temperaturas)

        return temp_promedio, temp_max, temp_min

    except FileNotFoundError:
        print(f"Error: El fichero '{nombre_fichero}' no se encontró.")
        return None
    except Exception as e:
        print(f"Error al procesar el fichero: {e}")
        return None

def escribir_resumen(nombre_fichero_resumen, temp_promedio, temp_max, temp_min):
    try:
        with open(nombre_fichero_resumen, 'w') as file:
            file.write(f"Temperatura promedio: {temp_promedio:.2f}°C\n")
            file.write(f"Temperatura máxima: {temp_max:.2f}°C\n")
            file.write(f"Temperatura mínima: {temp_min:.2f}°C\n")
        print(f"Fichero de resumen '{nombre_fichero_resumen}' creado correctamente.")
    except Exception as e:
        print(f"Error al escribir el fichero de resumen: {e}")

def main():
    url_fichero = "https://raw.githubusercontent.com/gdelgador/ProgramacionPython202407/main/Modulo4/src/temperaturas.txt"
    nombre_fichero = "temperaturas.txt"
    nombre_fichero_resumen = "resumen_temperaturas.txt"

    descargar_fichero(url_fichero, nombre_fichero)

    resultado = procesar_temperaturas(nombre_fichero)
    
    if resultado:
        temp_promedio, temp_max, temp_min = resultado
        escribir_resumen(nombre_fichero_resumen, temp_promedio, temp_max, temp_min)

if __name__ == "__main__":
    main()
