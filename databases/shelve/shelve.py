#! python3
# coding=utf-8


import shelve
from Log import CommonLog


class ShelveHandler:

    def __init__(self):
        self.db_filename = None
        self.run = False
        self.db = None
        self.transaction = False

    def set_db_filename(self, filename):
        if self.run is False:
            self.db_filename = filename
            CommonLog.log_d(self.db_filename)
        else:
            CommonLog.log_e('ShelveHandler is running now')

    def init(self):
        if self.run is False:
            self.db = shelve.open(self.db_filename, flag='c', protocol=2, writeback=False)
            self.run = True
        else:
            CommonLog.log_w('ShelveHandler is running now')

    def update(self, key, value):
        if self.run is True:
            if self.transaction is False:
                self.db[key] = value
                self.db.sync()
            else:
                CommonLog.log_e('ShelveHandler transaction is in process')
        else:
            CommonLog.log_e('ShelveHandler is not running now')

    def transaction_begin(self):
        if self.run is True:
            if self.transaction is False:
                self.transaction = True
            else:
                CommonLog.log_e('ShelveHandler transaction is in process')
        else:
            CommonLog.log_e('ShelveHandler is not running now')

    def transaction_update(self, key, value):
        if self.run is True:
            if self.transaction is True:
                self.db[key] = value
            else:
                CommonLog.log_e('ShelveHandler transaction is NOT in process')
        else:
            CommonLog.log_e('ShelveHandler is not running now')

    def transaction_commit(self):
        if self.run is True:
            if self.transaction is True:
                self.db.sync()
                self.transaction = False
            else:
                CommonLog.log_e('ShelveHandler transaction is NOT in process')
        else:
            CommonLog.log_e('ShelveHandler is not running now')

    def get_value(self, key):
        if self.run is True:
            return self.db[key]
        else:
            CommonLog.log_e('ShelveHandler is not running now')
            return None

    def exit(self):
        if self.run is True:
            self.db.close()
            self.db = None
            self.run = False
