#! python3
# coding=utf-8


LOG_OUTPUT_CHANNEL_CONSOLE = 0

g_log_output_channel = LOG_OUTPUT_CHANNEL_CONSOLE


def log_global_set_output_channel(channel):
    global g_log_output_channel
    g_log_output_channel = channel


def _log_t(level, *args):
    global g_log_output_channel
    output = level
    for arg in args:
        output = '{} {}'.format(output, arg)

    if g_log_output_channel == LOG_OUTPUT_CHANNEL_CONSOLE:
        print(output)


def log_d(*args):
    _log_t('DEBUG:', *args)


def log_i(*args):
    _log_t('INFO:', *args)


def log_w(*args):
    _log_t('WARNING:', *args)


def log_e(*args):
    _log_t('ERROR:', *args)


def log_v(*args):
    _log_t('VERBOSE:', *args)


def log_title(*args):
    _log_t('*****', *args, '*****')
