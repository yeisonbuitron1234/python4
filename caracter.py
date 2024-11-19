def comparar_cadenas():

    cadena1 = input("Ingresa la primera cadena: ")
    cadena2 = input("Ingresa la segunda cadena: ")

    if len(cadena1) != len(cadena2):
        print("Error: Las cadenas deben tener la misma longitud.")
        return

    diferencias = []
    for i in range(len(cadena1)):
        if cadena1[i] != cadena2[i]:
            diferencias.append((i, cadena1[i], cadena2[i]))

    if diferencias:
        print("\nDiferencias encontradas:")
        for pos, char1, char2 in diferencias:
            print(f"Posición {pos}: '{char1}' en la primera cadena, '{char2}' en la segunda cadena.")
    else:
        print("\nLas cadenas son idénticas.")
comparar_cadenas()