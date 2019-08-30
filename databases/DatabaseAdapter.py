#! python3
# coding=utf-8


from databases.shelve.shelve import ShelveHandler


DATABASE_TYPE_SHELVE = 0
g_database_handler = None


def init(db_type, properties):
    global DATABASE_TYPE_SHELVE
    global g_database_handler
    if DATABASE_TYPE_SHELVE == db_type:
        g_database_handler = ShelveHandler()
        set_properties(properties)
        g_database_handler.init()


def _get_shelve_property_func(property_name):
    global g_database_handler
    if property_name == 'db_filename':
        return g_database_handler.set_db_filename


def set_properties(properties):
    global g_database_handler
    if type(g_database_handler) == ShelveHandler:
        for key in properties:
            func = _get_shelve_property_func(key)
            args = properties[key]
            func(*args)


def update(key, value):
    global g_database_handler
    if type(g_database_handler) == ShelveHandler:
        g_database_handler.update(key, value)


def update_batch(kv_dict):
    global g_database_handler
    if type(g_database_handler) == ShelveHandler:
        g_database_handler.transaction_begin()
        for key in kv_dict:
            g_database_handler.transaction_update(key, kv_dict[key])
        g_database_handler.transaction_commit()


def get(key):
    global g_database_handler
    if type(g_database_handler) == ShelveHandler:
        return g_database_handler.get_value(key)
    return None


def uninit():
    global g_database_handler
    if type(g_database_handler) == ShelveHandler:
        g_database_handler.exit()
