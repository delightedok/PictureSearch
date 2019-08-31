#! python3
# coding=utf-8


from Log import CommonLog
from configs import ConfigArgs
from databases import DatabaseAdapter
from picture import PictureSearch
from picture import PictureAnalyse


if __name__ == '__main__':
    CommonLog.log_title('Picture Search')
    args = ConfigArgs.config_args_parse()
    DatabaseAdapter.init(DatabaseAdapter.DATABASE_TYPE_SHELVE, {'db_filename': [args.database]})

    fp_list = DatabaseAdapter.get('fingerprints')
    if fp_list is None or len(fp_list) <= 0:
        CommonLog.log_i('Loading fingerprints now.')
        fp_list = PictureAnalyse.analyse_picture_in_directory(args.path, ['jpg', 'png'])
        DatabaseAdapter.update('fingerprints', fp_list)
    else:
        CommonLog.log_i('Load fingerprints form database.')

    match_list = PictureSearch.search_picture_in_list(args.file, fp_list)
    for file in match_list:
        CommonLog.log_i('Result: ', file)

    DatabaseAdapter.uninit()
