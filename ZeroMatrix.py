def ZeroMatrix(matrix) : #SC O(len(matrix)*len(matrix[0])), TC O(len(matrix)*len(matrix[0]))

    ZeroRows = []

    ZeroColumns = []

    #Encontrar filas con cero

    for i in range(len(matrix)) :

        if 0 in matrix[i] :

            ZeroRows += [i]
                
    #Encontrar columnas con cero

    for i in range(len(matrix[0])) :

        for j in range(len(matrix)) :

            if matrix[j][i] == 0 :

                ZeroColumns += [i]

                break


    #Hacer cero filas que contengan cero

    for fila in ZeroRows :

        for col in range(len(matrix[0])) :

            matrix[fila][col] = 0

    
    #Hacer cero columnas que contengan cero

    for col in ZeroColumns :

        for fila in range(len(matrix)) :

            matrix[fila][col] = 0


    return matrix



print(ZeroMatrix([[1, 2, 3], [4, 0, 6], [7, 8, 9]]))
# 103
# 000
# 709

print(ZeroMatrix([[1, 0, 2], [0, 4, 6], [7, 8, 0]]))

# 000
# 000
# 000




