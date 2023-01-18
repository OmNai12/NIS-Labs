import random
MonoalphabeticSubstitutionCipher = {}
Alphabets = "abcdefghijklmnopqrstuvwxyz"
Letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(26):
    MonoalphabeticSubstitutionCipher[Alphabets[i]] = random.choice(Letters)
    Letters.remove(MonoalphabeticSubstitutionCipher[Alphabets[i]])

print(MonoalphabeticSubstitutionCipher)
keys = list(MonoalphabeticSubstitutionCipher.keys())
vals = list(MonoalphabeticSubstitutionCipher.values())


def encryption(plain_text):
    cipher_text = ""
    print("\nTable for Encryption: \n")
    print("Plain Text\t : \t", end="")
    for i in range(len(plain_text)):
        print(plain_text[i] + "\t", end="")
    print()
    print("Cipher Text\t : \t", end="")
    for i in range(len(plain_text)):
        print(MonoalphabeticSubstitutionCipher[plain_text[i]] + "\t", end="")
    print()
    for i in range(len(plain_text)):
        cipher_text += MonoalphabeticSubstitutionCipher[plain_text[i]]
    return cipher_text


def decryption(cipher_text):
    decrypted_text = ""
    print("\nTable for Decryption: \n")
    print("Cipher Text\t : \t", end="")
    for i in range(len(cipher_text)):
        print(cipher_text[i] + "\t", end="")
    print()
    print("Plain Text\t : \t", end="")
    for i in range(len(cipher_text)):
        print(keys[vals.index(cipher_text[i])] + "\t", end="")
    print()
    for i in range(len(cipher_text)):
        decrypted_text += keys[vals.index(cipher_text[i])]
    return decrypted_text


if __name__ == "__main__":
    plain_text = input("\nEnter Plain Text: ")
    cipher_text = encryption(plain_text)
    print("\nEncrypted(Cipher) Text is : " + cipher_text)
    decrypted_text = decryption(cipher_text)
    print("\nDecrypted(Plain) Text is : " + decrypted_text)
