import requests
import zipfile
import os

def descargar_imagen(url, nombre_archivo):
    try:
        response = requests.get(url, stream=True)
        
        if response.status_code == 200:
            with open(nombre_archivo, 'wb') as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
            print(f"Imagen descargada correctamente como '{nombre_archivo}'")
        else:
            print(f"Error al descargar la imagen: {response.status_code}")
    except requests.RequestException as e:
        print(f"Hubo un problema al descargar la imagen: {e}")

def crear_zip(nombre_imagen, nombre_zip):
    try:
        with zipfile.ZipFile(nombre_zip, 'w') as zipf:
            zipf.write(nombre_imagen)
        print(f"Archivo ZIP '{nombre_zip}' creado correctamente.")
    except Exception as e:
        print(f"Error al crear el archivo ZIP: {e}")

def descomprimir_zip(nombre_zip, directorio_destino):
    try:
        with zipfile.ZipFile(nombre_zip, 'r') as zip_ref:
            zip_ref.extractall(directorio_destino)
        print(f"Archivo ZIP '{nombre_zip}' descomprimido correctamente en '{directorio_destino}'")
    except Exception as e:
        print(f"Error al descomprimir el archivo ZIP: {e}")

def main():
    url_imagen = "https://images.unsplash.com/photo-1546527868-ccb7ee7dfa6a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    
    nombre_imagen = "imagen_descargada.jpg"
    nombre_zip = "imagen_comprimida.zip"
    directorio_destino = "descomprimido"

    descargar_imagen(url_imagen, nombre_imagen)
    
    crear_zip(nombre_imagen, nombre_zip)
    
    if not os.path.exists(directorio_destino):
        os.makedirs(directorio_destino)
    
    descomprimir_zip(nombre_zip, directorio_destino)

if __name__ == "__main__":
    main()