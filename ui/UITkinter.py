#! python3
# coding=utf-8


from tkinter import *


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


def _init_views(root):
    _set_attributes(root)
    pass


def set_attributes(attributes):
    global g_attributes
    for key in attributes:
        g_attributes[key] = attributes[key]


def main_loop():
    root = Tk()
    _init_views(root)
    root.mainloop()
