
from spacy.tokenizer import Tokenizer
from spacy.lang.pl import Polish

import numpy as np

if __name__ == '__main__':

    with open("romeo-i-julia-700.txt", "r") as file:
        text = file.read()

    nlp = Polish()
    tokenizer = Tokenizer(nlp.vocab)

    tokens = tokenizer(text)
    n = len(tokens)

