import numpy as np
from collections import defaultdict
from LCS import *

from text_preprocessing import *


def get_nGram_freq_vectors(s1, s2, n):
    l1 = len(s1)
    l2 = len(s2)

    d1 = defaultdict(lambda: 0)
    d2 = defaultdict(lambda: 0)
    for i in range(l1 - n + 1):
        d1[s1[i:i + n]] += 1
    for i in range(l2 - n + 1):
        d2[s2[i:i + n]] += 1
    nGrams = list(d2.keys() | d1.keys())

    v1 = np.array([d1[nG] for nG in nGrams])
    v2 = np.array([d2[nG] for nG in nGrams])

    return v1, v2, nGrams


def lcs_distance(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if n1 == n2 == 0:
        return 1
    return 1 - lcs_len_window(s1, s2) / max(len(s1), len(s2))


def dice_distance(s1, s2, n=3):
    v1, v2, _ = get_nGram_freq_vectors(s1, s2, n)
    count = lambda v: np.sum(v > 0)

    c1 = count(v1)
    c2 = count(v2)
    if c1 + c2 == 0:
        return 0

    return 1 - 2 * count(v1 * v2) / (c1 + c2)


def cos_distance(s1, s2, n=3):
    v1, v2, _ = get_nGram_freq_vectors(s1, s2, n)
    norm = lambda v: np.linalg.norm(v)
    n1 = norm(v1)
    n2 = norm(v2)
    if n1 + n2 == 0:
        return 0
    return norm(v1 - v2) / (n1 + n2)


def euclidean_distance(s1, s2, n=3):
    v1, v2, _ = get_nGram_freq_vectors(s1, s2, n)
    return np.linalg.norm(v1 - v2)


def levenstein_distance(str1, str2):
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

    return D[-1][-1]


# For generating text files with precomputed distances
def main(reduced, name):
    if name == "eucl":
        d = euclidean_distance
    elif name == "dice":
        d = dice_distance
    elif name == "lcs":
        d = lcs_distance
    elif name == "cos":
        d = cos_distance
    elif name == 'leven':
        d = levenstein_distance

    with open("lines.txt") as file:
        text = file.read()
    if not reduced:
        Lines = text.split("\n")
    else:
        Lines = get_list_of_lines(text, 200, 0, 0, reduced=True)

    n = len(Lines)

    file = open(f"{name}_{'reduced' if reduced else ''}.txt", "a")
    for i in range(1, n):
        for j in range(i):
            if j % 50 == 0:
                print(i, j, "leven")
            file.write(f"{i}:{j}:{d(Lines[i], Lines[j])}\n")


if __name__ == '__main__':
    name = 'leven'
    reduced = False
    main(reduced, name)



