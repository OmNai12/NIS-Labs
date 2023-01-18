# # Playfair Cipher

from math import ceil


# def find_I_J(kt: str):
#     if kt.find('I') != -1 or kt.find('J') != -1:
#         return True
#     else:
#         return False


# def listMaker():
#     tempL = 26*[0]
#     l = []
#     for i in range(26):
#         l.append(65 + i)
#     return [l, tempL]


# def alphabetBox(kt, i_or_j_present):
#     for i in keyText:
#         print(i)
#     pass


# def autokeyCipher(kt: str):
#     kt = kt.upper()
#     # Refrence List
#     l = listMaker()
#     # Checking prescence of I or J
#     findI_J = find_I_J(kt)

#     pass

# def createSplitList(pt: str):
#     splitList = []
#     j = 0
#     for i in range(ceil(len(pt)/2)):
#         splitList.append(pt[j:j + 2])
#         j = j + 2

#     print(splitList)
#     pass


def createSplitList(pt: str):
    splitList = []
    i = 0
    while i != (len(pt) - 1):
        # print(pt[i], pt[i+1])
        if pt[i] != pt[i+1]:
            splitList.append(pt[i]+pt[i+1])
            i = i + 1
        i = i + 1

    print(splitList)

    pass


if __name__ == "__main__":
    key = "ORANGE"
    plainText = "hello"
    createSplitList(plainText)
    # autokeyCipher(keyText)
    pass
