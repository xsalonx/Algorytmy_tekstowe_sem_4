

def find_LCS(arr1, arr2, n1, n2):

    C = []

    for j in range(0, n2 + 1):
        C.append([0] * (n1 + 1))

    for j in range(1, n2 + 1):
        for i in range(1, n1 + 1):

            if arr1[i - 1] == arr2[j - 1]:
                C[j][i] = C[j - 1][i - 1] + 1
            else:
                C[j][i] = max(C[j - 1][i], C[j][i - 1])

    return C

def cmpLCSs(s1, s2):
    n = len(s1)
    for i in range(0, n):
        if s1[i] != s2[i]:
            return False
    return True

def getAllLCSs(arr1, arr2, n1, n2, C):

    if n1 == 0 or n2 == 0:
        return [[]]
    LCSs = []
    LCSs1 = []
    LCSs2 = []

    if arr1[n1 - 1] == arr2[n2 - 1]:
        LCSs = getAllLCSs(arr1, arr2, n1 - 1, n2 - 1, C)
        LCSs = [s + [n1 - 1, n2 - 1] for s in LCSs]

    if C[n2][n1 - 1] == C[n2 - 1][n1] and C[n2][n1 - 1] == C[n2][n1]:
        LCSs1 = getAllLCSs(arr1, arr2, n1 - 1, n2, C)
        LCSs2 = getAllLCSs(arr1, arr2, n1, n2 - 1, C)

    elif C[n2][n1 - 1] > C[n2 - 1][n1] and C[n2][n1 - 1] == C[n2][n1]:
        LCSs1 = getAllLCSs(arr1, arr2, n1 - 1, n2, C)
    elif C[n2][n1 - 1] < C[n2 - 1][n1] and C[n2 - 1][n1] == C[n2][n1]:
        LCSs2 = getAllLCSs(arr1, arr2, n1, n2 - 1, C)

    return LCSs + LCSs1 + LCSs2

def get_LCS(arr1, arr2):

    n1 = len(arr1)
    n2 = len(arr2)

    C = find_LCS(arr1, arr2, n1, n2)
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

    # for i in range(0, len(arr2)+1):
    #     print(C[i])

    return LCS




if __name__ == '__main__':
    arr1 = [1, 7, 7, 8, 0, 0, 7, 1, 7, 7, 8, 0, 0, 7]
    arr2 = [1, 6, 7, 0, 0, 8, 0, 7, 1, 6, 7, 0, 0, 8, 0, 7]
    n1 = len(arr1)
    n2 = len(arr2)

    C = find_LCS(arr1, arr2, n1, n2)

    print("  ", arr1)
    for i in range(0, len(C)):
        print(C[i])
    print("")
    AllLCSs = getAllLCSs(arr1, arr2, n1, n2, C)
    i = 0
    while i < len(AllLCSs) - 1:
        j = i + 1
        while j < len(AllLCSs):
            if cmpLCSs(AllLCSs[i], AllLCSs[j]):
                AllLCSs.pop(j)
            else:
                j += 1
        i += 1

    for i in range(0, len(AllLCSs)):
        print(AllLCSs[i], i)




