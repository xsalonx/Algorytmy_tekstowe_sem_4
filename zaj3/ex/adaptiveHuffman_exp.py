maxLevels = 100


class Node:
    def __init__(self):
        self.char = '\0'
        self.weight = 0
        self.left = None
        self.right = None
        self.p = None
        self.level = -1

    def __lt__(self, other):
        return self.char < other.char

    def updateLevels(self):
        if self.left is not None:
            self.left.level = self.level + 1
            self.left.updateLevels()
        if self.right is not None:
            self.right.level = self.right + 1
            self.right.updateLevels()


def getSwapper(U, root, levels):
    lev = U.level
    w = U.weight

    Yidx = max([-1] + [i for i in range(len(levels[lev])) if levels[lev][i].weight == w])
    if Yidx != -1:
        return levels[lev][Yidx]
    else:
        Yidx = max([-1] + [i for i in range(len(levels[lev + 1])) if levels[lev + 1][i].weight == w])
        if Yidx != -1:
            return levels[lev + 1][Yidx]
        else:
            return None


def swapSubtrees(X: Node, U: Node, levels: dict):
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

    X_levRanges = dict([(l, [float('inf'), -1]) for l in range(maxLevels)])
    U_levRanges = dict([(l, [float('inf'), -1]) for l in range(maxLevels)])

    def traceSubTree(V: Node, levRanges):
        if V is None:
            return
        levRanges[V.level][0] = min(levRanges[V.level][0], levels[V.level].index(V))
        levRanges[V.level][1] = max(levRanges[V.level][0], levels[V.level].index(V))
        traceSubTree(V.left, levRanges)
        traceSubTree(V.right, levRanges)

    XU_levDiff = X.level - U.level

    traceSubTree(X, X_levRanges)
    traceSubTree(U, U_levRanges)

    for l in range(maxLevels):
        if X_levRanges[l][1] == -1:
            X_levRanges[l][0] = 0
            X_levRanges[l][1] = 0
        if U_levRanges[l][1] == -1:
            U_levRanges[l][0] = 0
            U_levRanges[l][1] = 0
    for l in range(min(X.level, U.level), maxLevels):
        lenl = len(levels[l])
        partX = levels[l][X_levRanges[l - XU_levDiff][0]:X_levRanges[l - XU_levDiff][1]]
        partY = levels[l][U_levRanges[l + XU_levDiff][0]:U_levRanges[l + XU_levDiff][1]]
    # TODO

def updateTree(U, root, levels):
    while U is not root:
        S = getSwapper(U, root, levels)
        if S is not None:
            swapSubtrees(U, S, levels)
        U.weight += 1
        U = U.p


def adaptiveHuffman(text):
    root = Node()
    zeroNode = Node()
    first = Node()
    first.weight = 1
    first.char = text[0]
    first.level = 1
    root.weight = 1
    root.level = 0
    zeroNode.level = 1

    leaves = {'\0': zeroNode, text[0]: first}
    levels = dict([(i, []) for i in range(0, maxLevels)])
    levels[0].append(root)
    levels[1].append(zeroNode)
    levels[1].append(first)

    first.p = root
    zeroNode.p = root
    root.left = zeroNode
    root.right = first

    for c in text[1:]:
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
            upN.level = zeroNode.level
            zeroNode.level += 1
            newCharNode.level = zeroNode.level

            levels[upN.level].remove(zeroP)
            levels[upN.level].append(upN)
            levels[zeroNode.level].append(zeroNode)
            levels[newCharNode.level].append(newCharNode)

            if side == 'l':
                zeroP.left = upN
            else:
                zeroP.right = upN

            upN.left = zeroNode
            zeroNode.p = upN

            upN.right = newCharNode
            newCharNode.p = upN

            updateTree(upN, root, levels)

        else:
            leaves[c].weight += 1
            updateTree(leaves[c], root, levels)
