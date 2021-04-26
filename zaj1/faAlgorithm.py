# import re



def finiteAuto_StringMatching(text, pattern=None, delta=None):
    if pattern is None and delta is None:
        raise ValueError
    if delta is None:
        delta = constructTransMatrix(pattern)
    correctShifts = []
    q = 0
    n = len(text)
    m = len(delta)
    for i in range(n):
        q = delta[q].get(text[i], 0)
        if q == m - 1:
            correctShifts.append(i+1-q)
    return correctShifts

def isPatternSuffixOf(patttern, text):
    k = len(patttern)
    m = len(text)
    if k > m:
        return False
    else:
        return patttern == text[m - k:]

def constructTransMatrix(pattern):
    delta = []
    alphabet = set(pattern)
    n = len(pattern)
    for q in range(n + 1):
        delta.append({})
        for a in alphabet:
            k = q + 1
            while not isPatternSuffixOf(pattern[:k], pattern[:q] + a):
                k -= 1
            delta[q][a] = k
    return delta

if __name__ == '__main__':
    text = 'abbabbabbacafdjbfsfbjsfbsjfbsjdabbaaaabba'
    pattern = 'abba'
    print(finiteAuto_StringMatching(text, pattern))

    pass







