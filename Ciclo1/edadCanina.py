def edadCanina(edadPerruna):

    if edadPerruna <= 0:
        print("Debe ingresar un número MAYOR a cero.")
    elif edadPerruna <= 2:
        edadPerro = edadPerruna * 10.5
        print(f"La edad en años perrunos es: {edadPerro}.")
    else:
        edadPerro = 21 + (edadPerruna - 2)*4
        print(f"La edad en años perrunos es: {edadPerro}.")

edad = float(input("Ingrese edad en años humanos: "))
    
edadCanina(edad)