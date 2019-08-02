import re
import os
import os.path

# TODO ADD DOCSTRINGS


class fmt:
    def __init__(self, linestart, lineend, pathtofixed, pathtoold):
        self.linestart = linestart
        self.lineend = lineend
        self.pathtofixed = pathtofixed
        self.pathtoold = pathtoold

    def _fixfilepath(self):

        if not os.path.isdir(self.pathtofixed):
            print('Creating directory {}', self.pathtofixed)
            os.mkdir(self.pathtofixed)
        if self.pathtofixed[-1] != '/':
            self.pathtofixed = ''.join((self.pathtofixed, '/'))
        if self.pathtoold[-1] != '/':
            self.pathtoold = ''.join((self.pathtofixed, '/'))
        try:
            os.path.exists(self.pathtoold)
        except FileNotFoundError:
            print('Error: check path to unformatted files. ')
            print('Provided path: {}', self.pathtoold)

    def _read_space(self):
        self._fixfilepath()
        namelist = os.listdir(self.pathtoold)

        for filename in namelist:
            if os.path.isdir(filename) or filename[-5:] != ".java":
                continue
            f = open(self.pathtoold + filename, 'r')
            self.__TEST__(f, filename)
            f.close()

    def __TEST__(self, f, filename):
        comments_slash1 = re.compile(r'//\s?.*')
        comments_slash_ast2 = re.compile(r'(/\**.*\*/)|/\*.*?')
        comments_slash_end3 = re.compile(r'.*?\*/')
        comments_only_ast4 = re.compile(r'^\*.*')
        skip_next_line = False
        begin_write = False

        for line in f:

            if skip_next_line:
                skip_next_line = False
                continue

            line = line.strip()

            if comments_slash1.search(line):
                line = comments_slash1.sub('', line)
            if comments_slash_ast2.search(line):
                line = comments_slash_ast2.sub('', line)
            if comments_slash_end3.search(line):
                line = comments_slash_end3.sub('', line)
            if comments_only_ast4.search(line):
                continue
            if not begin_write and line.find(
                    self.linestart) != -1 and not line.find('{'):
                skip_next_line = True
                begin_write = True
            elif not begin_write and line.find(self.linestart) != -1:
                begin_write = True

            elif begin_write and (line.find(self.lineend) != -1
                                  or line.find('public') != -1):
                break
            if begin_write:
                self._write_fixed(line, filename)

    def _write_fixed(self, text, filename):
        fixed = open(self.pathtofixed + 'f' + filename, 'a')
        fixed.write(text + '\n')
        fixed.close()

    def format(self):
        self._read_space()


if __name__ == "__main__":
    linestart = input("start string: ")
    lineend = input("end string: ")
    pathtofixed = input("fixed file path: ")
    pathtoold = input("pathtoold to read from: ")
    a = fmt(linestart, lineend, pathtofixed, pathtoold)
    a.format()

# EXAMPLE
#    linestart = 'lookup('
#    lineend = '@Override'
#    pathtofixed = 'javahw1/newfixed/'
#    pathtoold = 'javahw1/'
#    a = fmt(linestart, lineend, pathtofixed, pathtoold)
#    a.format()
