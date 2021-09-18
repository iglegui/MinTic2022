def tipoTriangulo(a, b, c):

    if (a == b == c):
        print(f"El triángulo es equilatero.")
    elif (a == b or b == c or c == a):
        print(f"El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")

ladoA = float(input("Ingrese el lado A del triángulo: "))
ladoB = float(input("Ingrese el lado B del triángulo: "))
ladoC = float(input("Ingrese el lado C del triángulo: "))
    
tipoTriangulo(ladoA, ladoB, ladoC)