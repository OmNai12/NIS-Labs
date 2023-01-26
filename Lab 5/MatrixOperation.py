# Extended Euclidean Algorithm For Finding Multiplicative Inverse

def findGcd(a, b):
    if b == 0:
        return a
    else:
        return findGcd(b, a % b)


def ExtEucAlgo(a, n):
    getGCD = findGcd(a, n)
    if getGCD == 1:
        # r1 > r2
        r1 = n
        r2 = a
        t1 = 0
        t2 = 1
        i = 0
        while r2 > 0:
            q = int(r1/r2)
            r = r1 - q*r2
            r1 = r2
            r2 = r
            # Inverse part
            t = t1 - q*t2
            t1 = t2
            t2 = t

        if t1 < 0:
            return t1 % n
        else:
            return t1
    else:
        return -1


def matrixMultiplication(X, Y):
    # Used for Matrix Multiplicaion
    result = [[sum(a*b for a, b in zip(X_row, Y_col))
               for Y_col in zip(*Y)] for X_row in X]
    encryptedMatrix = []
    for r in result:
        tempMatrix = []
        for j in r:
            tempMatrix.append(chr((j % 26) + 65))
        encryptedMatrix.append(tempMatrix)

    return encryptedMatrix


def findDeterminant(mat, dim):
    # To find the determinant.
    if dim == 2:
        det = (mat[0][0]*mat[1][1]) - (mat[0][1]*mat[1][0])
    elif dim == 3:
        det = mat[0][0]*((mat[1][1]*mat[2][2]) - (mat[2][1]*mat[1][2])) - mat[0][1]*((mat[1][0]*mat[2]
                                                                                      [2]) - (mat[2][0]*mat[1][2])) + mat[0][2]*((mat[1][0]*mat[2][1]) - (mat[2][0]*mat[1][1]))
    return det % 26


def inverseOfdim2(mat: list):
    # This will give the adjoint of the matrix.
    return [mat[1][1], (-1)*mat[0][1]], [(-1)*mat[1][0], mat[0][0]]


def inverseOfdim3(mat: list):
    # This will give the adjoint of the matrix.
    k = 0
    for i in range(2):
        for j in range(3):
            mat[k].append(mat[j][i])
            k = (k + 1) % 3

    while k != 2:
        mat.append(mat[k].copy())
        k = k + 1

    k = 0
    adjMat = []
    for i in range(3):
        adjMat.append([])

    for i in range(1, 4):
        for j in range(1, 4):
            l = [[mat[i][j], mat[i][j+1]], [mat[i+1][j], mat[i+1][j+1]]]
            x = findDeterminant(l, 2)
            adjMat[k].append(x)
            k = (k + 1) % 3

    return adjMat


def helperMatrix(mat, val):
    # This multiply the given matix with inverse of it's deteminant and also be in range of mod 26
    invKeyMat = []
    for i in mat:
        tempMat = []
        for j in i:
            tempMat.append((j*val) % 26)
        invKeyMat.append(tempMat)

    return invKeyMat


def inverseOfMatrix(matrix, dimension):
    determinant = findDeterminant(matrix, dimension)
    inverseOfDeterminant = ExtEucAlgo(determinant, 26)
    if dimension == 2:
        mat = inverseOfdim2(matrix)
    elif dimension == 3:
        mat = inverseOfdim3(matrix)

    return helperMatrix(mat, inverseOfDeterminant)
