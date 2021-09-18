def valorAbsoluto(numero):
    if numero < 0:
        resultado = numero * -1
        print(f"El valor absoluto de {numero} es {resultado}.")
    else:
        print(f"El valor absoluto de {numero} es {numero}.")

entero = int(input("Ingrese un número entero: "))
    
valorAbsoluto(entero)