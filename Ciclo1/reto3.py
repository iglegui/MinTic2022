listaViajes = input().split()

frecuenciaLetras = []
frecuenciaConteo = []

for i in range(len(listaViajes)):
    if i == 0:
        conteo = 0
        conteo2 = 0
        frecuenciaLetras.append(listaViajes[i])
        conteo += 1
        frecuenciaConteo.append(conteo)
    else:
        if listaViajes[i] == listaViajes[i-1]:
            frecuenciaConteo[conteo2] += 1
        else:
            frecuenciaLetras.append(listaViajes[i])
            conteo = 1
            conteo2 += 1
            frecuenciaConteo.append(conteo)

print(" ".join([str(item1) for item1 in frecuenciaLetras]))
print(" ".join([str(item2) for item2 in frecuenciaConteo]))


