#! python3
# coding=utf-8


import os


def file_exist(filename):
    return os.path.exists(filename)


def file_exists(filename_list):
    for filename in filename_list:
        if file_exist(filename) is False:
            return False
    return True


def file_get_filename(filename):
    (file_path, file_simple_name) = os.path.split(filename)
    return file_simple_name


def file_get_path(filename):
    (file_path, file_simple_name) = os.path.split(filename)
    return file_path


def file_join(path, filename):
    return os.path.join(path, filename)
