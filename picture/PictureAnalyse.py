#! python3
# coding=utf-8


import glob
import imagehash
from PIL import Image
from Log import CommonLog
from picture import PictureCommons
from picture import PictureInfo


def analyse_picture_in_directory(path, suffix_list):
    fp_list = list()
    for suffix in suffix_list:
        for picture_path in glob.glob(path + '\*.' + suffix):
            # CommonLog.log_d(picture_path)
            fp_dict = dict()
            image = Image.open(picture_path)
            fp_dict[PictureCommons.PICTURE_COMMON_KEY_INFO] = PictureInfo.get_picture_info_by_image(image)
            if suffix.lower() == 'png':
                image = image.convert('RGBA')
            image_hash = str(imagehash.dhash(image))
            fp_dict[PictureCommons.PICTURE_COMMON_KEY_FILENAME] = picture_path
            fp_dict[PictureCommons.PICTURE_COMMON_KEY_FINGERPRINT] = image_hash
            fp_list.append(fp_dict)
    return fp_list
