#! python3
# coding=utf-8


import imagehash
from PIL import Image
from Log import CommonLog
from picture import PictureCommons


def _is_similar(picture_hash, fp_list):
    similar_list = list()
    for fp in fp_list:
        if picture_hash == fp[PictureCommons.PICTURE_COMMON_KEY_FINGERPRINT]:
            similar_list.append(fp[PictureCommons.PICTURE_COMMON_KEY_FILENAME])
    return similar_list


def search_picture_in_list(picture_name, fp_list):
    image = Image.open(picture_name)
    image_hash = str(imagehash.dhash(image))
    match_list = _is_similar(image_hash, fp_list)
    return match_list
