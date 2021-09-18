rowA = [1, 2, 3]
rowB = [4, 5, 6]
rowC = [7, 8, 9]

matrix = [rowA, rowB, rowC]

for fila in matrix:
  print(fila)

for index_fila in range(len(matrix)):
  fila = matrix[index_fila]

  for index_columna in range(len(fila)):
    componente = matrix[index_fila][index_columna]

    matrix[index_fila][index_columna] = componente ** 2
  
print("\n")
for fila in matrix:
  print(fila)