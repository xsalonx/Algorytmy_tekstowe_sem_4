from LCS import get_LCS_array


def mark_diffs(arr1, arr2, C=None):
    i = len(arr1)
    j = len(arr2)

    d1 = [-1] * i
    d2 = [-1] * j

    if C is None:
        C = get_LCS_array(arr1, arr2)
    LCS_len = C[j][i]

    while i > 0 and j > 0:
        if arr1[i - 1] == arr2[j - 1]:
            d1[i - 1] = j - 1
            d2[j - 1] = i - 1
            i -= 1
            j -= 1
            LCS_len -= 1
        else:
            if C[j - 1][i] > C[j][i - 1]:
                j -= 1
            else:
                i -= 1

    return d1, d2


def print_diffs(text1, text2):
    T2 = text2.split('\n')
    T1 = text1.split('\n')
    print(len(T1), len(T2))
    C = get_LCS_array(T1, T2)
    print(C[-1][-1])

    d1, d2 = mark_diffs(T1, T2)

    i = 0
    j = 0
    k = 0
    n1 = len(T1)
    n2 = len(T2)
    while i < n1 or j < n2:
        while i < n1:
            if d1[i] == -1:
                k += 1
                print(f"diff {k}; file 1; line {i}; <{T1[i]}>")
                i += 1
                break
            i += 1
        while j < n2:
            if d2[j] == -1:
                k += 1
                print(f"diff {k}; file 2; line {j}; <{T2[j]}>")
                j += 1
                break
            j += 1



if __name__ == '__main__':
    src_pat = "romeo-i-julia-700.txt"
    dst1_path = "rjc_changed.txt"
    dst2_path_for_src = "rjc_unchanged.txt"

    with open(dst1_path, "r") as file:
        text1 = file.read()
    with open(dst2_path_for_src, "r") as file:
        text2 = file.read()

    print_diffs(text1, text2)





