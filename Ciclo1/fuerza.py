m1 = float(input("Ingrese masa 1: "))
m2 = float(input("Ingrese masa 2: "))
r = float(input("Ingrese la distancia: "))

gravitational_constant = 6.67384e-10

force = (gravitational_constant * m1 * m2) / (r ** 2)

print(force)