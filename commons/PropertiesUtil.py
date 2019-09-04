#! python3
# coding=utf-8


class Properties:

    def __init__(self):
        self.content = dict()
        self.filename = None
        self.fp = None

    def open(self, filename, encoding='utf-8'):
        if filename is not None:
            self.content.clear()
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

    def _close(self):
        if self.fp is not None:
            self.fp.close()
            self.fp = None

    def close(self):
        self._close()
        # self.content.clear()

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

    @staticmethod
    def dict_2_file(filename, content_dict, encoding='utf-8'):
        with open(filename, 'w', encoding='utf-8') as fp:
            if content_dict is not None:
                for title in content_dict:
                    fp.write('[{}]\n'.format(title))
                    for key in content_dict[title]:
                        fp.write('{} = {}\n'.format(key, content_dict[title][key]))
            fp.close()

    def update_value(self, title=None, key=None, value=''):
        if self.fp is not None:
            if title is not None:
                title_exist = False
                for t in self.content:
                    if t == title:
                        title_exist = True
                        break
                if title_exist is False:
                    self.content[title] = dict()
                if key is not None:
                    self.content[title][key] = value

                # sync the content to file
                self.close()
                Properties.dict_2_file(self.filename, self.content)
                self.open(self.filename).load()
                return True
        return False
