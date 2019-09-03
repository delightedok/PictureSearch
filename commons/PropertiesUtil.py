#! python3
# coding=utf-8


class Properties:

    def __init__(self):
        self.content = dict()
        self.filename = None
        self.fp = None

    def open(self, filename, encoding='utf-8'):
        if filename is not None:
            self.filename = filename
            self.fp = open(filename, 'r', encoding=encoding)
            return self

    def load(self):
        if self.fp is not None:
            line = self.fp.readline()
            index = None
            while line is not None and len(line) > 0:
                line = line.strip()
                if 0 == len(line):
                    line = self.fp.readline()
                    continue
                elif '[' == line[0] and ']' == line[len(line) - 1]:
                    index = line[1: len(line) - 1]
                    self.content[index] = dict()
                else:
                    content = line[0: len(line)]
                    kv = content.split('=', 1)
                    if len(kv) > 1:
                        self.content[index][kv[0].strip()] = kv[1].strip()
                    elif 1 == len(kv):
                        self.content[index][kv[0].strip()] = ''
                    else:
                        return False
                line = self.fp.readline()
            return True
        else:
            return False

    def close(self):
        if self.fp is not None:
            self.fp.close()
            self.fp = None

    def get_content(self):
        return self.content

    @staticmethod
    def parse(filename, encoding='utf-8'):
        prop = Properties()
        prop.open(filename, encoding)
        if prop.load() is True:
            prop.close()
            return prop.get_content()
        else:
            return None
