def RotateMatrix(matrix) : #SC O(len(matrix)^2), TC O(len(matrix)^2)

    RotMat = [] #SC O(1), TC O(1)

    aux = [] #SC O(1), TC O(1)

    for i in range(len(matrix)) : #SC O(len(matrix)^2), TC O(len(matrix)^2)

        for j in range(len(matrix)) : #SC O(len(matrix)), TC O(len(matrix))

            aux += [matrix[len(matrix) - j - 1][i]] #SC O(1), TC O(1)

            
        RotMat += [aux] #SC O(1), TC O(1)

        aux = [] #SC O(1), TC O(1)




    return RotMat #SC O(1), TC O(1)

print(RotateMatrix([['a', 'b'], ['c', 'd']]))
# ca
# db

print(RotateMatrix([['q', 'w', 'e'], ['r', 't', 'y'], ['u', 'i', 'o']]))
# urq
# itw
# oye

