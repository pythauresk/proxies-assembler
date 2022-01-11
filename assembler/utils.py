import os

import numpy as np
from PIL import Image


def check_sizes():
    """check if images in '/images' have the same sizes (return boolean)"""
    list_imgs = os.listdir("./images")
    print(list_imgs)
    boolean = True
    size = Image.open("./images/{}".format(list_imgs[0])).size
    i = 1
    while boolean and (i <= len(list_imgs)-1):
        boolean = (size == Image.open("./images/{}".format(list_imgs[i])).size)
        i += 1

    # TODO identify the first image that have not the same size
    return boolean


def check_nb_proxies():
    print(len(os.listdir("./images")))
    return len(os.listdir("./images")) <= 9


def assembler():
    if check_nb_proxies() and check_sizes():
        list_imgs = os.listdir("./images")
        while len(list_imgs) % 3 != 0:
            list_imgs.append('')

        size = Image.open("./images/{}".format(list_imgs[0])).size
        blank = np.zeros([size[1], size[0], 4], dtype=np.uint8)
        sep = np.zeros([size[1], 8, 4], dtype=np.uint8)

        arr = np.asarray([list(i) for i in list(zip(*[iter(list_imgs)] * 3))])

        list_rows = []
        for row in arr:
            img = np.array(Image.open("./images/{}".format(row[0])))
            img = np.concatenate((img, sep), axis=1)
            if row[1] == '':
                img = np.concatenate((img, blank, sep, blank), axis=1)
            else:
                img = np.concatenate((img, np.array(Image.open("./images/{}".format(row[1]))), sep), axis=1)
                if row[2] == '':
                    img = np.concatenate((img, blank), axis=1)
                else:
                    img = np.concatenate((img, np.array(Image.open("./images/{}".format(row[2])))), axis=1)

            horiz_sep = np.zeros([8, img.shape[1], 4], dtype=np.uint8)
            list_rows.append(np.concatenate((img, horiz_sep), axis=0))

        final_img = Image.fromarray(np.concatenate(tuple(list_rows), axis=0))
        final_img.save('result.png')

        return True
    else:
        return False


if __name__ == "__main__":
    pass
