def HillCipherEncryption(pt: str, matrixDimension):

    pass


def refinedPlainText(pt: str):
    gapPresentIndex = []
    for i in range(len(pt)):
        if pt[i] == " ":
            gapPresentIndex.append(i)

    newText = pt.replace(" ", "").upper()
    return newText


def HillCipherFunction(pt):
    newPlainText = refinedPlainText(plainText)
    lengthOfText = len(newPlainText)
    if (lengthOfText % 2 == 0) and (lengthOfText % 3 == 0):
        print("Encryption possible with any of the key matrix of 2*2 or 3*3.")
    elif lengthOfText % 2 == 0:
        print("Encryption possible with 2*2 key matrix.")
        HillCipherEncryption(newPlainText, 2)
    elif lengthOfText % 3 == 0:
        print("Encryption possible with 3*3 key matrix.")
        HillCipherEncryption(newPlainText, 3)
    else:
        print("Encryption is not possible for the given plain text.")
        exit(0)
    pass


if __name__ == "__main__":
    plainText = "pay more money"
    print("In Main ", HillCipherFunction(plainText))
