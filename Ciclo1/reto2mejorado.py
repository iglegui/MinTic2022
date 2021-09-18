def listaConjunta():
    puntajesAyB = ""
    conteoA = 0
    conteoC = 0

    if conteoA == conteoC:
        puntajesAyB += "E"
    elif conteoA < conteoC:
        puntajesAyB += "C"
    elif conteoA > conteoC:
        puntajesAyB += "A"
    return puntajesAyB
 
def conteo(escA, escC, ganadores):

    for letra in ganadores: 
        if (letra not in escA) and (letra not in escC):
            listaConjunta()

        elif (letra in escA) and (letra in escC):
            conteoA += 1
            conteoC += 1
        
        elif letra in escA:
            conteoA += 1
            
        elif letra in escC:
            conteoC += 1       

    return puntajesAyB

escuderiaA = str(input())
escuderiaC = str(input())
ganadoresCarreraT = str(input())


print(listaConjunta(escuderiaA, escuderiaC, ganadoresCarreraT))