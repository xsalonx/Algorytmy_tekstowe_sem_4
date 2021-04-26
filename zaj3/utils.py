def getLettersCounts(text: str):
    lettersCounts = {}
    for c in text:
        if c not in lettersCounts:
            lettersCounts[c] = 1
        else:
            lettersCounts[c] += 1
    return lettersCounts


def getAsciiCoding(text: str):
    binText = ""
    for c in text:
        binText += '{0:08b}'.format(ord(c))

    return binText


def getHuffmanCoding(v, code: str, Codes: dict):
    if v.char != '\0' or v.weight == 0:
        Codes[v.char] = code
        return
    else:
        getHuffmanCoding(v.left, code + '0', Codes)
        getHuffmanCoding(v.right, code + '1', Codes)


def compress(text, Codes):
    compressed = ""
    for c in text:
        compressed += Codes[c]
    return compressed


def decompress(text: str, root):
    decompressed = ""
    v = root
    # konwencja 0 - lewe dziecko, 1 - prawe dziecko
    for c in text:
        if c == '0':
            v = v.left
        else:
            v = v.right
        if v.char != '\0':
            decompressed += v.char
            v = root

    return decompressed
