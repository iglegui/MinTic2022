def conteoLetra(frase1, letra1): 
    totalConteo = frase1.count(letra1)
    return totalConteo


frase = str(input("Ingrese una frase: "))
letra = str(input("Ingrese una letra: "))

print(f"El número de veces que aparece la {letra} en la frase es: " + str(conteoLetra(frase, letra)))