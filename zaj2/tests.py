
import random
from Tekstowe.zaj2 import trie, suffixTree
from time import time_ns
from matplotlib import pyplot as plt
import numpy as np

def getTime():
    return time_ns()/1000000

def compareStructures(text, numberOfRepeats=10000):

    trieTime = 0
    suffixTTime = 0
    for r in range(numberOfRepeats):
        t1 = getTime()
        trieT = trie.Trie(text)
        t2 = getTime()
        suffixT = suffixTree.SuffixTree(text)
        t3 = getTime()

        trieTime += (t2 - t1)
        suffixTTime += (t3 - t2)
    trieTime /= numberOfRepeats
    suffixTTime /= numberOfRepeats

    print(f"For text <{text}> construction time:\n      trie: {trieTime} ms\n        size: {trieT.getSize()}\n      suffix tree: {suffixTTime} ms\n        size: {suffixT.getSize()}")

def genRandTextAndPattern(alphabetSize=2, textSize=100000, patternSize=2):
    assert alphabetSize >= 2
    assert textSize >= patternSize
    assert patternSize > 0
    alphabet = [chr(i) for i in range(97, 97 + alphabetSize)]
    text = ''
    for _ in range(textSize):
        text += alphabet[random.randint(0, alphabetSize - 1)]
    pattern = ''
    for _ in range(patternSize):
        pattern += alphabet[random.randint(0, alphabetSize - 1)]

    return text, pattern

def randTextTest(alphabetSize=2, textSizeLow=100, step=100, stepsNumb=100, numberOfRepeats=2):

    data = {}

    for i in range(stepsNumb):
        size = textSizeLow + i * step
        print(size)
        data[size] = [0., 0, 0., 0]
        trieTime = 0
        suffixTime = 0
        for _ in range(numberOfRepeats):
            text, _ = genRandTextAndPattern(alphabetSize, size)
            text += '$'
            t1 = getTime()
            tT = trie.Trie(text)
            t2 = getTime()
            sT = suffixTree.SuffixTree(text)
            t3 = getTime()
            trieTime += (t2 - t1)
            suffixTime += (t3 - t2)
        data[size][0] = trieTime/numberOfRepeats
        data[size][1] = tT.getSize()
        data[size][2] = suffixTime/numberOfRepeats
        data[size][3] = sT.getSize()


    return data

if __name__ == '__main__':
    texts = ['bbbd', 'aabbabd', 'ababcd', 'abcbccd', 'ababababd']
    actFile = open('1997_714.txt', encoding='UTF-8')
    actText = actFile.read(300) + '$'

    # for i in range(len(texts)):
    #     compareStructures(texts[i], numberOfRepeats=10000)
    # compareStructures(actText, numberOfRepeats=2)
    # print(len(actText))

    data = randTextTest(alphabetSize=5, textSizeLow=50, step=4, stepsNumb=20, numberOfRepeats=5)
    X = data.keys()
    d = list(data.values())
    trieTime = [e[0] for e in d]
    trieSize = [e[1] for e in d]
    suffTime = [e[2] for e in d]
    suffSize = [e[3] for e in d]

    _, ax = plt.subplots(1, 2, figsize=(16, 8))
    ax[0].scatter(X, trieTime)
    ax[0].scatter(X, suffTime)
    ax[0].set_title('Run time for variable length of text')
    ax[0].set_xlabel('size of text')
    ax[0].set_ylabel('time [ms]')
    ax[0].legend(["trie", "suffix"])

    ax[1].scatter(X, trieSize)
    ax[1].scatter(X, suffSize)
    ax[1].set_title('Size of structure for variable length of text')
    ax[1].set_xlabel('size of text')
    ax[1].set_ylabel('size')
    ax[1].legend(["trie", "suffix"])
    plt.show()
