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

        if self.pathtofixed[-1] != '/':
            self.pathtofixed = ''.join((self.pathtofixed, '/'))
        if self.pathtoold[-1] != '/':
            self.pathtoold = ''.join((self.pathtofixed, '/'))
        try:
            os.path.exists(self.pathtofixed)
            os.path.exists(self.pathtoold)
        except FileNotFoundError:
            print('Error: check path for fixed and path to original files. ')
            print('fixed: {}', self.pathtofixed)
            print('orig: {}', self.pathtoold)

    def _read_space(self):
        self._fixfilepath()
        namelist = os.listdir(self.pathtoold)

        for filename in namelist:
            if os.path.isdir(filename) or filename[-5:] != ".java":
                continue
            f = open(self.pathtoold + filename, 'r')
            _to_analyze = f.read()
            f.close()
            if not len(_to_analyze):
                continue
            self._cleaning(_to_analyze, filename)

    def _cleaning(self, f, name):

        f = ' '.join(f.split())
        # first clean comments
        comments_regex = re.compile(r'/\**\s\*?\s?.*?\s?\*/|//\s?.*?[;\n]',
                                    re.I)
        f = comments_regex.sub('', f)
        if self.linestart.search(f) is None:
            logging = open('LOGFILE.txt', 'a')
            logging.write('linestart.search => None: ' + filename)
            logging.close()
        start_indx = self.linestart.search(f).end()
        if self.lineend.search(f) is None:
            logging = open('LOGFILE.txt', 'a')
            logging.write('lineend.search => None: ' + filename)
            logging.close()
        end_indx = self.lineend.search(f).start()
        student_code_start = f[start_indx:end_indx]

    def _analyze(self, f):
        # comments
        comments_regex = re.compile(r'/\**\s\*?\s?.*?\s?\*/|//\s?.*?[;\n]')
        f = f.split()
        f = ' '.join(f)

        breakpoint()
        match = self.linestart.search(f)
        assert match
        start = match.start()
        end = match.end()

        final_code = f[start:end]
        print(final_code)

    def format(self):
        self._read_space()
        exit()

        self._fixfilepath()
        namelist = os.listdir(self.pathtoold)
        self.linestart = ''.join(self.linestart.split())
        self.lineend = ''.join(self.lineend.split())
        for filename in namelist:
            if os.path.isdir(filename) or filename[-5:] != ".java":
                continue
            linesnum = []
            lineenum = 0
            num = 0
            check = False
            with open(self.pathtoold + filename, 'r') as f:
                for line in f:
                    num += 1
                    line = ''.join(line.split())
                    if self.linestart in line:
                        check = True
                    elif check and not line.startswith(
                            '/') and not line.startswith('*'):
                        linesnum.append(num)
                    elif line == self.lineend:
                        lineenum = num
            num = 0
            check = False
            with open(self.pathtofixed + 'f' + filename, 'w') as nf:
                with open(self.pathtoold + filename, 'r') as f:
                    for line in f:
                        num += 1
                        if num in linesnum:
                            nf.write(line)
                        if num + 1 == lineenum:
                            break


if __name__ == "__main__":
    #    linestart = input("start string: ")
    #    lineend = input("end string: ")
    #    pathtofixed = input("fixed file path: ")
    #    pathtoold = input("pathtoold to read from: ")
    #    format(linestart, lineend, pathtofixed, pathtoold)
    linestart = re.compile(r'lookup\(string id\)\s?.*?{\s*',
                           re.I)

    lineend = re.compile(r'.(?=public list<(insttuple)|(table.insttuple)> lookupbydept)', re.I)
    pathtofixed = 'javahw1/fixed'
    pathtoold = 'javahw1/'
    a = fmt(linestart, lineend, pathtofixed, pathtoold)
    a.format()
