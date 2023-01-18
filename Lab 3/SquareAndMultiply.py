# Square and multiply method for fast power.

# a^b % n for fast power

def SqAndMul(a, b, n):
    z, i = 1, 2
    binaryOfNumber = bin(b)
    while i != len(binaryOfNumber):
        z = (z*z) % n
        if binaryOfNumber[i] == 1:
            z = (z*a) % n
        i += 1

    return z


if __name__ == "__main__":
    a, b, n = 7, 100, 15
    ans = SqAndMul(a, b, n)
    print(ans)
