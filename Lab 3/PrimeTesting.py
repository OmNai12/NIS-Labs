# Use for primality testing

import random as rand
from SquareAndMultiply import SqAndMul as fastPower
from ExtendedEuclidean import findGcd as GCD_calc


def isPrime(n):
    k = 700
    while k > 0:
        a = 2 + rand.randint(0, 97824621) % (n - 3)
        if GCD_calc(n, a) != 1:
            return False
        if fastPower(a, n-1, n) != 1:
            return False
        k -= 1

    return True


if __name__ == "__main__":
    # n = 246810121
    n = 8242721
    m = 98862919
    ans = isPrime(m)
    print(ans)
