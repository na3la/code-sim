import re
import os
import os.path

# parames used: linestart = 'publicInstTuplelookup(StringID){'

# self.lineend = /**
# TODO IMPROVE CODE QUALITY/REFACTOR


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

    def __TEST__(self, f, filename):
        skip_next_line = False
        begin_write = False
        test = re.compile(r'//\s?.*')
        for line in f:
            if skip_next_line:
                continue
            line = line.strip()
            if test.search(line):
                line = test.sub('', line)
           # if re.search(r'/*\*.*?\*/', line):  # no match
           #     line = re.sub(r'/*\*.*?\*/', '', line)
            elif re.search(r'/\*\*.*', line):
                line = re.sub(r'/\*\*.*', '', line)
                check = False
            if re.search(r'.*?\*/', line):
                line = re.sub(r'.*?\*/', '', line)
                continue
            if re.search(r'[\s]+\*.*', line):# and not check:
                continue
            #if re.search(r'[^/\*]\*[^/].*', line):  # no match
             #   line = re.search(r'[^/\*]\*[^/].*', line)
              #  continue
           # elif re.search(r'\*/', line):  # no match
            #    check = True
             #   re.sub(r'.*?\*/', '', line)
              #  continue
            if not begin_write and line.find(self.linestart) != -1 and line.find('{'):
                begin_write = True
            elif not begin_write and line.find(self.linestart) != -1 and not line.find('{'):
                skip_next_line = True
                begin_write = True

            elif begin_write and (line.find(self.lineend) != -1
                                  or line.find('public') != -1):
                begin_write = False
                break
            elif begin_write:
                self._write_fixed(line, filename)

    def _write_fixed(self, text, filename):
        fixed = open(self.pathtofixed + 'f' + filename, 'a')
        fixed.write(text + '\n')
        fixed.close()

    def format(self):
        self._read_space()


if __name__ == "__main__":
    #    linestart = input("start string: ")
    #    lineend = input("end string: ")
    #    pathtofixed = input("fixed file path: ")
    #    pathtoold = input("pathtoold to read from: ")
    #    format(linestart, lineend, pathtofixed, pathtoold)
    # linestart = re.compile(r'eval\s?\(table table\)\s?.*?{\s*', re.I)

    # lineend = re.compile(r'.(?=@Override public\s?string\s?tostring\(\))',
    #                     re.I)
    linestart = 'eval('
    lineend = '@Override'
    pathtofixed = 'javahw3/newfixed'
    pathtoold = 'javahw3/'
    a = fmt(linestart, lineend, pathtofixed, pathtoold)
    a.format()
