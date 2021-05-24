import re
from collections import defaultdict

import numpy as np

DELIMITERS = ",;|<>*&^' \"%$#@!()\\\/.\[\]\+\-:"

def is_pos_int(s: str):
    return s.isdigit() or s[1:].isdigit()

def get_stop_list(text, n_most_frequent=0):
    words = re.split(f"[{DELIMITERS}\n]+", text)
    if words.__contains__(''):
        words.remove('')

    D = defaultdict(lambda: 0, [])
    for w in words:
        D[w] += 1

    freq = [(D[w], w) for w in D.keys() if len(w) and not is_pos_int(w)]
    freq.sort(reverse=True)
    if n_most_frequent == 0:
        n_most_frequent = len(freq)
    else:
        n_most_frequent = min(n_most_frequent, len(freq))
    return freq[:n_most_frequent], n_most_frequent

def remove_words_with_delimiters(text, words):
    text = re.sub(f"[{DELIMITERS}]+", " ", text)
    for w in words:
        text = re.sub(f" {w} ", " ", text)
    return text

def get_list_of_lines(text, n_most_frequent, lines_n=0, min_line_len=0, reduced=False):
    if reduced:
        words_to_cut, _ = get_stop_list(text, n_most_frequent)
        text = remove_words_with_delimiters(text, [w for _, w in words_to_cut])
    else:
        text = re.sub(f"[{DELIMITERS}]+", " ", text)
        text = re.sub("[ ]+", " ", text)
    Lines = text.split("\n")
    if lines_n == 0:
        lines_n = len(Lines)

    if min_line_len == 0:
        return Lines[:lines_n]
    else:
        return [l for l in Lines[:lines_n] if len(l) >= min_line_len]


if __name__ == '__main__':

    with open("lines.txt") as file:
        text = file.read()
    stopList, _ = get_stop_list(text, 50)
    i = 0
    n  = len(stopList)
    while i < n:
        for _ in range(4):
            if i < len(stopList):
                print(stopList[i], end="  ::  ")
            i += 1
        print("")


