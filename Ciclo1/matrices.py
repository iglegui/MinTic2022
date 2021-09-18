# Una función general que permite construir una nueva matriz que contiene
# el cuadrado de cada componente de una matriz dada

def cuadrados_matriz(X):
    Y = []
    for i in range(len(X)):
        fila = []
        for j in range(len(X[i])):
            fila.append(X[i][j]*X[i][j])
        Y.append(fila)
    return Y
print(cuadrados_matriz([[1,-3, 2],[4,11,-1]]))


# Una función general que permite obtener un arreglo con los elementos que
# están en la diagonal de una matriz cuadrada (mismo número de filas y
# columnas)
def diagonal_matriz(X):
    Y = []
    for i in range(len(X)):
        Y.append(X[i][i])
    return Y
print(diagonal_matriz([[1,-3],[4,11]]))

# Una función general que permite determinar si una matriz cuadrada es
# simétrica o no

def matriz_simetrica(X):
    bandera = True
    for i in range(len(X)-1):
        for j in range(i+1,len(X)):
            bandera = bandera and (X[i][j] == X[j][i])
    return bandera
print(matriz_simetrica([[1,-3],[4,11]]))
print(matriz_simetrica([["A","B"],["B","A"]]))