"""
tokenizer.py


A java lexer class


"""
import javac_parser
import os.path
from collections import Counter


class tokenizer():
    """
    ASSUMES FIXED FILE NAMES START WITH A LETTER IE f!!!!!!!!!!!!!!!!!!!!
    class tokenizer takes an input folder path, creates a tokenizer obj,
    and an output dictionary with each files lexed result held in a multidim
    string array"""

    def __init__(self, iff):
        self.outputDict = dict()
        self.inputFileFolder = iff
        self.summaryDict = dict()

    def folderRead(self):
        java = javac_parser.Java()
        dirlist = os.listdir(self.inputFileFolder)
        if self.inputFileFolder[-1] is not "/":
            self.inputFileFolder = self.inputFileFolder + "/"
        for item in dirlist:
            if os.path.isfile(self.inputFileFolder + item):
                with open(str(self.inputFileFolder + item), 'r+') as ifile:
                    self.outputDict[int(item[1:7])] = []
                    for line in ifile:
                        for tup in java.lex(line):
                            if tup[0] != 'EOF':
                                self.outputDict[int(item[1:7])].append(tup)

        self._postprocess(self.outputDict)

        for key in self.outputDict:
            self.outputDict[int(key)].append(
                self._summarize(self.outputDict[key]))

    def _summarize(self, tlist):
        c = Counter()
        for elem in tlist:
            c[elem[0]] += 1

        return c

    def _postprocess(self, tlist):
        tstring = ""
        rstring = ""
        for k, v in self.outputDict.items():
            for elem in v:
                tstring += str(elem[0]) + " "
                rstring += elem[1] + " "
            self.summaryDict[k] = (tstring, rstring)
            tstring = ""
            rstring = ""
