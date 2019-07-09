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
            continue
            f = open(self.pathtoold + filename, 'r')
            _to_analyze = f.read()
            f.close()
            if not len(_to_analyze):
                continue
            # try yielding _to_analyze and filename, and feed to cleaning
            fixed_text = self._cleaning(_to_analyze, filename)
            if fixed_text:
                self._write_fixed(fixed_text, filename)

    def __TEST__(self, f, filename):
        check = True
        begin_write = False
        test = re.compile(r'//\s?.*')
        for line in f:
            line = line.strip()
            if test.search(line):
                line = test.sub('', line)
            if re.search(r'/\*\*', line) and re.search(r'\*/', line):
                line = re.sub(r'/\*\*.*?\*/', '', line)
            elif re.search(r'/\*\*', line):
                line = re.sub(r'/\*\*.*?', '', line)
                check = False
            elif not check and not re.search(r'\*/', line):
                continue
            elif re.search(r'\*/', line):
                check = True
                continue
                re.sub(r'.*?\*/', '', line)
            if line.find('eval(') != -1:
                begin_write = True
            elif begin_write and (line.find('@Override') != -1
                                  or line.find('public') != -1):
                begin_write = False
                break
            if begin_write:
                self._write_fixed(line, filename)

#    def _cleaning(self, f, filename):
#
#        f = ' '.join(f.split())
        # first clean comments
        # if filename == '757092_assignsubmission_file_SelectQuery.java':
        # comments_regex = re.compile(
        #   r'/\**\s\*?\s?.*?\s?\*/|//*\s?.*?(?=})|(?=\n)', re.I)
        # f = comments_regex.sub('', f)
#        breakpoint()
#        if self.linestart.search(f) is None:
#            logging = open('LOGFILE.txt', 'a')
#            logging.write('linestart.search => None: ' + filename + '\n')
#            logging.close()
#            return 0
#        start_indx = self.linestart.search(f).end()
#        if self.lineend.search(f) is None:
#            logging = open('LOGFILE.txt', 'a')
#            logging.write('lineend.search => None: ' + filename + '\n')
#            logging.close()
#            return 0
#        end_indx = self.lineend.search(f).start()

#        return f[start_indx:end_indx]

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
    linestart = re.compile(r'eval\s?\(table table\)\s?.*?{\s*', re.I)

    lineend = re.compile(r'.(?=@Override public\s?string\s?tostring\(\))',
                         re.I)

    # re.compile(
    #   r'.(?=public list<(insttuple)|(table.insttuple)> lookupbydept)', re.I)
    pathtofixed = 'javahw3/newfixed'
    pathtoold = 'javahw3/'
    a = fmt(linestart, lineend, pathtofixed, pathtoold)
    a.format()
