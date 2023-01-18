# Multiplicative Cipher

import ExtendedEuclidean as ExtdEucAlgo


def MultiplicativeCipherEncryption(text, n):
    # Key genration part
    while True:
        encryptionKey = int(
            input(f"Enter the encryption key for multiplicative in range of {n} : "))
        if encryptionKey > n and encryptionKey < 0:
            print("Entered Key is out of range")
        else:
            decryptionKey = ExtdEucAlgo.ExtEucAlgo(encryptionKey, n)
            if decryptionKey == -1:
                print("Invalid Key")
            else:
                break

    # Encryption part
    encryptedText = ""
    for ch in text:
        encryChar = ord(ch) - 65
        encryptedText += chr(((encryChar * encryptionKey) % n) + 65)

    return [encryptedText, decryptionKey]


def MultiplicativeCipherDecryption(text: str, key):
    # Decryption part
    decryptedText = ""
    for ch in text:
        decryChar = ord(ch) - 65
        decryptedText += chr(((decryChar * key) % 26) + 65)

    return decryptedText


if __name__ == "__main__":
    text = input("Enter the text : ")
    text = text.upper()
    n = 26
    encryptedText, decryptionKey = MultiplicativeCipherEncryption(text, 26)
    print("\nOrignal text :- ", text)
    print("Encrypted text :- ", encryptedText)
    decryptedText = MultiplicativeCipherDecryption(
        encryptedText, decryptionKey)
    print("Decrypted text :- ", decryptedText)
