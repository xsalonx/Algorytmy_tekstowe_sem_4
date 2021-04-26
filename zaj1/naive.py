
def areStringsEq(str1, str2):
    n = len(str1)
    m = len(str2)
    if n != m:
        return False
    for i in range(n):
        if str1[i] != str2[i]:
            return False
    return True

def naiveStringMatching(text, pattern):
    correctShift = []

    n = len(text)
    m = len(pattern)
    for s in range(n - m + 1):
        if areStringsEq(text[s:s+m], pattern):
        # if text[s:s+m] == pattern:
            correctShift.append(s)
    return correctShift

if __name__ == '__main__':

    text = 'abbabbabbacafdjbfsfbjsfbsjfbsjdabbaaaabba'
    pattern = 'abba'
    print(naiveStringMatching(text, pattern))
















