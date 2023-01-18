# Affine Cipher

import AdditiveCipher as AddCph
import MultiplicativeCipher as MulCph


def AffineCipherEncryption(text, n):
    # Encryption part
    encryption_AdditiveCipher, additiveCipherKey = AddCph.AdditiveCipherEncryption(
        text, n)
    encryption_MultiplicativeCipher, multiplicativeCipherKey = MulCph.MultiplicativeCipherEncryption(
        encryption_AdditiveCipher, n)
    return [additiveCipherKey, multiplicativeCipherKey, encryption_MultiplicativeCipher]


def AffineCipherDecryption(addtiveKey, multiplicativeKey, text):
    # Decryption part
    decryption_MultiplicativeCipher = MulCph.MultiplicativeCipherDecryption(
        text, multiplicativeKey)
    decryption_AdditiveCipher = AddCph.AdditiveCipherDecryption(
        decryption_MultiplicativeCipher, addtiveKey)
    return decryption_AdditiveCipher


if __name__ == "__main__":
    text = input("Enter the text : ")
    text = text.upper()
    n = 26
    addKey, mulKey, encryptedText = AffineCipherEncryption(text, n)
    print("\nOrignal text :- ", text)
    print("Encrypted text :- ", encryptedText)
    decryptedText = AffineCipherDecryption(addKey, mulKey, encryptedText)
    print("Decrypted text :- ", decryptedText)
