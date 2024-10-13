import os

class TablasMultiplicar:

    def __init__(self):
        self.ruta = os.getcwd()

    def generar_tabla(self, n):
        nombre_fichero = f"tabla-{n}.txt"
        try:
            with open(nombre_fichero, 'w') as fichero:
                for i in range(1, 11):
                    fichero.write(f"{n} x {i} = {n * i}\n")
            print(f"Tabla del {n} generada correctamente en '{nombre_fichero}'")
        except Exception as e:
            print(f"Error al generar la tabla: {e}")

    def mostrar_tabla(self, n):
        nombre_fichero = f"tabla-{n}.txt"
        try:
            with open(nombre_fichero, 'r') as fichero:
                contenido = fichero.read()
                print(f"Tabla del {n}:\n{contenido}")
        except FileNotFoundError:
            print(f"El fichero '{nombre_fichero}' no existe.")
        except Exception as e:
            print(f"Error al leer la tabla: {e}")

    def mostrar_linea(self, n, m):
        nombre_fichero = f"tabla-{n}.txt"
        try:
            with open(nombre_fichero, 'r') as fichero:
                lineas = fichero.readlines()
                if 1 <= m <= 10:
                    print(f"Línea {m} de la tabla del {n}: {lineas[m - 1].strip()}")
                else:
                    print("El número de línea debe estar entre 1 y 10.")
        except FileNotFoundError:
            print(f"El fichero '{nombre_fichero}' no existe.")
        except Exception as e:
            print(f"Error al leer la línea de la tabla: {e}")

def menu():
    tablas = TablasMultiplicar()

    while True:
        print("\n---- Menú ----")
        print("1. Generar tabla de multiplicar")
        print("2. Mostrar tabla de multiplicar")
        print("3. Mostrar línea de una tabla de multiplicar")
        print("4. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                n = int(input("Ingrese un número entre 1 y 10 para generar su tabla: "))
                if 1 <= n <= 10:
                    tablas.generar_tabla(n)
                else:
                    print("El número debe estar entre 1 y 10.")
            elif opcion == 2:
                n = int(input("Ingrese un número entre 1 y 10 para mostrar su tabla: "))
                if 1 <= n <= 10:
                    tablas.mostrar_tabla(n)
                else:
                    print("El número debe estar entre 1 y 10.")
            elif opcion == 3:
                n = int(input("Ingrese un número entre 1 y 10 para la tabla: "))
                if 1 <= n <= 10:
                    m = int(input("Ingrese un número entre 1 y 10 para la línea: "))
                    if 1 <= m <= 10:
                        tablas.mostrar_linea(n, m)
                    else:
                        print("El número de línea debe estar entre 1 y 10.")
                else:
                    print("El número debe estar entre 1 y 10.")
            elif opcion == 4:
                print("Saliendo del programa.")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido.")

if __name__ == "__main__":
    menu()
