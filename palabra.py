def calcular_puntos(palabra):
    
    abecedario = {chr(i): i - 64 for i in range(65, 91)}  # A=1, B=2, ..., Z=26
    puntos = 0
    for letra in palabra.upper():  # Convertimos a mayúsculas para evitar problemas
        if letra in abecedario:
            puntos += abecedario[letra]
        else:
            print(f"Advertencia: La letra '{letra}' no es válida.")
    return puntos
def main():
    while True:
        # Solicitar al usuario que ingrese una palabra
        palabra = input("Introduce una palabra (o 'salir' para terminar): ").strip()
        
        if palabra.lower() == 'salir':
            print("El programa ha finalizado.")
            break
        
        puntos = calcular_puntos(palabra)
        print(f"El valor de la palabra '{palabra}' es: {puntos} puntos.")
        
        # Comprobamos si la palabra alcanzó los 100 puntos
        if puntos >= 100:
            print(f"¡Felicidades! La palabra '{palabra}' alcanzó los 100 puntos.")
            break
if __name__ == "__main__":
    main()