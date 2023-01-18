# RSA algorithm

import random as rand
from PrimeTesting import isPrime
import SquareAndMultiply as fastPower
import ExtendedEuclidean as EEAlgo


def genratePrimeNumber():
    num = rand.randint(1001, 100001)
    while isPrime(num) != True:
        num = rand.randint(1001, 100001)
    return num


def getEncryKey(n):
    e = rand.randint(1, n)
    while EEAlgo.findGcd(e, n) != 1:
        e = rand.randint(1, n)
    return e


def RSA_KeysGenration():
    p = genratePrimeNumber()
    q = genratePrimeNumber()
    n = p*q
    phiN = (p-1)*(q-1)
    encryKey = getEncryKey(phiN)
    decryKey = EEAlgo.ExtEucAlgo(encryKey, phiN)
    # print(encryKey, decryKey)
    return [encryKey, decryKey, n]


def RSA_encryption(e, encryKey, n):
    c = fastPower.SqAndMul(e, encryKey, n)
    return c


def RSA_decryption(c, decryKey, n):
    e = fastPower.SqAndMul(c, decryKey, n)
    return e


if __name__ == "__main__":
    msg = 89
    encryKey, decryKey, n = RSA_KeysGenration()
    print(encryKey, decryKey, n)
    encry_msg = RSA_encryption(msg, encryKey, n)
    print(encry_msg)
    decry_msg = RSA_decryption(encry_msg, decryKey, n)
    print(decry_msg)
