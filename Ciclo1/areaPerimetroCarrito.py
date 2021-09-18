from math import pi as p

def area_primer_rectangulo(a1, a2):
    total_area_rectangulo1 = float(a1 * a2)
    return total_area_rectangulo1
def area_segundo_rectangulo(a3, a4):
    total_area_rectangulo2 = float(a3 * a4)
    return total_area_rectangulo2
def area_primer_circulo(r1): 
    total_area_circulo1 = float(p * (r1 ** 2))
    return total_area_circulo1
def area_segundo_circulo(r2): 
    total_area_circulo2 = float(p * (r2 ** 2))
    return total_area_circulo2
def perimetro_primer_rectangulo(a5, a6):
    total_perimetro_rectangulo1 = float(a5 + a6 + a6) # un lado(ancho) del primer rectangulo 
    return total_perimetro_rectangulo1                # ya va incluido en el ancho del segundo 
                                                      # rectangulo, por esa razon no se suma aqui.   
def perimetro_segundo_rectangulo(a7, a8):
    total_perimetro_rectangulo2 = float(a7 + a7 + a8 + a8)
    return total_perimetro_rectangulo2
def perimetro_primer_circulo(r3):
    diametro_circulo1 = r3 * 2 
    total_perimetro_circulo1 = float(p * diametro_circulo1)
    return total_perimetro_circulo1
def perimetro_segundo_circulo(r4):
    diametro_circulo2 =  r4 * 2
    total_perimetro_circulo2 = float(p * diametro_circulo2)
    return total_perimetro_circulo2


ancho1 = float(input("Ingrese el ancho del primer rectangulo: "))
altura1 = float(input("Ingrese la altura del primer rectangulo: "))
ancho2 = float(input("Ingrese el ancho del segundo rectangulo: "))
altura2 = float(input("Ingrese la altura del segundo rectangulo: "))
radio1 = float(input("Ingrese el radio del primer circulo: "))
radio2 = float(input("Ingrese el radio del segundo circulo: "))

area_carrito = float(area_primer_rectangulo(ancho1, altura1) + area_segundo_rectangulo(ancho2, altura2)
                + area_primer_circulo(radio1) + area_segundo_circulo(radio2))
perimetro = float(perimetro_primer_rectangulo(ancho1, altura1) + perimetro_segundo_rectangulo(ancho2, altura2)
                + perimetro_primer_circulo(radio1) + perimetro_segundo_circulo(radio2))

print(f"El total del área del carrito inclinado es {area_carrito}. Y su perímetro es {perimetro}.")