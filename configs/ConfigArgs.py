#! python3
# coding=utf-8


import argparse


g_args_need = [{
        'args': ['-p', '--path'],
        'action': None,
        'help': 'directory for searching picture'
    }, {
        'args': ['-f', '--file'],
        'action': None,
        'help': 'sample picture used for searching'
    }, {
        'args': ['-d', '--database'],
        'action': None,
        'help': 'directory of database which stores the fingerprint of pictures'
    }
]

g_args_optional = [{
        'args': ['-vvvvv'],
        'action': 'store_true',
        'help': 'log level of error, info, warning, debug, verbose'
    }, {
        'args': ['-vvvv'],
        'action': 'store_true',
        'help': 'log level of error, info, warning, debug'
    }, {
        'args': ['-vvv'],
        'action': 'store_true',
        'help': 'log level of error, info, warning'
    }, {
        'args': ['-vv'],
        'action': 'store_true',
        'help': 'log level of error, info'
    }, {
        'args': ['-v'],
        'action': 'store_true',
        'help': 'log level of error'
    }
]


def config_args_parse():
    global g_args_need
    global g_args_optional
    ap = argparse.ArgumentParser()
    for arg in g_args_need:
        if arg['action'] is not None:
            if 'default' in arg:
                ap.add_argument(*arg['args'], required=True, help=arg['help'],
                                action=arg['action'], default=arg['default'])
            else:
                ap.add_argument(*arg['args'], required=True, help=arg['help'],
                                action=arg['action'])
        else:
            if 'default' in arg:
                ap.add_argument(*arg['args'], required=True, help=arg['help'], default=arg['default'])
            else:
                ap.add_argument(*arg['args'], required=True, help=arg['help'])
    for arg in g_args_optional:
        if arg['action'] is not None:
            if 'default' in arg:
                ap.add_argument(*arg['args'], help=arg['help'], action=arg['action'], default=arg['default'])
            else:
                ap.add_argument(*arg['args'], help=arg['help'], action=arg['action'])
        else:
            if 'default' in arg:
                ap.add_argument(*arg['args'], help=arg['help'], default=arg['default'])
            else:
                ap.add_argument(*arg['args'], help=arg['help'])
    return ap.parse_args()
