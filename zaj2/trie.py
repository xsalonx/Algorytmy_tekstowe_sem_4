

class TrieNode:
    def __init__(self):
        self.children = {}
        self.label = ''
        self.depth = -1
        self.parent = None

    def addSuffix(self, label, END_SIGN):
        if not label:
            return
        if label[0] not in self.children:
            self.children[label[0]] = TrieNode()
            self.children[label[0]].label = label[0]
            self.children[label[0]].parent = self
            self.children[label[0]].depth = self.depth + 1
        self.children[label[0]].addSuffix(label[1:], END_SIGN)

    def searchSubPattern(self, subPattern):
        if not subPattern:
            return True
        if subPattern[0] in self.children:
            return self.children[subPattern[0]].searchSubPattern(subPattern[1:])
        else:
            return False

    def getSubTreeSize(self):
        return 1 + sum([n.getSubTreeSize() for n in self.children.values()])

class Trie:
    def __init__(self, text, ignoreWhitespaces=False):
        self.root = TrieNode()
        self.root.depth = 0
        self.END_SIGN = text[-1]
        for beg in range(len(text) - 1, -1, -1):
            suffix = text[beg:]
            self.root.addSuffix(suffix, self.END_SIGN)

    def search(self, pattern):
        return self.root.searchSubPattern(pattern)

    def getSize(self):
        return self.root.getSubTreeSize()

def printTrie(node: TrieNode, level=0):
    for a in node.children:
        print(" " * level + f"{a}::{level}")
        printTrie(node.children[a], level + 1)


if __name__ == '__main__':
    texts = ['bbbd', 'aabbabd', 'ababcd', 'abcbccd', 'ababababd']
    actFile = open('1997_714.txt', encoding='UTF-8')
    actText = actFile.read(300) + '$'

    text = actText
    sT = Trie(text)

    printTrie(sT.root)
    print(sT.getSize())
    for i in range(len(text) - 1):
        for j in range(i, len(text)):
            pattern = text[i:j]
            if not sT.search(pattern):
                exit(1)
