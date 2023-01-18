# Additive Cipher

def AdditiveCipherEncryption(text, n):
    # Key genration part
    while True:
        key = int(
            input(f"Enter the encryption key for additive in range of {n} : "))
        if key > n and key < 0:
            print("Entered Key is out of range")
        else:
            break

    # Encryption part
    encryptedText = ""
    for ch in text:
        encryChar = (((ord(ch) - 65)) + key) % 26
        encryptedText += chr(encryChar + 65)

    return [encryptedText, key]


def AdditiveCipherDecryption(text: str, key):
    # Decryption part
    decryptedText = ""
    for ch in text:
        decryChar = (((ord(ch) - 65)) - key) % 26
        decryptedText += chr(decryChar + 65)

    return decryptedText


if __name__ == "__main__":
    text = input("Enter the text : ")
    text = text.upper()
    n = 26
    encryptedText, decryptionKey = AdditiveCipherEncryption(text, 26)
    print("\nOrignal text :- ", text)
    print("Encrypted text :- ", encryptedText)
    decryptedText = AdditiveCipherDecryption(
        encryptedText, decryptionKey)
    print("Decrypted text :- ", decryptedText)
