import MatrixGenrator
import MatrixDisplay as ShowMatrix
import MatrixOperation as MatrixOP


def showEncryptedText(mat: list):
    text = ""
    for i in mat:
        for j in i:
            text += j

    return text


def HillCipherDecryption(keyMatrix, cipherText, matrixDimension):
    inverseKeyMatrix = MatrixOP.inverseOfMatrix(keyMatrix, matrixDimension)
    helperMat = MatrixOP.matrixMultiplication(
        MatrixGenrator.valueMatrix(cipherText, matrixDimension), inverseKeyMatrix)
    decrypetedText = showEncryptedText(helperMat)
    return decrypetedText


def HillCipherEncryption(pt: str, matrixDimension):
    print("\n\n**************************************************\n")
    # Genration of the plain text matrix.
    print("Plain text matrix is as under :- ")
    plainTextMatrix = MatrixGenrator.valueMatrix(pt, matrixDimension)
    ShowMatrix.matrixDispalyFunction(plainTextMatrix)
    print()
    # Genration of the key matrix.
    keyMatrix = MatrixGenrator.keyMatrixGenrator(
        matrixDimension, matrixDimension)
    print("Key matrix genrated is as under :- ")
    ShowMatrix.matrixDispalyFunction(keyMatrix)
    print()
    # Getting the the cipher text.
    cipherTextMatrix = MatrixOP.matrixMultiplication(
        plainTextMatrix, keyMatrix)
    cipherText = showEncryptedText(cipherTextMatrix)
    print("**************************************************\n")
    print("Encrypted text is as under :- ")
    print(cipherText, "\n")
    # Decryption of the cipher text.
    decryText = HillCipherDecryption(keyMatrix, cipherText, matrixDimension)
    print("Decrypted text is as under :- ")
    print(decryText, "\n")
    print("**************************************************\n")


def refinedPlainText(pt: str):
    # Removing the spaces in the string.
    return pt.replace(" ", "").upper()


def HillCipherFunction(pt):
    # Driver code of the hill cipher function.
    newPlainText = refinedPlainText(pt)
    lengthOfText = len(newPlainText)
    if (lengthOfText % 2 == 0) and (lengthOfText % 3 == 0):
        print("Encryption possible with both key matrix i.e. 2*2 or 3*3.\n")
        dimOfKeyMatrix = input("Enter key matric of your choice :- ")
        HillCipherEncryption(newPlainText, int(dimOfKeyMatrix))
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
    HillCipherFunction(plainText)
