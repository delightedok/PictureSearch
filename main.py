#! python3
# coding=utf-8


from Log import CommonLog
from configs import ConfigArgs
from databases import DatabaseAdapter


if __name__ == '__main__':
    CommonLog.log_title('Picture Search')
    args = ConfigArgs.config_args_parse()
    DatabaseAdapter.init(DatabaseAdapter.DATABASE_TYPE_SHELVE, {'db_filename': [args.database]})
    DatabaseAdapter.uninit()
