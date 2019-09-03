#! python3
# coding=utf-8


from PIL import Image
from io import BytesIO


PICTURE_COMMON_KEY_FILENAME = 'filename'
PICTURE_COMMON_KEY_FINGERPRINT = 'fingerprint'
PICTURE_COMMON_KEY_INFO = 'info'
PICTURE_COMMON_KEY_FORMAT = 'format'
PICTURE_COMMON_KEY_RESOLUTION = 'resolution'


g_resize_width = 9
g_resize_height = 8
g_gray_scale = True
g_hamming_distance = 5


def set_resize(width=None, height=None):
    global g_resize_width
    global g_resize_height
    if width is not None:
        g_resize_width = width
    if height is not None:
        g_resize_height = height


def get_resize_width():
    global g_resize_width
    return g_resize_width


def get_resize_height():
    global g_resize_height
    return g_resize_height


def enable_grayscale(enable=True):
    global g_gray_scale
    g_gray_scale = enable


def is_grayscale():
    global g_gray_scale
    return g_gray_scale


def dhash(filename):
    if filename[filename.rfind('.') + 1:].lower() == 'png':
        image = Image.open(filename).convert('RGB')
    else:
        image = Image.open(filename)

    image = image.resize((get_resize_width(), get_resize_height()), Image.ANTIALIAS)

    if is_grayscale() is True:
        image = image.convert('L')
    pixels = list(image.getdata())
    difference_list = list()
    for row in range(get_resize_height()):
        index = row * get_resize_width()
        for col in range(get_resize_width() - 1):
            start_index = index + col
            difference_list.append(pixels[start_index] > pixels[start_index + 1])
    image.close()

    decimal_value = 0
    hash_string = ''
    for index, value in enumerate(difference_list):
        if value:
            decimal_value += value * (2 ** (index % 8))
        if 7 == index % 8:
            hash_string += str(hex(decimal_value)[2:].rjust(2, '0'))
            decimal_value = 0

    return hash_string


def get_hamming_distance(hash1, hash2):
    difference = (int(hash1, 16)) ^ (int(hash2, 16))
    return bin(difference).count('1')


def get_hamming_distance_standard():
    global g_hamming_distance
    return g_hamming_distance
