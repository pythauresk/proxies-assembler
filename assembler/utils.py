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
    pass


if __name__ == "__main__":
    pass
