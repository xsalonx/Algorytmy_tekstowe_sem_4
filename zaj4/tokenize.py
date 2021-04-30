import string

from spacy.tokenizer import Tokenizer
from spacy.lang.pl import Polish

import numpy as np
from LCS import get_LCS_array
from random_change import random_changes_in_file


if __name__ == '__main__':
    src_pat = "romeo-i-julia-700.txt"
    dst1_path = "rjc_changed.txt"
    dst2_path_for_src = "rjc_unchanged.txt"

    random_changes_in_file(dst1_path, dst2_path_for_src, src_pat)

    nlp = Polish()
    tokenizer = Tokenizer(nlp.vocab)

    with open(dst1_path, "r") as file:
        text1 = file.read()
    with open(dst2_path_for_src, "r") as file:
        text2 = file.read()


    doc1 = tokenizer(text1)
    doc2 = tokenizer(text2)

    print(len(doc1), len(doc2))

    isEq = lambda t1, t2: t1.text == t2.text
    C = get_LCS_array(doc1, doc2, isEq=isEq)
    print(C[len(doc2)][len(doc1)])




