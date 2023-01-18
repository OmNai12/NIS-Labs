import random


def genrateMatrix(n):
    matrix = []
    for row in range(n):
        coloums = []
        for j in range(n):
            coloums.append(random.randint(0, 25))
        matrix.append(coloums)

    print(matrix)


if __name__ == "__main__":
    n = 2
    genrateMatrix(n)
