import MatrixGenrator
import MatrixDisplay as ShowMatrix


def HillCipherEncryption(pt: str, matrixDimension):
    print("**************************************************\n")
    print("Plain text matrix is as under :- ")
    plainTextMatrix = MatrixGenrator.plainTextMatrixGenrator(
        pt, matrixDimension)
    ShowMatrix.matrixDispalyFunction(plainTextMatrix)
    print()
    # keyMatrix = MatrixGenrator.keyMatrixGenrator(matrixDimension)
    keyMatrix = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]
    print("Key matrix kenrated is as under :-")
    ShowMatrix.matrixDispalyFunction(keyMatrix)
    # ShowMatrix.matrixDispalyFunction(keyMatrix, matrixDimension)

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
        print("Encryption possible with any of the key matrix of 2*2 or 3*3.\n")
        HillCipherEncryption(newPlainText, 3)
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
