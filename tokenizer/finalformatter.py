import os
import os.path
# parames used: linestart = 'publicInstTuplelookup(StringID){'

# self.lineend = /**


class fmt:
    def __init__(self, linestart, lineend, pathtofixed, pathtoold):
        self.linestart = linestart
        self.lineend = lineend
        self.pathtofixed = pathtofixed
        self.pathtoold = pathtoold

    def _fixfilepath(self):

        if self.pathtofixed[-1] != '/':
            self.pathtofixed = ''.join([self.pathtofixed, '/'])
        if self.pathtoold[-1] != '/':
            self.pathtoold = ''.join([self.pathtofixed, '/'])
        try:
            os.path.exists(self.pathtofixed)
            os.path.exists(self.pathtoold)
        except FileNotFoundError:
            print('Error: check path for fixed and path to original files. ')
            print('fixed: {}', self.pathtofixed)
            print('orig: {}', self.pathtoold)

    def format(self):
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
    linestart = 'lookup(StringID)'
    lineend = '/**'
    pathtofixed = 'javahw1/fixed'
    pathtoold = 'javahw1/'
    a = fmt(linestart, lineend, pathtofixed, pathtoold)
    a.format()
