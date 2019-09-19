#! python3
# coding=utf-8


from Log import CommonLog
from configs import ConfigArgs
from databases import DatabaseAdapter
from picture import PictureSearch
from picture import PictureAnalyse
from ui import UIMain
from commons import FileUtil


g_fp_list = list()
g_database_list = list()


def on_find(file_list, path_list, database_list, use_db):
    global g_fp_list
    global g_database_list

    if len(g_fp_list) > 0:
        if use_db > 0:
            load_from_db = True
        else:
            load_from_db = False
    else:
        load_from_db = False
        if use_db > 0:
            db_name = FileUtil.file_get_filename(database_list[0])
            if FileUtil.file_exists([FileUtil.file_join(database_list[0], db_name + '.bak'),
                                     FileUtil.file_join(database_list[0], db_name + '.dat'),
                                     FileUtil.file_join(database_list[0], db_name + '.dir')]) is True:
                load_from_db = True

    if load_from_db is True:
        DatabaseAdapter.init(DatabaseAdapter.DATABASE_TYPE_SHELVE, {'db_filename': database_list})
        g_fp_list = DatabaseAdapter.get('fingerprints')
        DatabaseAdapter.uninit()
        CommonLog.log_i('Load fingerprints form database.')
    else:
        CommonLog.log_i('Loading fingerprints now.')
        g_fp_list = PictureAnalyse.analyse_picture_in_directory(path_list[0], ['jpg', 'png'])
        if use_db > 0:
            DatabaseAdapter.init(DatabaseAdapter.DATABASE_TYPE_SHELVE, {'db_filename': database_list})
            DatabaseAdapter.update('fingerprints', g_fp_list)
            DatabaseAdapter.uninit()
        CommonLog.log_i('Loading fingerprints finished.')

    match_list = PictureSearch.search_picture_in_list_by_content(file_list[0], g_fp_list)
    for file in match_list:
        CommonLog.log_i('Result: ', file)


if __name__ == '__main__':
    CommonLog.log_title('Picture Search')
    # args = ConfigArgs.config_args_parse()
    # DatabaseAdapter.init(DatabaseAdapter.DATABASE_TYPE_SHELVE, {'db_filename': [args.database]})
    #
    # fp_list = DatabaseAdapter.get('fingerprints')
    # if fp_list is None or len(fp_list) <= 0:
    #     CommonLog.log_i('Loading fingerprints now.')
    #     fp_list = PictureAnalyse.analyse_picture_in_directory(args.path, ['jpg', 'png'])
    #     DatabaseAdapter.update('fingerprints', fp_list)
    # else:
    #     CommonLog.log_i('Load fingerprints form database.')
    #
    # match_list = PictureSearch.search_picture_in_list_by_content(args.file, fp_list)
    # for file in match_list:
    #     CommonLog.log_i('Result: ', file)
    #
    # DatabaseAdapter.uninit()

    UIMain.set_ui_type(UIMain.UI_TYPE_TKINTER)
    UIMain.set_attributes({'title': '** Picture Search **', 'geometry': '1024x600', 'background': '#FFDEAD'})
    UIMain.set_on_find(on_find)
    UIMain.mainloop()
