#! python3
# coding=utf-8


from tkinter import *
import tkinter.messagebox
from Log import CommonLog


LEVEL_INFO = 0
LEVEL_WARNING = 1
LEVEL_ERROR = 2


def _show_message_mb(title, level, message):
    if level == LEVEL_INFO:
        tkinter.messagebox.showinfo(title, message)
    elif level == LEVEL_WARNING:
        tkinter.messagebox.showwarning(title, message)
    elif level == LEVEL_ERROR:
        tkinter.messagebox.showerror(title, message)
    else:
        CommonLog.log_e('UITkinter', '_show_message_mb', 'Unknown Log Level[{}]'.format(level))


def _set_title(root, title):
    root.title(title)


def _set_geometry(root, geometry):
    root.geometry(geometry)


def _set_background(root, background):
    root.configure(background=background)


g_attributes_func = {
    'title': _set_title,
    'geometry': _set_geometry,
    'background': _set_background,
}
g_attributes = dict()


def _set_attributes(root):
    global g_attributes_func
    global g_attributes
    for key in g_attributes:
        g_attributes_func[key](root, g_attributes[key])


def _show_about(root):
    _show_message_mb('About', LEVEL_INFO, 'Author: TamGitsun\nEmail: jieshentan@outlook.com')


def _init_menus(root):
    menu_help = Menu(root, tearoff=0)
    menu_help.add_command(label='Help')
    menu_help.add_separator()
    menu_help.add_command(label='Check for Updates...')
    menu_help.add_command(label='About', command=lambda : _show_about(root))
    menu_bar = Menu(root)
    menu_bar.add_cascade(label='Help', menu=menu_help)
    root['menu'] = menu_bar


def _init_views(root):
    _set_attributes(root)
    _init_menus(root)
    pass


def set_attributes(attributes):
    global g_attributes
    for key in attributes:
        g_attributes[key] = attributes[key]


def main_loop():
    root = Tk()
    _init_views(root)
    root.mainloop()
