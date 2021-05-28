
def kmp_string_matching(text, pattern=None, Pi=None):
    if pattern is None:
        raise ValueError
    if Pi is None:
        Pi = prefix_function(pattern)
    correctShifts = []
    q = 0
    for i in range(0, len(text)):
        while q > 0 and pattern[q] != text[i]:
            q = Pi[q - 1]
        if pattern[q] == text[i]:
            q = q + 1
        if q == len(pattern):
            correctShifts.append(i + 1 - q)
            q = Pi[q - 1]
    return correctShifts

def prefix_function(pattern):
    Pi = [0]
    k = 0
    for q in range(1, len(pattern)):
        while(k > 0 and pattern[k] != pattern[q]):
            k = Pi[k-1]
        if(pattern[k] == pattern[q]):
            k = k + 1
        Pi.append(k)
    return Pi


if __name__ == '__main__':
    text = 'abbabbabbacafdjbfsfbjsfbsjfbsjdabbaaaabba'
    pattern = 'abba'
    print(kmp_string_matching(text, pattern))