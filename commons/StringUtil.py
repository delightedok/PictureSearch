#! python3
# coding=utf-8


def str_2_escape(string, escape_char_list):
    ret = string
    for char in escape_char_list:
        ret = ret.replace(char, '\\{}'.format(char))
    return ret


def wildcards_2_pattern(string, wildcard_list):
    ret = string
    for wildcard in wildcard_list:
        if '*' == wildcard:
            ret = ret.replace(wildcard, '.{}'.format(wildcard))
    return ret
