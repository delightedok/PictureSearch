#! python3
# coding=utf-8


import glob
from PIL import Image
from picture import PictureCommons


def get_picture_info(filename):
    info = dict()
    image = Image.open(filename)
    info[PictureCommons.PICTURE_COMMON_KEY_FILENAME] = filename
    info[PictureCommons.PICTURE_COMMON_KEY_FORMAT] = image.format
    info[PictureCommons.PICTURE_COMMON_KEY_RESOLUTION] = image.size
    return info


def get_picture_info_by_image(image):
    info = dict()
    if image is not None:
        info[PictureCommons.PICTURE_COMMON_KEY_FILENAME] = image.filename
        info[PictureCommons.PICTURE_COMMON_KEY_FORMAT] = image.format
        info[PictureCommons.PICTURE_COMMON_KEY_RESOLUTION] = image.size
    return info
