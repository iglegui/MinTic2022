import math

def area_rectangulo(num1, num2):
    total_area_rectangulo = float(num1 * num2)
    return total_area_rectangulo

def area_dos_circulos(num3): 
    total_area_circulos = float(2 * (math.pi * (num3 ** 2)))
    return total_area_circulos


ancho = float(input("Ingrese el ancho del rectangulo: "))
altura = float(input("Ingrese la altura del rectangulo: "))
radio = float(input("Ingrese el radio: "))

area_carrito = area_rectangulo(ancho, altura) + area_dos_circulos(radio)

print(f"El área del carrito es: {area_carrito}")