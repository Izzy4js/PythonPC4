import requests

def precio_bitcoin():
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        precio_usd = float(data["bpi"]["USD"]["rate_float"])
        return precio_usd
    except requests.RequestException as e:
        print(f"Error al obtener el precio de Bitcoin: {e}")
        return None

def main():
    while True:
        try:
            n= float(input("Ingrese la cantidad de bitcoins que posee: "))
            break 
        except ValueError:
            print("Error: Debe ingresar un número válido.")

    precio_usd = precio_bitcoin()

    if precio_usd is not None:
        costo_usd = n * precio_usd
        print(f"El costo actual de {n} bitcoins en USD es: ${costo_usd:,.4f}")
    else:
        print("No se pudo obtener el precio de Bitcoin.")

if __name__ == "__main__":
    main()