import numpy as np
from PIL import Image



def part_text_im(path, save_folder, parts=2):
    im_arr = np.array(Image.open(path).convert('L'))
    file_name = path.split("/")[-1].split(".")[0]

    m = im_arr.shape[0]
    h = m // parts
    for i in range(parts):
        p = Image.fromarray(im_arr[i*h:(i+1)*h, :])
        p.save(save_folder + f"/{file_name}_part_{i+1}_of_{parts}.png")


if __name__ == '__main__':
    path = "data/haystack.png"
    save_folder = "data"
    parts = 16

    part_text_im(path, save_folder, parts)