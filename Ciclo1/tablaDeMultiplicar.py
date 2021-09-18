def tablaMultiplicar(num):
    for i in range(1, 11):
        resultado = int(num) * i
        print("{0} x {1} = {2}".format(num, i, resultado))

numero = str(input("Ingrese un número entero positivo: "))

while numero.isdigit() == False:
    numero = str(input("Por favor, ingrese un número entero positivo: "))

tablaMultiplicar(numero)
