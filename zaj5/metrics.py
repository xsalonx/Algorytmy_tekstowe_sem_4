import numpy as np
from collections import defaultdict
from LCS import *

def make_freq_letters_vectors_from_text(s1: str, s2: str):
    A = list(set(s1) | set(s2))
    v1 = [s1.count(a) for a in A]
    v2 = [s2.count(a) for a in A]

    return np.array(v1), np.array(v2)


def make_nGram_freq_vectors(s1, s2, n):
    l1 = len(s1)
    l2 = len(s2)
    assert n < min(l1, l2)

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




# lcs metric

def lcs_distance(s1, s2):
    return 1 - lcs_len1(s1, s2) / max(len(s1), len(s2))


# DICE metric

def dice_distance(s1, s2, n):
    v1, v2, _ = make_nGram_freq_vectors(s1, s2, n)
    count = lambda v: np.sum(v > 0)

    return 1 - 2 * count(v1 * v2) / (count(v1) + count(v2))

def cos_distance(s1, s2, n=3):
    v1, v2, _ = make_nGram_freq_vectors(s1, s2, n)
    norm = lambda v: np.linalg.norm(v)
    return norm(v1 - v2) / (norm(v1) * norm(v2))

def euclidean_distance(s1, s2, n=3):
    v1, v2, _ = make_nGram_freq_vectors(s1, s2, n)
    return np.linalg.norm(v1 - v2)


if __name__ == '__main__':
    s1 = "aba"
    s2 = "aabba gggggggggggggggggggggasdcasdcasdcasdca"

    n = 1
    print(make_nGram_freq_vectors(s1, s2, n))
    print(f"euc :: {euclidean_distance(s1, s2, n)}")
    print(f"cos :: {cos_distance(s1, s2, n)}")
    print(f"lcs :: {lcs_distance(s1, s2)}")
    print(f"dic :: {dice_distance(s1, s2, n)}")
