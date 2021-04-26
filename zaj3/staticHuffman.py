from queue import PriorityQueue
from Tekstowe.zaj3.utils import *


class Node:
    def __init__(self):
        self.char = '\0'
        self.weight = -1
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.char < other.char


def staticHuffman(lettersCounts):

    Q = PriorityQueue()
    for c, w in lettersCounts.items():
        v = Node()
        v.char = c
        v.weight = w
        Q.put((w, v))

    while Q.qsize() > 1:
        _, v1 = Q.get()
        _, v2 = Q.get()
        p = Node()
        p.weight = v1.weight + v2.weight
        p.left = v1
        p.right = v2
        Q.put((p.weight, p))

    _, root = Q.get()
    Codes = dict()
    getHuffmanCoding(root, "", Codes)

    return root, Codes




if __name__ == '__main__':

    actFile = open("Texts/Not ASCII/Matthew Fontaine Maury, the Pathfinder of the Seas by Charles Lee Lewis", encoding='ASCII')
    actText = actFile.read()

    text = actText

    lettersCounts = getLettersCounts(text)
    l = list(lettersCounts.items())
    l.sort(key=lambda x: x[1], reverse=True)
    print(l)

    root, Codes = staticHuffman(lettersCounts)
    print(Codes)

    rawBin = getAsciiCoding(text)
    compressedBin = compress(text, Codes)
    # print(rawBin)
    # print(compressedBin)
    print(len(compressedBin)/len(rawBin))
    decompressed = decompress(compressedBin, root)
    # print(decompressed)

