from aho_corasic import *
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def search_2d_pattern(text: str,
                      patterns, FIRST_CHAR=48):  # patterns - list of 2d patterns; each given as "<line1>\n<line2>\n<line3>..."
    # TODO not so effective parsing text and patterns ...,  but works

    Lines = text.split("\n")
    Patterns = [p.split("\n") for p in patterns]
    shape = (len(Lines), len(max(Lines, key=lambda t: len(t))))
    search_matrix = np.zeros(shape=shape, dtype=int)

    subpatterns_searcher = Searcher()
    subpatterns_searcher.add_all([p for pc in Patterns for p in pc])

    Pos = [subpatterns_searcher.search(t) for t in Lines]
    for j, pos in enumerate(Pos):
        for i, word_idx in pos:
            search_matrix[j, i] = word_idx

    pos_searcher = Searcher()
    pos_search_patterns = ["".join([chr(FIRST_CHAR + subpatterns_searcher.pattern_idx(p)) for p in pc]) for pc in Patterns]
    pos_searcher.add_all(pos_search_patterns)

    columns_as_text = ["".join([chr(i + FIRST_CHAR) for i in search_matrix[:, c]]) for c in range(shape[1])]
    res = [pos_searcher.search(c) for c in columns_as_text]

    res = [(j, i, k) for i, col in enumerate(res) for j, k in col]
    Res = [[(i, chr(96 + k)) for j, i, k in res if j == r] for r in range(shape[0])]

    return Res, search_matrix


def search_2d_image_pattern(im_path, pattern_path, FIRST_CHAR=48):
    image = np.array(Image.open(im_path).convert('L'))
    pattern_im = np.array(Image.open(pattern_path).convert('L'))

    # deg = 100
    #
    # d = image < deg
    # image[d] = 0
    # image[np.logical_not(d)] = 255
    # d = pattern_im < deg
    # pattern_im[d] = 0
    # pattern_im[np.logical_not(d)] = 255

    image_text = "\n".join(["".join([chr(image[j, i] + FIRST_CHAR) for i in range(image.shape[1])]) for j in range(image.shape[0])])
    pattern_text = ["\n".join(["".join([chr(pattern_im[j, i] + FIRST_CHAR) for i in range(pattern_im.shape[1])]) for j in range(pattern_im.shape[0])])]

    Res, search_matrix = search_2d_pattern(image_text, pattern_text, FIRST_CHAR=FIRST_CHAR)

    return Res, search_matrix

def main_im(whole_text_im_file_path, patter_im_file, show_each_ad=False):

    Res, search_matrix = search_2d_image_pattern(whole_text_im_file_path, patter_im_file)

    [print(j, r) for j, r in enumerate(Res) if len(r) > 0]

    im = np.array(Image.open(whole_text_im_file_path).convert('L'))
    plt.imshow(im)
    for j, r in enumerate(Res):
        for i, v in r:
            plt.scatter([i], [j], color="red")

    if show_each_ad:
        X = []
        Y = []
        for idx in np.ndindex(search_matrix.shape):
            if search_matrix[idx] > 0:
                X.append(idx[1])
                Y.append(idx[0])
        plt.scatter(X, Y, s=5, color="green")
    plt.show()

def main_txt(path, patterns):
    with open(path) as f:
        text = f.read()
    Res, _ = search_2d_pattern(text, patterns, FIRST_CHAR=97)
    [print(j, r) for j, r in enumerate(Res) if len(r) > 0]


if __name__ == '__main__':

    text_path = "data/haystack.txt"
    patterns = [f"{chr(i)}\n{chr(i)}" for i in range(97, 123)]
    # main_txt(text_path, patterns)


    whole_text_im_file_path = "data/haystack_part_1_of_2.png"
    patter_im_file = "data/of.png"
    main_im(whole_text_im_file_path, patter_im_file)
