#! python3
# coding=utf-8


from ui import UITkinter

UI_TYPE_BEGIN = 0
UI_TYPE_TKINTER = 1
UI_TYPE_END = 2


g_ui_type = UI_TYPE_TKINTER
g_ui_list = [
    {'func_mainloop': 'func', 'func_set_attributes': 'func'},
    {'mainloop': UITkinter.main_loop, 'set_attributes': UITkinter.set_attributes},
]


def set_ui_type(ui_type):
    global g_ui_type
    if UI_TYPE_BEGIN < ui_type < UI_TYPE_END:
        g_ui_type = ui_type
        return True
    return False


def set_attributes(attributes):
    global g_ui_type
    global g_ui_list
    g_ui_list[g_ui_type]['set_attributes'](attributes)


def mainloop():
    global g_ui_type
    global g_ui_list
    correct = True
    if correct is True:
        g_ui_list[g_ui_type]['mainloop']()
