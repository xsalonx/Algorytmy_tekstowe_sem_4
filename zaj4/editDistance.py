def printOperationsInOnString(D, i, j, str1, str2):
    if i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            return printOperationsInOnString(D, i - 1, j - 1, str1, str2) + f"{str1[i - 1]}"
        else:
            m = min(D[j - 1][i], D[j][i - 1], D[j - 1][i - 1])
            if m == D[j][i - 1]:
                return printOperationsInOnString(D, i - 1, j, str1, str2) + f"(-{str1[i - 1]})"
            elif m == D[j - 1][i]:
                return printOperationsInOnString(D, i, j - 1, str1, str2) + f"(+{str2[j - 1]})"
            else:
                return printOperationsInOnString(D, i - 1, j - 1, str1, str2) + f"({str1[i - 1]}->{str2[j - 1]})"

    elif i == 0 and j > 0:
        return printOperationsInOnString(D, i, j - 1, str1, str2) + f"(+{str2[j - 1]})"
    elif i > 0:
        return printOperationsInOnString(D, i + 1, j, str1, str2) + f"(-{str1[i - 1]})"
    else:
        return ""


# def p

NOTHING = 0
ADD_SIGN = 1
DEL_SIGN = 2
REP_SIGN = 3


def getOperationList(D, str1, str2):
    i = len(str1)
    j = len(str2)
    operations = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            operations.append([NOTHING])
            i -= 1
            j -= 1
        else:
            m = min(D[j - 1][i], D[j][i - 1], D[j - 1][i - 1])
            if m == D[j][i - 1]:
                operations.append([DEL_SIGN, str1[i - 1]])
                i -= 1
            elif m == D[j - 1][i]:
                operations.append([ADD_SIGN, str2[j - 1]])
                j -= 1
            else:
                operations.append([REP_SIGN, str2[j - 1]])
                i -= 1
                j -= 1

    if i == 0:
        while j > 0:
            operations.append([ADD_SIGN, str2[j - 1]])
            j -= 1
    while i > 0:
        operations.append([DEL_SIGN, str1[i - 1]])
        i -= 1

    operations.reverse()
    return operations


def printOperationsBySteps(operations, str1, str2):
    currPrefix = ""
    n = len(operations)
    i = 0
    j = 0

    print_help = lambda j, cp, c: f"{j}: {currPrefix} * {str1[i:]}"
    print(0, str1)
    while j < n:
        if operations[j][0] == NOTHING:
            currPrefix += str1[i]
            i += 1
            print(f"{print_help(j + 1, currPrefix, str1[i:])} :: pass {str1[i - 1]}")
        elif operations[j][0] == ADD_SIGN:
            currPrefix += operations[j][1]
            print(f"{print_help(j + 1, currPrefix, str1[i:])} :: add {operations[j][1]}")
        elif operations[j][0] == DEL_SIGN:
            i += 1
            print(f"{print_help(j + 1, currPrefix, str1[i:])} :: del {operations[j][1]}")
        elif operations[j][0] == REP_SIGN:
            currPrefix += operations[j][1]
            i += 1
            print(f"{print_help(j, currPrefix, str1[i:])} :: swap {str1[i - 1]} with {operations[j][1]}")
        else:
            raise ValueError("Incorrect operation operator")
        j += 1

    assert currPrefix == str2
    print(f"res = {currPrefix}")


def editDistance(str1, str2):
    n1 = len(str1)
    n2 = len(str2)

    D = [[0] * (n1 + 1) for j in range(0, n2 + 1)]

    for i in range(1, n1 + 1):
        D[0][i] = i
    for i in range(1, n2 + 1):
        D[i][0] = i

    for j in range(1, n2 + 1):
        for i in range(1, n1 + 1):

            if str1[i - 1] == str2[j - 1]:
                D[j][i] = D[j - 1][i - 1]
            else:
                D[j][i] = 1 + min(D[j][i - 1], D[j - 1][i], D[j - 1][i - 1])

    return D


if __name__ == '__main__':
    str1 = ["los", "łódź", "kwintesencja", "ATGAATCTTACCGCCTCG"]
    str2 = ["kloc", "lodz", "quintessence", "ATGAGGCTCTGGCCCCTG"]
    for s1, s2 in zip(str1, str2):
        D = editDistance(s1, s2)
        print(f"str1: {s1}\nstr2: {s2}")
        opsInString = printOperationsInOnString(D, len(s1), len(s2), s1, s2)
        print(opsInString)
        operations = getOperationList(D, s1, s2)
        printOperationsBySteps(operations, s1, s2)
        print("")
