
from spacy.tokenizer import Tokenizer
from spacy.lang.pl import Polish

PART_TO_REMOVE = 0.03

from random import randint

def random_changes_in_file(dst1_path, dst2_path_for_src, src_path):


    text = ""
    with open(src_path, "r") as file:
        text = file.read()

    # text = text.replace("\n", " ")

    nlp = Polish()
    tokenizer = Tokenizer(nlp.vocab)

    doc = tokenizer(text)
    T = [t for t in doc]
    n = len(T)
    for i in range(int(n * PART_TO_REMOVE)):
        del T[randint(0, len(T) - 1)]

    with open(dst1_path, "w+") as file:
        for i in range(len(T)):
            file.write(T[i].text + " ")

    with open(dst2_path_for_src, "w+") as file:
        for i in range(len(doc)):
            file.write(doc[i].text + " ")


if __name__ == '__main__':

    src_pat = "romeo-i-julia-700.txt"
    dst1_path = "rjc_changed.txt"
    dst2_path_for_src = "rjc_unchanged.txt"

    random_changes_in_file(dst1_path, dst2_path_for_src, src_pat)

    with open("rjc_changed.txt", "r") as file:
        text1 = file.read()
    with open("rjc_unchanged.txt", "r") as file:
        text2 = file.read()

    print(len(text1), len(text2))




