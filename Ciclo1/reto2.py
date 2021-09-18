def listaConjunta(escA, escC, ganadores):

    puntajesAyB = ""
    conteoA = 0
    conteoC = 0

    for letra in ganadores: 

        if (letra not in escA) and (letra not in escC):
            if conteoA == conteoC:
                puntajesAyB += "E"
            elif conteoA < conteoC:
                puntajesAyB += "C"
            elif conteoA > conteoC:
                puntajesAyB += "A"

        elif (letra in escA) and (letra in escC):
            conteoA += 1
            conteoC += 1
            if conteoA == conteoC:
                puntajesAyB += "E"
            elif conteoA < conteoC:
                puntajesAyB += "C"
            elif conteoA > conteoC:
                puntajesAyB += "A"
        
        elif letra in escA:
            conteoA += 1
            if conteoC == conteoA:
                puntajesAyB += "E"
            elif conteoC > conteoA:
                puntajesAyB += "C"
            elif conteoC < conteoA:
                puntajesAyB += "A"
            
        elif letra in escC:
            conteoC += 1
            if conteoA == conteoC:
                puntajesAyB += "E"
            elif conteoA > conteoC:
                puntajesAyB += "A"
            elif conteoA < conteoC:
                puntajesAyB += "C"

    return puntajesAyB


escuderiaA = str(input())
escuderiaC = str(input())
ganadoresCarreraT = str(input())

print(listaConjunta(escuderiaA, escuderiaC, ganadoresCarreraT))
