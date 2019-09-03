#! python3
# coding=utf-8


import imagehash
from PIL import Image
from Log import CommonLog
from picture import PictureCommons
import re


def _is_similar(picture_hash, fp_list):
    similar_list = list()
    for fp in fp_list:
        # if picture_hash == fp[PictureCommons.PICTURE_COMMON_KEY_FINGERPRINT]:
        if PictureCommons.get_hamming_distance_standard() > \
                PictureCommons.get_hamming_distance(picture_hash, fp[PictureCommons.PICTURE_COMMON_KEY_FINGERPRINT]):
            similar_list.append(fp[PictureCommons.PICTURE_COMMON_KEY_FILENAME])
    return similar_list


def search_picture_in_list_by_content(picture_name, fp_list):
    image = Image.open(picture_name)
    image_hash = str(imagehash.dhash(image))
    match_list = _is_similar(image_hash, fp_list)
    return match_list


def search_picture_in_list_by_name(picture_name_pattern, fp_list):
    similar_list = list()
    print(picture_name_pattern)
    regexp = r'' + picture_name_pattern
    pat = re.compile(regexp)
    for fp in fp_list:
        index = fp[PictureCommons.PICTURE_COMMON_KEY_FILENAME].rfind('\\') + 1
        result = pat.search(fp[PictureCommons.PICTURE_COMMON_KEY_FILENAME][index:])
        if result is not None:
            similar_list.append(fp[PictureCommons.PICTURE_COMMON_KEY_FILENAME])
    return similar_list
