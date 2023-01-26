def valueMatrix(pt: str, n):
    matrix = []
    k = 0
    rows = int(len(pt) / n)
    for i in range(rows):
        tempList = []
        for j in range(n):
            tempList.append(ord(pt[k]) - 65)
            k += 1
        matrix.append(tempList)

    return matrix


# def keyMatrixGenrator(n):
#     matrix = []
#     for rows in range(n):
#         coloums = []
#         for j in range(n):
#             coloums.append(random.randint(0, 25))
#         matrix.append(coloums)
#     return matrix

def keyMatrixGenrator(n, dim):
    if dim == 2:
        return [[7, 8], [11, 11]]
    elif dim == 3:
        return [[17, 17, 5], [21, 18, 21], [2, 2, 19]]
