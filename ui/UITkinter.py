#! python3
# coding=utf-8


from tkinter import *
import tkinter.messagebox
import tkinter.filedialog
from tkinter import ttk
from Log import CommonLog


LEVEL_INFO = 0
LEVEL_WARNING = 1
LEVEL_ERROR = 2

g_data_dict = {
    'file': {
        'data': [],
        'update': False,
        'view': None,
        'view_type': 'Entry'
    },
    'path': {
        'data': [],
        'update': False,
        'view': None,
        'view_type': 'Entry'
    },
    'database': {
        'data': [],
        'update': False,
        'view': None,
        'view_type': 'Entry'
    },
    'use_db': {
        'data': None,
        'update': False,
        'view': None,
        'view_type': 'Checkbutton'
    },
    'find': {
        'data': None,  # CALLBACK: param[0]: use_db
        'update': False,
        'view': None,
        'view_type': 'Button'
    }
}


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
    menu_help.add_command(label='About', command=lambda: _show_about(root))
    menu_bar = Menu(root)
    menu_bar.add_cascade(label='Help', menu=menu_help)
    root['menu'] = menu_bar


def _init_ttk_styles():
    style = ttk.Style()
    style.configure('Content.TFrame', background=g_attributes['background'])
    style.configure('Label.TLabel', background=g_attributes['background'], foreground='white')
    style.configure('Entry.TEntry', width=200)
    style.configure('UseDB.TCheckbutton', background=g_attributes['background'])


def _update_entry(view, data):
    text_var = ''
    for text in data['data']:
        text_var += text + ';'
    if len(text_var) > 0:
        text_var = text_var[: len(text_var) - 1]
    CommonLog.log_d('file: {}'.format(text_var))
    view.delete(0, END)  # clear the value
    view.insert(0, text_var)  # set the value


def _update():
    global g_data_dict
    for data in g_data_dict:
        if g_data_dict[data]['update'] is True:
            view = g_data_dict[data]['view']
            view_type = g_data_dict[data]['view_type']
            if view_type == 'Entry':
                _update_entry(view, g_data_dict[data])
            g_data_dict[data]['update'] = False


def _add_file_update_entry(entry_type, choose_dir=False):
    global g_data_dict
    if choose_dir is False:
        filename = tkinter.filedialog.askopenfilename()
    else:
        filename = tkinter.filedialog.askdirectory()
    if filename is not None and '' != filename:
        g_data_dict[entry_type]['data'].append(filename)
        g_data_dict[entry_type]['update'] = True
        _update()


def _choose_file_update_entry(entry_type, choose_dir=False):
    global g_data_dict
    if choose_dir is False:
        filename = tkinter.filedialog.askopenfilename()
    else:
        filename = tkinter.filedialog.askdirectory()
    if filename is not None and '' != filename:
        g_data_dict[entry_type]['data'].clear()
        g_data_dict[entry_type]['data'].append(filename)
        g_data_dict[entry_type]['update'] = True
        _update()


def _choose_file():
    _choose_file_update_entry('file')


def _choose_path():
    _choose_file_update_entry('path', True)


def _choose_database():
    _choose_file_update_entry('database', True)


def _add_file():
    _add_file_update_entry('file')


def _add_path():
    _add_file_update_entry('path', True)


def _add_database():
    _add_file_update_entry('database', True)


def _find():
    global g_data_dict
    if g_data_dict['find']['data'] is not None:
        g_data_dict['find']['data'](g_data_dict['file']['data'], g_data_dict['path']['data'],
                                    g_data_dict['database']['data'], g_data_dict['use_db']['data'].get())


def _init_main_view(root):
    global g_data_dict
    global g_attributes
    content = ttk.Frame(root, padding=(10, 10, 10, 10), style='Content.TFrame')

    label_file = ttk.Label(content, text='File:', style='Label.TLabel', font=('Times New Roman', 12, 'normal'))
    label_path = ttk.Label(content, text='Path:', style='Label.TLabel', font=('Times New Roman', 12, 'normal'))
    label_database = ttk.Label(content, text='Database:', style='Label.TLabel', font=('Times New Roman', 12, 'normal'))

    entry_file = ttk.Entry(content, style='Entry.TEntry')
    entry_path = ttk.Entry(content, style='Entry.TEntry')
    entry_database = ttk.Entry(content, style='Entry.TEntry')

    button_file = ttk.Button(content, text='Choose File', command=_choose_file)
    button_file_add = ttk.Button(content, text='Add File', command=_add_file)
    button_path = ttk.Button(content, text='Choose Path', command=_choose_path)
    button_path_add = ttk.Button(content, text='Add Path', command=_add_path)
    button_database = ttk.Button(content, text='Choose Database', command=_choose_database)
    button_find = ttk.Button(content, text='Find', command=_find)

    g_data_dict['use_db']['data'] = tkinter.IntVar()
    cb_database = ttk.Checkbutton(content, text='Load From Database',
                                  style='UseDB.TCheckbutton', variable=g_data_dict['use_db']['data'])

    label_file.grid(row=0, column=0, sticky=W)
    entry_file.grid(row=1, column=0, sticky=W)
    button_file.grid(row=1, column=1, sticky=W)
    button_file_add.grid(row=1, column=2, sticky=W)
    # content.columnconfigure(0, minsize=15)
    label_path.grid(row=2, column=0, sticky=W)
    entry_path.grid(row=3, column=0, sticky=W)
    button_path.grid(row=3, column=1, sticky=W)
    button_path_add.grid(row=3, column=2, sticky=W)
    # content.columnconfigure(1, minsize=15)
    label_database.grid(row=4, column=0, sticky=W)
    entry_database.grid(row=5, column=0, sticky=W)
    button_database.grid(row=5, column=1, sticky=W)
    # content.columnconfigure(2, minsize=15)
    cb_database.grid(row=6, column=0, sticky=W)
    button_find.grid(row=7, column=0, sticky=W)

    content.grid(row=0, column=0, sticky=(N, S, E, W))
    root.columnconfigure(0, weight=1)
    root.rowconfigure(0, weight=1)

    g_data_dict['file']['view'] = entry_file
    g_data_dict['path']['view'] = entry_path
    g_data_dict['database']['view'] = entry_database
    g_data_dict['use_db']['view'] = cb_database


def _init_views(root):
    _set_attributes(root)
    _init_ttk_styles()
    _init_menus(root)
    _init_main_view(root)
    pass


def set_attributes(attributes):
    global g_attributes
    for key in attributes:
        g_attributes[key] = attributes[key]


def set_on_find(callback):
    global g_data_dict
    g_data_dict['find']['data'] = callback


def main_loop():
    root = Tk()
    _init_views(root)
    root.mainloop()
