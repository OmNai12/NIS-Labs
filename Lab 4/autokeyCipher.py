def autoKeyCipherKeyGenration(msg: str, autoKey):
    return chr(autoKey + 65) + msg[0:len(msg) - 1]


def autoKeyCipherEncryption(msg, key):
    i = 0
    encryptedText = ""
    while i != len(msg):
        encryptedText += chr(((ord(msg[i]) - 65 + ord(key[i]) - 65) % 26) + 65)
        i += 1
    return encryptedText


def autoKeyCipherDecryption(encryptedText, key):
    i = 0
    decryptedText = ""
    while i != len(encryptedText):
        decryptedText += chr(
            ((ord(encryptedText[i]) - 65 - ord(key[i]) - 65) % 26) + 65)
        i += 1
    return decryptedText


if __name__ == "__main__":
    text = "attack"
    autokey = 12
    key = autoKeyCipherKeyGenration(text.upper(), autokey)
    encryptedText = autoKeyCipherEncryption(text.upper(), key)
    print("Encrypted Text :- ", encryptedText)
    decryptedText = autoKeyCipherDecryption(encryptedText, key)
    print("Decrypted Text :- ", decryptedText)
