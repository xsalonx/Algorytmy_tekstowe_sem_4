import random
from time import time_ns
from zaj1.faAlgorithm import finiteAuto_StringMatching, constructTransMatrix
from zaj1.naive import naiveStringMatching
from zaj1.KMP import kmp_string_matching, prefix_function
from matplotlib import pyplot as plt
import numpy as np

def getTime_ms():
    return time_ns() / 1000000

def forArticleTimeTest():
    legend = ['naiveTime', 'faDeltaConstTime', 'faTime', 'piConstTime', 'KMPTime']

    ustawa = open('ustawa.txt', 'r', encoding='UTF-8')
    text = ustawa.read()
    # print(text)
    pattern = 'art'


    T = np.array(times(text, pattern))
    for _ in range(5):
        T += np.array(times(text, pattern))

    print("Article::")
    for i in range(len(legend)):
        print(f"    {legend[i]}: {T[i]} ms")

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

def testForRandomText_VarLengthOfText():
    legend = ['naiveTime', 'faDeltaConstTime', 'faTime', 'piConstTime', 'KMPTime']

    measurementsPoints = [100 + 100*i for i in range(15, 30)]
    timeArray = []
    alphabetSize = 2
    patternSize = 100
    repeatsPerMeasurements = 3
    for textSize in measurementsPoints:

        text, pattern = genRandTextAndPattern(alphabetSize=alphabetSize, textSize=textSize, patternSize=patternSize)
        T = np.array(times(text, pattern))
        for _ in range(repeatsPerMeasurements - 1):
            text, pattern = genRandTextAndPattern(alphabetSize=alphabetSize, textSize=textSize, patternSize=patternSize)
            T += np.array(times(text, pattern))

        timeArray.append(T/repeatsPerMeasurements)

    for i in range(len(timeArray[0])):
        plt.scatter(measurementsPoints, [timeArray[m][i] for m in range(len(measurementsPoints))], label=legend[i])

    plt.title('Run time for variable length of text')
    plt.xlabel('size of text')
    plt.ylabel('time [ms]')
    plt.legend()
    plt.show()

def testForRandomText_VarLengthOfPattern():
    legend = ['naiveTime', 'faDeltaConstTime', 'faTime', 'piConstTime', 'KMPTime']

    measurementsPoints = [5000 * i for i in range(1, 20)]
    timeArray = []
    alphabetSize = 10
    repeatsPerMeasurements = 5
    textSize = 100000
    for patternSize in measurementsPoints:

        text, pattern = genRandTextAndPattern(alphabetSize=alphabetSize, textSize=textSize, patternSize=patternSize)
        T = np.array(times(text, pattern, without_fintieAuto=True))
        for _ in range(repeatsPerMeasurements - 1):
            text, pattern = genRandTextAndPattern(alphabetSize=alphabetSize, textSize=textSize, patternSize=patternSize)
            T += np.array(times(text, pattern, without_fintieAuto=True))

        timeArray.append(T / repeatsPerMeasurements)

    for i in range(len(timeArray[0])):
        plt.scatter(measurementsPoints, [timeArray[m][i] for m in range(len(measurementsPoints))], label=legend[i])

    plt.title('Run time for variable length of pattern')
    plt.xlabel('size of pattern')
    plt.ylabel('time [ms]')
    plt.legend()
    plt.show()


def badCaseOfNaive():
    legend = ['naiveTime', 'faDeltaConstTime', 'faTime', 'piConstTime', 'KMPTime']

    n = 100
    textElement = 'abc'
    text = textElement * n * 2
    pattern = textElement * n

    T = np.array(times(text, pattern))
    for _ in range(5):
        T += np.array(times(text, pattern))

    print("Article::")
    for i in range(len(legend)):
        print(f"    {legend[i]}: {T[i]} ms")


def times(text, pattern, without_fintieAuto=False):
    t1 = getTime_ms()
    res1 = naiveStringMatching(text, pattern)
    t2 = getTime_ms()
    if not without_fintieAuto:
        delta = constructTransMatrix(pattern)

    t3 = getTime_ms()
    res2 = []
    if not without_fintieAuto:
        res2 = finiteAuto_StringMatching(text, delta=delta)
    t4 = getTime_ms()
    pi = prefix_function(pattern)
    t5 = getTime_ms()
    res3 = kmp_string_matching(text, pattern=pattern, pi=pi)
    t6 = getTime_ms()

    print(len(res1), len(res2), len(res3))
    # print(f"{t2 - t1}, {t3 - t2} + {t4 - t3}, {t5 - t4} + {t6 - t5}")
    return t2 - t1, t3 - t2, t4 - t3, t5 - t4, t6 - t5


if __name__ == '__main__':

    # forArticleTimeTest()
    # testForRandomText_VarLengthOfText()
    # testForRandomText_VarLengthOfPattern()
    badCaseOfNaive()

