def ZeroMatrix(matrix) :

    ZeMat = []

    AuxRow = []

    for i in range(len(matrix)) :

        for j in range(len(matrix[0])) :

            if matrix[i][j] == 0 :

                if len(AuxRow) != 0 :

                    AuxRow = []

                for x in range(len(matrix[0])) :

                    AuxRow += [0]

                break

            else :

                AuxRow += [matrix[i][j]]

            
        ZeMat += [AuxRow]

        AuxRow = []


    return ZeMat


print(ZeroMatrix([[1, 2, 3], [4, 0, 6], [7, 8, 9]]))



