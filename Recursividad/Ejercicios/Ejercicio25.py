#transponer una matriz
def transpose_recursive(matrix):
    # Si la matriz es de tamaño 1x1, devolver la matriz original
    if len(matrix) == 1 and len(matrix[0]) == 1:
        return matrix

    # Si la matriz no es de tamaño 1x1, crear una matriz transpuesta de tamaño nxm
    n = len(matrix)
    m = len(matrix[0])
    transposed_matrix = [[0 for j in range(n)] for i in range(m)]

    # Recorrer la matriz original y asignar cada elemento a la posición correspondiente en la matriz transpuesta
    for i in range(n):
        for j in range(m):
            transposed_matrix[j][i] = matrix[i][j]
    # Llamar recursivamente a la función con la matriz transpuesta como entrada y devolver el resultado
    return transpose_recursive(transposed_matrix)

matrix = [[1,0,0],
          [2,1,0],
          [1,1,1]]

ma = transpose_recursive(matrix)
print(ma)