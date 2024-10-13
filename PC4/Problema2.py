import random
from pyfiglet import Figlet

def lista_fuente(fuentes_disponibles):
    while True:
        try:
            fuente = input("Ingrese el nombre de la fuente o Enter(Fuente aleatoria): ")
            
            if not fuente:
                fuente_aleatoria = random.choice(fuentes_disponibles)
                print(f"Fuente seleccionada aleatoriamente: {fuente_aleatoria}")
                return fuente_aleatoria

            if fuente in fuentes_disponibles:
                return fuente
            else:
                raise ValueError("La fuente no válida.")

        except ValueError as e:
            print(e)

def solicitar_palabra():
    while True:
        try:
            texto = input("Ingrese el texto que desea convertir en arte ASCII: ")
            
            if not texto.strip():
                raise ValueError("Debe ingresar un texto válido.")
            
            return texto
        
        except ValueError as e:
            print(e)

def main():
    figlet = Figlet()   
    fuentes_disponibles = figlet.getFonts()
    fuente_seleccionada = lista_fuente(fuentes_disponibles)
    figlet.setFont(font=fuente_seleccionada)
    texto = solicitar_palabra()
    print(figlet.renderText(texto))

if __name__ == "__main__":
    main()