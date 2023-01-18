def matrixMultiplication(X, Y):
    # mat1 :- Plain Text Matrix
    # mat2 :- Key Matrix
    # result = []
    # for i in range(len(mat1)):
    #    # iterate through columns of Y
    #     for j in range(len(mat2[0])):
    #        # iterate through rows of Y
    #         for k in range(len(mat2)):
    #             result[i][j] += mat1[i][k] * mat2[k][j]

    # for r in result:
    #     print(r)
    result = [[sum(a*b for a, b in zip(X_row, Y_col))
               for Y_col in zip(*Y)] for X_row in X]

    for r in result:
        for j in r:
            print(chr((j % 26) + 65), end="\t")
        print()

    pass


if __name__ == "__main__":
    m1 = [[15,   0,    24], [12,  14, 17], [4,  12,    14], [13, 4,    24]]
    m2 = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]
    matrixMultiplication(m1, m2)
