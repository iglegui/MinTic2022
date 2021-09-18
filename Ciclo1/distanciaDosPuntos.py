from math import sqrt as sq

def distanciaDosPuntos(cx1, cx2, cy1, cy2):
    distancia = sq(((cx2-cx1)**2) + ((cy2-cy1)**2))
    print(f"La distancia entre las coordenadas ({cx1}, {cy1}) y ({cx2}, {cy2}) es {distancia}.")   

x1 = float(input("Ingrese x1: "))
x2 = float(input("Ingrese x2: "))
y1 = float(input("Ingrese y1: "))
y2 = float(input("Ingrese y2: "))


distanciaDosPuntos(x1, x2, y1, y2)