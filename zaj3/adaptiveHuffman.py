from Tekstowe.zaj3.utils import *


class Node:
    def __init__(self):
        self.char = '\0'
        self.weight = 0
        self.left = None
        self.right = None
        self.p = None

    def __lt__(self, other):
        return self.char < other.char

    def getLevel(self):
        lev = 0
        X = self
        while X.p is not None:
            lev += 1
            X = X.p
        return lev
    def __str__(self):
        return "{" + f"{self.char}, {self.weight}" + "}"

    def __repr__(self):
        return "{" + f"{self.char}, {self.weight}" + "}"

def getNodesAtLevel(root: Node, level: int):
    nodesList = []

    def trace(V: Node, lev):
        if V == None:
            return
        if lev == level:
            nodesList.append(V)
            return
        else:
            trace(V.left, lev + 1)
            trace(V.right, lev + 1)

    trace(root, 0)
    return nodesList


def getSwapper(U, root):
    lev = U.getLevel()
    w = U.weight

    lev_1Nodes = getNodesAtLevel(root, lev - 1)
    Yidx = max([-1] + [i for i in range(len(lev_1Nodes)) if (lev_1Nodes[i].weight == w and lev_1Nodes[i] is not U)])
    if Yidx != -1:
        return lev_1Nodes[Yidx]
    else:
        lev0Nodes = getNodesAtLevel(root, lev)
        Yidx = max([-1] + [i for i in range(len(lev0Nodes)) if (lev0Nodes[i].weight == w and lev0Nodes[i] is not U)])
        if Yidx != -1:
            return lev0Nodes[Yidx]
        else:
            return None


def swapSubtrees(X: Node, U: Node):
    if X == X.p.left:
        Xside = 'l'
    else:
        Xside = 'r'
    if U == U.p.left:
        Uside = 'l'
    else:
        Uside = 'r'

    X.p, U.p = U.p, X.p
    if Xside == 'l':
        U.p.left = U
    else:
        U.p.right = U

    if Uside == 'l':
        X.p.left = X
    else:
        X.p.right = X

    # X.p.weight = X.p.left.weight + X.p.left.weight
    # U.p.weight = U.p.left.weight + U.p.left.weight


def updateTree(U, root):
    while U is not root:
        S = getSwapper(U, root)
        if S is not None:
            swapSubtrees(U, S)
        U.weight += 1
        U = U.p
    root.weight += 1


def adaptiveHuffman(text):
    root = Node()
    zeroNode = Node()
    first = Node()
    first.weight = 1
    first.char = text[0]
    root.weight = 1

    leaves = {'\0': zeroNode, text[0]: first}

    first.p = root
    zeroNode.p = root
    root.left = zeroNode
    root.right = first

    for c in text[1:]:
        print(c,end="")
        if c not in leaves:
            zeroP = zeroNode.p
            if zeroNode == zeroP.left:
                side = 'l'
            else:
                side = 'r'
            newCharNode = Node()
            newCharNode.char = c
            newCharNode.weight = 1
            leaves[c] = newCharNode

            upN = Node()
            upN.weight = 1
            upN.p = zeroP

            if side == 'l':
                zeroP.left = upN
            else:
                zeroP.right = upN

            upN.left = zeroNode
            zeroNode.p = upN

            upN.right = newCharNode
            newCharNode.p = upN

            updateTree(upN.p, root)

        else:
            leaves[c].weight += 1
            updateTree(leaves[c].p, root)

    Codes = dict()
    getHuffmanCoding(root, "", Codes)

    return root, Codes

if __name__ == '__main__':

    actFile = open("Texts/2X Linux Text 1MB", encoding='ASCII')
    actText = actFile.read()

    text = actText
    print(set(text))
    lettersCounts = getLettersCounts(text)
    l = list(lettersCounts.items())
    l.sort(key=lambda x: x[1], reverse=True)
    print(l)

    root, Codes = adaptiveHuffman(text)

    rawBin = getAsciiCoding(text)
    compressedBin = compress(text, Codes)
    # print(rawBin)
    # print(compressedBin)
    print(len(compressedBin)/len(rawBin))
    decompressed = decompress(compressedBin, root)
    # print(decompressed)

