def area_rectangulo(l, a):
  area = l * a
  return area
  
largo = float(input("Largo del rectángulo: "))
ancho = float(input("Ancho del rectángulo: "))
print("El área del rectángulo es:", end = " ")
print(area_rectangulo(largo, ancho))

