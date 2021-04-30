from LCS import get_LCS_array


def mark_diffs(arr1, arr2, C=None):
    i = len(arr1)
    j = len(arr2)

    arr1_s = [-1] * i
    arr2_s = [-1] * j

    if C is None:
        C = get_LCS_array(arr1, arr2)
    LCS_len = C[j][i]

    while i > 0 and j > 0:
        if arr1[i - 1] == arr2[j - 1]:
            arr1_s[i - 1] = j - 1
            arr2_s[j - 1] = i - 1
            i -= 1
            j -= 1
            LCS_len -= 1
        else:
            if C[j - 1][i] > C[j][i - 1]:
                j -= 1
            else:
                i -= 1

    return arr1_s, arr2_s





if __name__ == '__main__':
    src_pat = "romeo-i-julia-700.txt"
    dst1_path = "rjc_changed.txt"
    dst2_path_for_src = "rjc_unchanged.txt"

    with open(dst1_path, "r") as file:
        text1 = file.read()
    with open(dst2_path_for_src, "r") as file:
        text2 = file.read()

    T2 = text2.split('\n')
    T1 = text1.split('\n')
    print(len(T1), len(T2))
    C = get_LCS_array(T1, T2)
    print(C[-1][-1])

    d1, d2 = mark_diffs(T1, T2)
    print(d1)
    print(d2)
