def encryption(plain_text, cipher_key):
    cipher_text = ""
    print("\nTable for Encryption: \n")
    print("Plain Text\t : ", end="")
    for i in range(len(plain_text)):
        print(plain_text[i] + "\t", end="")
    print()
    print("Pi\t\t : ", end="")
    for i in range(len(plain_text)):
        print(str(ord(plain_text[i]) - ord("a")) + "\t", end="")
    print()
    print("Cipher Key\t : ", end="")
    for i in range(len(plain_text)):
        print(str(cipher_key) + "\t", end="")
    print()
    print("(Pi + key)\t : ", end="")
    for i in range(len(plain_text)):
        print(str((ord(plain_text[i]) - ord("a") + cipher_key)) + "\t", end="")
    print()
    print("Ci\t\t : ", end="")
    for i in range(len(plain_text)):
        print(
            str(((ord(plain_text[i]) - ord("a") + cipher_key) % 26)) + "\t", end="")
    print()
    print("Cipher Text\t : ", end="")
    for i in range(len(plain_text)):
        print(chr(((ord(plain_text[i]) - ord("a") +
              cipher_key) % 26) + ord("a")) + "\t", end="")
    print()
    for i in range(len(plain_text)):
        cipher_text += chr(((ord(plain_text[i]) -
                           ord("a") + cipher_key) % 26) + ord("a"))
    return cipher_text


def decryption(cipher_text, cipher_key):
    decrypted_text = ""
    print("\nTable for Decryption: \n")
    print("Cipher Text\t : ", end="")
    for i in range(len(cipher_text)):
        print(cipher_text[i] + "\t", end="")
    print()
    print("Ci\t\t : ", end="")
    for i in range(len(cipher_text)):
        print(str(ord(cipher_text[i]) - ord("a")) + "\t", end="")
    print()
    print("Cipher Key\t : ", end="")
    for i in range(len(cipher_text)):
        print(str(cipher_key) + "\t", end="")
    print()
    print("(Ci - key)\t : ", end="")
    for i in range(len(cipher_text)):
        print(
            str((ord(cipher_text[i]) - ord("a") - cipher_key)) + "\t", end="")
    print()
    print("Pi\t\t : ", end="")
    for i in range(len(cipher_text)):
        print(
            str(((ord(cipher_text[i]) - ord("a") - cipher_key) % 26)) + "\t", end="")
    print()
    print("Plain Text\t : ", end="")
    for i in range(len(cipher_text)):
        print(chr(
            ((ord(cipher_text[i]) - ord("a") - cipher_key) % 26) + ord("a")) + "\t", end="")
    print()
    for i in range(len(cipher_text)):
        decrypted_text += chr(((ord(cipher_text[i]) -
                              ord("a") - cipher_key) % 26) + ord("a"))
    return decrypted_text


def cryptanalysis(cipher_text, cipher_key):
    cryptanalytic_guess = ""
    for i in range(len(cipher_text)):
        cryptanalytic_guess += chr(
            ((ord(cipher_text[i]) - ord("a") - cipher_key) % 26) + ord("a"))
    return cryptanalytic_guess


if __name__ == "__main__":
    plain_text = input("\nEnter Plain Text: ")
    cipher_key = int(input("\nEnter Cipher Key: "))
    cipher_text = encryption(plain_text, cipher_key)
    print("\nEncrypted(Cipher) Text is : " + cipher_text)
    decrypted_text = decryption(cipher_text, cipher_key)
    print("\nDecrypted(Plain) Text is : " + decrypted_text)
    print("\nCryptanalysis:\n")
    print("Cryptanalysis for cipher key,")
    for i in range(26):
        print("(k = " + str(i) + ") : " + cryptanalysis(cipher_text, i))
