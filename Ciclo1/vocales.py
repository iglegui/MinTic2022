def letra(vocal):
    if len(vocal) == 1:
        if vocal == "a" or vocal == "e" or vocal == "i" or vocal == "o" or vocal == "u": 
	        print("La letra ingresada es vocal.")
        else:
            print("La letra ingresada no es vocal.")
    else:
        print("Por favor ingresar solo una letra.")


v = str(input("Ingrese una letra: "))
    
letra(v)