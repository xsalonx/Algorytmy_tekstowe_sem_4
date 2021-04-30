

def get_LCS_array(arr1, arr2, cmp=None):

    if cmp is None:
        cmp = lambda x, y: x == y
    n1 = len(arr1)
    n2 = len(arr2)
    C = [[0] * (n1 + 1) for _ in range(n2 + 1)]


    for j in range(1, n2 + 1):
        for i in range(1, n1 + 1):

            if cmp(arr1[i - 1], arr2[j - 1]):
                C[j][i] = C[j - 1][i - 1] + 1
            else:
                C[j][i] = max(C[j - 1][i], C[j][i - 1])

    return C

def cmpLCSs(s1, s2, cmp=None):
    if cmp is None:
        cmp = lambda x, y: x == y
    n = len(s1)
    for i in range(0, n):
        if not cmp(s1[i], s2[i]):
            return False
    return True

def get_all_LCSs(arr1, arr2, i, j, C):

    if i == 0 or j == 0:
        return [[]]
    LCSs = []
    LCSs1 = []
    LCSs2 = []

    if arr1[i - 1] == arr2[j - 1]:
        LCSs = get_all_LCSs(arr1, arr2, i - 1, j - 1, C)
        LCSs = [s + [i - 1, j - 1] for s in LCSs]

    if C[j][i - 1] == C[j - 1][i] and C[j][i - 1] == C[j][i]:
        LCSs1 = get_all_LCSs(arr1, arr2, i - 1, j, C)
        LCSs2 = get_all_LCSs(arr1, arr2, i, j - 1, C)

    elif C[j][i - 1] > C[j - 1][i] and C[j][i - 1] == C[j][i]:
        LCSs1 = get_all_LCSs(arr1, arr2, i - 1, j, C)
    elif C[j][i - 1] < C[j - 1][i] and C[j - 1][i] == C[j][i]:
        LCSs2 = get_all_LCSs(arr1, arr2, i, j - 1, C)

    return LCSs + LCSs1 + LCSs2

def get_LCS(arr1, arr2, C=None):

    n1 = len(arr1)
    n2 = len(arr2)

    if C is None:
        C = get_LCS_array(arr1, arr2)
    LCS_len = C[n2][n1]
    LCS = [0] * LCS_len

    while n1 > 0 and n2 > 0:
        if arr1[n1 - 1] == arr2[n2 - 1]:
            LCS[LCS_len - 1] = arr1[n1 - 1]
            n1 -= 1
            n2 -= 1
            LCS_len -= 1
        else:
            if C[n2 - 1][n1] > C[n2][n1 - 1]:
                n2 -= 1
            else:
                n1 -= 1


    return LCS

import numpy as np


if __name__ == '__main__':

    n = 10000
    arrO = np.random.randint(0, 10, n)
    m = 1000
    gets = np.unique(np.random.randint(0, n-1, m))
    arrS = arrO[gets]

    print(arrO)
    print(gets)
    print(arrS, len(arrS))
    print(get_LCS_array(arrO, arrS)[-1][-1])


