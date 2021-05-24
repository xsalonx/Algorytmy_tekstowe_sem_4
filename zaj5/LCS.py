from typing import List

def get_common_prefix_len(L: List[str]):
    k = len(L)
    i = 0
    while True:
        j = 1
        while j < k:
            if L[j - 1][i] != L[j][i]:
                break
            j += 1
        if j != k:
            break
        i += 1
    return i


# with window
def lcs_len_window(str1: str, str2: str, sentinel1=chr(1005), sentinel2=chr(1020)):
    # concatenation of strings
    Str = str1 + sentinel1 + str2 + sentinel2
    n1 = len(str1)
    n2 = len(str2)
    n = n1 + n2 + 2

    # suffix array creation and sorting
    SuffArr__ = [(Str[i:], 0) for i in range(n1)] + [(Str[i:], 1) for i in range(n1 + 1, n - 1)]
    SuffArr__.sort()
    SuffArr = [l for l, _ in SuffArr__]
    SuffTypes = [t for _, t in SuffArr__]

    i = 0
    j = 1
    #array of number of suffixes types present in window
    nums = [0, 0]
    nums[SuffTypes[i]] += 1
    nums[SuffTypes[j]] += 1
    maxLen = 0

    N = len(SuffTypes)
    while i < N - 1:
        if nums[0] * nums[1] > 0:
            length = get_common_prefix_len(SuffArr[i:j + 1])
            if maxLen < length:
                maxLen = length

            nums[SuffTypes[i]] -= 1
            i += 1

        elif j < N - 1:
            j += 1
            nums[SuffTypes[j]] += 1
        else:
            return maxLen

    return maxLen


# dynamic
def lcs_len_dynamic(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    D = [[0 for _ in range(0, n1 + 1)] for __ in range(0, n2 + 1)]

    maxLen = 0
    for i in range(1, n1 + 1):
        for j in range(0, n2 + 1):

            if str1[i - 1] == str2[j - 1]:
                D[j][i] = D[j - 1][i - 1] + 1
                maxLen = max(maxLen, D[j][i])

    return maxLen















###############################################
def get_max_prefix(L: List[str]):
    k = len(L)

    i = 0
    while True:
        j = 1
        while j < k:
            if L[j - 1][i] != L[j][i]:
                break
            j += 1
        if j != k:
            break
        i += 1
    return i, L[0][:i]


def find_LCS(str1: str, str2: str, sentinel1=chr(1005), sentinel2=chr(1020)):
    Str = str1 + sentinel1 + str2 + sentinel2
    n1 = len(str1)
    n2 = len(str2)
    n = n1 + n2 + 2

    SuffArr__ = [(Str[i:], 0) for i in range(len(str1))] + [(Str[i:], 1) for i in range(len(str1) + 1, len(Str) - 1)]
    SuffArr__.sort()
    SuffArr = [l for l, _ in SuffArr__]
    SuffTypes = [t for _, t in SuffArr__]

    i = 0
    j = 1
    nums = [0, 0]
    nums[SuffTypes[i]] += 1
    nums[SuffTypes[j]] += 1
    Prefs = set()
    maxLen = 0

    N = len(SuffTypes)
    while i < N - 1:
        if nums[0] * nums[1] > 0:
            length, pref = get_max_prefix(SuffArr[i:j + 1])
            if maxLen < length:
                maxLen = length
                Prefs.clear()
                Prefs.add(pref)
            elif maxLen == length:
                Prefs.add(pref)

            nums[SuffTypes[i]] -= 1
            i += 1

        elif j < N - 1:
            j += 1
            nums[SuffTypes[j]] += 1

    return maxLen, Prefs
