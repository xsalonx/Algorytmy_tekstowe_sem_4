class SuffixTreeNode:
    def __init__(self):
        self.children = {}
        self.label = ''
        self.depth = 0
        self.parent = None

    def childByFirstLetter(self, letter):
        return self.children.get(letter, (None, None))[1]

    def calcDepths(self):
        for (_, child) in self.children.values():
            child.depth = self.depth + 1
            child.calcDepths()

    def breakPath(self, label):
        (_range, child) = self.children[label[0]]
        prev_label = child.label
        break_node = SuffixTreeNode()
        break_node.depth = self.depth + 1

        self.children.pop(label[0])
        self.children[label[0]] = ((_range[0], _range[0] + len(label) - 1), break_node)
        break_node.parent = self
        break_node.label = label
        child.parent = break_node
        child.label = prev_label[len(label):]
        break_node.children[prev_label[len(label):][0]] = ((_range[0] + len(label), _range[1]), child)

        break_node.calcDepths()

        return break_node

    def slowFind(self, label):
        child = self.childByFirstLetter(label[0])
        if not child:
            return self
        for i in range(1, len(child.label)):
            if (child.label[i] != label[i]):
                return self.breakPath(label[:i])
        return child.slowFind(label[len(child.label):])

    def getSubTreeSize(self):
        return 1 + sum([n.getSubTreeSize() for (_, n) in self.children.values()])

    def retAllDepths(self):
        if len(self.children) == 0:
            return [self.depth]
        # return [d for res in [n.retAllDepth() for (_, n) in self.children.values()] for d in res]
        res = []
        for (_, n) in self.children.values():
            r = n.retAllDepths()
            if r:
                for x in r:
                    res.append(x)
        return res

    def __repr__(self):
        return f"label: {self.label}, depth: {self.depth}, children: {self.children.keys()}"


class SuffixTree:
    def __init__(self, text):
        self.root = SuffixTreeNode()
        self.text = text
        self.END_SIGN = text[-1]

        for i in range(0, len(text)):
            suffix = text[i:]
            parent = self.root.slowFind(suffix)
            label = suffix[parent.depth:]

            child = SuffixTreeNode()
            child.parent = parent
            child.depth = parent.depth + 1
            child.label = label

            parent.children[label[0]] = ((i + parent.depth, len(text) - 1), child)

    def search(self, pattern):
        node = self.root
        i = 0
        while i < len(pattern):
            (_, nextNode) = node.children.get(pattern[i], (None, None))
            if not nextNode:
                return None
            j = 0
            while j < len(pattern) - i and j < len(nextNode.label):
                if pattern[i + j] != nextNode.label[j]:
                    return None
                j += 1
            i += j
            node = nextNode

        if i == len(pattern):
            x = node.retAllDepths()
            return set([len(self.text)-k for k in x])
        return None

    def getSize(self):
        return self.root.getSubTreeSize()


def printTrie(node: SuffixTreeNode):
    for a in node.children:
        print(" " * node.depth + f"{a}::{node.depth} {node.children[a][0]} {node.children[a][1].label}")
        printTrie(node.children[a][1])


# if __name__ == '__main__':
#     texts = ['bbbd', 'aabbabd', 'ababcd', 'abcbccd', 'ababababd']
#     actFile = open('1997_714.txt', encoding='UTF-8')
#     actText = actFile.read(300) + '$'
#
#     text = texts[1]
#     sT = SuffixTree(text)
#
#     printTrie(sT.root)
#     print(sT.getSize())
#     for i in range(len(text) - 1):
#         for j in range(i+1, len(text)):
#             pattern = text[i:j]
#             res = sT.search(pattern)
#             print(pattern, res)
#             if not res:
#                 exit(1)
