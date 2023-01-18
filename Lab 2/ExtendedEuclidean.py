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


if __name__ == "__main__":
    a = 15
    n = 26
    ans = ExtEucAlgo(a, n)
    if ans == -1:
        print("Multiplicative inverse is not possible.")
    else:
        print(f"The multiplictive inverse of {a} is {ans}")
