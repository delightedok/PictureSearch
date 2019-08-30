#! python3
# coding=utf-8


import argparse


g_args_need = [{
        'args': ['-p', '--path'],
        'help': 'directory for searching picture'
    }, {
        'args': ['-f', '--file'],
        'help': 'sample picture used for searching'
    }
]

g_args_optional = [{
        'args': ['-vvvvv'],
        'help': 'log level of error, info, warning, debug, verbose'
    }, {
        'args': ['-vvvv'],
        'help': 'log level of error, info, warning, debug'
    }, {
        'args': ['-vvv'],
        'help': 'log level of error, info, warning'
    }, {
        'args': ['-vv'],
        'help': 'log level of error, info'
    }, {
        'args': ['-v'],
        'help': 'log level of error'
    }
]


def config_args_parse():
    global g_args_need
    global g_args_optional
    ap = argparse.ArgumentParser()
    for arg in g_args_need:
        ap.add_argument(*arg['args'], required=True, help=arg['help'])
    for arg in g_args_optional:
        ap.add_argument(*arg['args'], help=arg['help'])
    return ap.parse_args()
